#!/usr/bin/python3
"""Module for command line interface implementation"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Implementation of command line interface"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Pass

        Description:
        Executes nothing when the enter key is pressed over
        an empty line. The cursor jumps to the next line
        """

        pass

    def do_quit(self, line):
        """Quit Console

        Description:
        Exits the command line interface
        """

        return True

    def do_EOF(self, line):
        """Quit Console

        Description:
        Exits the command line interface
        """

        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
