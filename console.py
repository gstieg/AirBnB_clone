#!/usr/bin/python3
""" add the new cmds"""
import json
import cmd

class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, args):
       """quit the command"""
       exit()        

    def do_EOF(self, args):
        """ quits after reaching end of file"""
        return True

    def empty_line(self,args):
        """ dosent execute on empty line"""
        pass

    

if __name__ == "__main__":
    HBNBCommand().cmdloop()
