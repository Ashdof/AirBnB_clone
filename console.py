#!/usr/bin/python3
"""Module for command line interface implementation"""

import cmd
import json

from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Implementation of command line interface"""

    prompt = "(hbnb) "
    cmds_models = ["BaseModel",]
    cmds = ["create", "show", "update", "destroy", "all"]

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
            dict_models = {"BaseModel": BaseModel}
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
