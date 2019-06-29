#!/usr/bin/python3
""" add the new cmds"""
import json
import cmd

class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = ("(hbnb)")

    def quit(self, args):
       """quit the command"""
       return True

    def EOF(self, args):
        """ quits after reaching end of file"""
        return True
