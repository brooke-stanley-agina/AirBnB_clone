#!/usr/bin/python3
"""
Module console
Entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ The AirBnB command line interpreter """
    prompt = "(hbnb) "
    valid_classes = {'BaseModel': BaseModel, 'User': User,
                     'City': City,
                     'Amenity': Amenity, 'Place': Place,
                     'Review': Review}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        save it to JSON file and prints the id
        """
        if len(line) == 0:
            self.perror(1)
        elif line not in HBNBCommand.valid_classes.keys():
            self.perror(2)
        else:
            model = HBNBCommand.valid_classes[line]()
            model.save()
            print(model.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        data = line.split()
        if len(line) == 0:
            self.perror(1)
        elif data[0] not in HBNBCommand.valid_classes.keys():
            self.perror(2)
        elif len(data) == 1:
            self.perror(3)
        else:
            # Create the key
            key = data[0] + "." + data[1]
            # Fetch all objects from file storage
            all_objs = storage.all()
            if key not in all_objs.keys():
                self.perror(4)
            else:
                print(all_objs[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        data = line.split()
        if len(line) == 0:
            self.perror(1)
        elif data[0] not in HBNBCommand.valid_classes.keys():
            self.perror(2)
        elif len(data) == 1:
            self.perror(3)
        else:
            # Create the key
            key = data[0] + "." + data[1]
            # Fetch all objects from file storage
            all_objs = storage.all()
            if key not in all_objs.keys():
                self.perror(4)
            else:
                del (all_objs[key])
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        all_instances = storage.all()
        if len(line) == 0:
            all_objs = []
            for k, obj in all_instances.items():
                all_objs.append(str(obj))
            print(all_objs)
        elif line in HBNBCommand.valid_classes.keys():
            objs = []
            for k, v in all_instances.items():
                if line == v.__class__.__name__:
                    key = line + "." + str(v.id)
                    objs.append(str(all_instances[key]))
            print(objs)
        else:
            self.perror(2)

    def do_update(self, line):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        data = line.split()
        if len(line) == 0:
            self.perror(1)
        elif data[0] not in HBNBCommand.valid_classes.keys():
            self.perror(2)
        elif len(data) == 1:
            self.perror(3)
        elif len(data) == 2:
            self.perror(5)
        elif len(data) == 3:
            self.perror(6)
        else:
            key = data[0] + "." + data[1]
            all_storage = storage.all()
            if key not in all_storage.keys():
                self.perror(4)
            else:
                obj = all_storage[key]
                setattr(obj, data[2], data[3])
                storage.save()

    def perror(self, code):
        """
        Helper function to print common errors
        """
        if code == 1:
            print("** class name missing **")
        elif code == 2:
            print("** class doesn't exist **")
        elif code == 3:
            print("** instance id missing **")
        elif code == 4:
            print("** no instance found **")
        elif code == 5:
            print("** attribute name missing **")
        elif code == 6:
            print("** value missing **")

    def default(self, line):
        """
        Used to handle commands for which there us no
        'do_xxx' methods
        In this case commands such as
            Object.all()
        """
        if len(line) == 0:
            return
        # Separate class from command
        data = line.split('.')
        # Pick the class
        cls = data[0]
        if cls in HBNBCommand.valid_classes:
            if len(data) == 2:
                if data[1] == "all()":
                    HBNBCommand.do_all(self, cls)
                if str(data[1])[:4] == "show":
                    obj_id = data[1][6:-2]
                    arg = str(cls) + " " + str(obj_id)
                    HBNBCommand.do_show(self, arg)
                if str(data[1])[:7] == "destroy":
                    obj_id = data[1][9:-2]
                    arg = str(cls) + " " + str(obj_id)
                    HBNBCommand.do_destroy(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
