0x00. AirBnB clone - The console
Group project
Python
OOP
 By: Guillaume
 Weight: 5
 Project to be done in teams of 2 people (your team:  Binyam Tegene, Michael Goboola)
 Project will start Aug 1, 2022 6:00 AM, must end by Aug 8, 2022 6:00 AM
 will be released at Aug 6, 2022 12:00 PM
 Manual QA review must be done (request it when you are done with the project)
 An auto review will be launched at the deadline
Concepts
For this project, we expect you to look at these concepts:

Python packages
AirBnB clone

## Project Description

- A command interpreter to manage our AirBnB objects. The main purpose is to create all classes for AirBnB(`User`, `City`, `Place...) that inherit from a `BaseModel, create a class that takes care of the initialization, serialization and deserialization of instances, an
abstracted storage engine, and unit tests to validate all classes and the storage engine.

## How to use

### In interactive mode

```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
```
### In non-interactive mode

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Functions of the consonle

`quit:` Quit command to exit the program

`EOF:` method to EOF to exit with (CTRL + D)

`empyline:` an empty line + ENTER shouldn’t execute anything

`create:` Create a new object (ex: a new User or a new Place)

`show:` Prints the string representation of an instance based on the class name and id.

`destroy:` Deletes an instance based on the class name and id

`all:` Prints all string representation of all instances based or not on the class name.

`update:` Update attributes of an object


## Directory and File Descriptions

`models` - Contains models used in Airbnb.

`models/engine/file_storage.py` - Used to serialize and deserialize python objects to and from a json file.

`models/base_model.py` - Base class from which other models inherit. Has methods to convert an object to
a dictionary and save it to the storage engine.

`models/city.py, amenity.py, place.py, review.py, state.py, user.py` - These are the different entities that inherit from `base_model.py` and are used each for a different purpose as their name suggests. More information is provided in each module.

`console.py` - It is the command line interpreter from which commands are initiated to perform CRUD operations on the above mentioned models.

`AUTHORS` - Lists all individuals having contributed content to the repository.


### Authors
- [ ] Michael Goboola
- [ ] Kayongo Johnson Brian