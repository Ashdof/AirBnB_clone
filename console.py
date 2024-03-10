#!/usr/bin/python3
"""Module for command line interface implementation"""

import cmd
import json
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Implementation of command line interface"""

    prompt = "(hbnb) "
    cmds_models = ["BaseModel", "User", "State", "City", "Amenity",
                   "Place", "Review"]
    cmds = ["create", "show", "update", "destroy", "all"]

    def precmd(self, arg):
        """Parse Input

        Description:
        Parses the command input

        Args:
        args (str): the input command
        """

        if "." in arg and "(" in arg and ")" in arg:
            cls = arg.split(".")
            cn = cls[1].split("(")
            args = cn[1].split(")")

            if cls[0] in HBNBCommand.cmds_models and cn[0] in HBNBCommand.cmds:
                arg = cn[0] + " " + cls[0] + " " + args[0]

        return arg

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

    def do_create(self, arg_model):
        """Create New Instance

        Description:
        Creates a new instance of a model, saves it in the
        JSON file and prints its id to the console.

        Args:
        arg_model (model): the type of model to create
        """

        if not arg_model:
            print("** class name missing **")
        elif arg_model not in HBNBCommand.cmds_models:
            print("** class doesn't exist **")
        else:
            dict_models = {"BaseModel": BaseModel, "User": User,
                           "State": State, "City": City, "Amenity": Amenity,
                           "Place": Place, "Review": Review}

            obj_model = dict_models[arg_model]()
            print(obj_model.id)
            obj_model.save()

    def do_show(self, args):
        """Print Instances

        Description:
        Prints the string representation of an instance based
        on the model name and id.

        Args:
        args (model): the model's name and id
        """

        if not args:
            print("** class name missing **")
            return

        arg = args.split(" ")

        if arg[0] not in HBNBCommand.cmds_models:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()

            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id

                if obj_name == arg[0] and obj_id == arg[1].strip('"'):
                    print(value)
                    return

            print("** no instance found **")

    def do_destroy(self, args):
        """Delete Instance

        Description:
        Deletes an instance based on the model's name and id

        Args:
        args (model): the model's name and id
        """

        if not args:
            print("** class name missing **")
            return

        arg = args.split(" ")

        if arg[0] not in HBNBCommand.cmds_models:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()

            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id

                if obj_name == arg[0] and obj_id == arg[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return

            print("** no instance found **")

    def do_all(self, args):
        """Print All Instances

        Description:
        Prints the string representation of all instances of a
        given model. In the absence of a model, it prints all
        instances of all models.

        Args:
        args (model): an optional model's name
        """

        if not args:
            print("** class name missing **")
            return

        arg = args.split(" ")

        if arg[0] not in HBNBCommand.cmds_models:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_objs = []

            for key, value in all_objs.items():
                obj_name = value.__class__.__name__

                if obj_name == arg[0]:
                    list_objs += [value.__str__()]
            print(list_objs)

    def do_update(self, args):
        """Update Instance Attributes

        Description:
        Updates the attributes of an instance of a given model
        based on the model's name and id

        Args:
        args (model): the name and id of a given model
        """

        if not args:
            print("** class name missing **")
            return

        argv = ""
        for arg in args.split(","):
            argv += arg

        arg = shlex.split(argv)

        if arg[0] not in HBNBCommand.cmds_models:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()

            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id

                if obj_name == arg[0] and obj_id == arg[1].strip('"'):
                    if len(arg) == 2:
                        print("** attribute name missing **")
                    elif len(arg) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, arg[2], arg[3])
                        storage.save()
                    return

            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
