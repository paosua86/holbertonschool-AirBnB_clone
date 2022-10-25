#!/usr/bin/python3
"""
entry point of the command interprete
"""
import cmd




class HBNBCommand(cmd.Cmd):
    """command interprete"""


    prompt = "(hbnb) "

    def do_quit(self, arg):
        """to exit the program"""
        return True

    def do_EOF(self, arg):
        """exit"""
        return True

    def emptyline(self):
        """ignores emptyline"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
