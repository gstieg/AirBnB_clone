#!/usr/bin/python3
'''console for HBNB'''

import json
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = "(hbnb) "
    classes = {"BaseModel", "User", "City", "Amenity", "Review", "State",
               "Place"}
    classes = {
        "BaseModel",
        "User",
        "City",
        "Amenity",
        "Review",
        "State",
        "Place"
        }

    def do_quit(self, args):
        """quit the command"""
        return True

    def do_EOF(self, args):
        """ quits after reaching end of file"""
        return True

    def empty_line(self, args):
        """ dosent execute on empty line"""
        pass

    def do_create(self, args):
        '''creats a new instansce of basemodel, saves to json, then id print'''
        argv = args.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.classes:
            print("** class dosen't exist **")
        else:
            instance = eval("{}()".format(args))
            instance.save()
            print(instance.id)

    def do_show(self, line):
        ''' prints string representation of an instance based on the class'''
        argv = line.split()
        if len(argv) == 0:
            print('** class name missing **')
        elif argv[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        else:
            show = storage.all()
            key = str(argv[0]) + '.' + str(argv[1])
            if key in show:
                print(show[key])
            else:
                print("** no instance found **")

    def do_all(self, args):
        ''' prints str representation of all instances'''
        show = storage.all()
        list_obj = []
        if not args:
            for key, obj in show.items():
                list_obj.append(str(obj))
            print(list_obj)
        else:
            argv = args.split()
            if argv[0] not in self.classes:
                print("** class dosen't exist **")
            else:
                for key, obj in show.items():
                    instance = obj.to_dict()
                    if instance['__class__'] == argv[0]:
                        list_obj.append(str(show[key]))
                        print(list_obj)
                        print(list_obj)
                        print(list_obj)

    def do_destroy(self, args):
        ''' deletes an instance based on its class name and id'''
        argv = args.split()
        if len(argv) == 0:
            print('** class name missing **')
        elif argv[0] not in self.classes:
            print("** class dosen't exist **")
        elif len(argv) < 2:
            print('** instance id missing **')
        else:
            show = storage.all()
            key = str(argv[0]) + '.' + str(argv[1])
            if key in show:
                del show[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, args):
        ''' update instance based on the class name and id
            if not created, one will be created
        '''
        argv = args.split()
        if len(argv) == 0:
            ''' update instance based on the class name and id
            if not created, one will be created
            '''
        argv = args.split()
        if len(argv) == 0:
            ''' update instance based on the class name and id
            if not created, one will be created
        '''
        argv = args.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif len(argv) == 2:
            print("** attribute name missing **")
        elif len(argv) == 3:
            print("** value missing **")
        else:
            show = storage.all()
            key = str(argv[0]) + '.' + str(argv[1])
            if key in show:
                setattr(show[key], argv[2], argv[3])
                storage.save()
            else:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
