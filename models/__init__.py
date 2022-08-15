#!/usr/bin/python3
"""
Init file for models package
Create variable storage an instance of fileStorage
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
