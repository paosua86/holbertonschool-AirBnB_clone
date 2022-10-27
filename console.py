#!/usr/bin/python3
"""
entry point of the command interprete
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from models.user import User
from models.place import Place
import shlex  # splits the line along spaces except in double quotes


class_items = {"BaseModel": BaseModel, "User": User, "Review": Review,
               "Amenity": Amenity, "City": City,
               "State": State, "Place": Place}


class HBNBCommand(cmd.Cmd):
    """command interprete"""

    prompt = "(hbnb) "

    def precmd(self, arg):
        args = arg.split(".")
        if len(args) > 1:
            tmp = args[1].split('(')[0]
            args_new = tmp+" "+args[0]
            return (args_new)
        else:
            return args[0]

    def do_quit(self, arg):
        """to exit the program"""
        return True

    def do_EOF(self, arg):
        """exit"""
        return True

    def emptyline(self):
        """ignores emptyline"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id"""

        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] in class_items:
            new_instance = class_items[args[0]]()
            print(new_instance.id)
            new_instance.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""

        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] in class_items:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on
        the class name and id"""

        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] in class_items:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of
        all instances based or not on the class name"""
        args = shlex.split(args)
        dict1 = storage.all()

        if not args:
            print([str(value) for value in dict1.values()])
            return
        if args[0] in class_items:
            print([str(value) for key, value in dict1.items()
                  if key.split(".")[0] == args[0]])
            return
        print("** class doesn't exist **")

    def do_update(self, args):
        """ method that updates an object """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in class_items:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if '{}.{}'.format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        updated_content = storage.all()['{}.{}'.format(args[0], args[1])]
        setattr(updated_content, args[2], args[3])
        updated_content.save()

    def do_count(self, args):
        """count # of instances of a class"""
        args = shlex.split(args)
        counter = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                counter += 1
        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
