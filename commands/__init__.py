from datetime import datetime

from main import Command, Item

from commands.add import *
from commands.delete import *
from commands.complete import *
from commands.listall import *
from commands.projects import *
from commands.inbox import *
from commands.edit import *
from commands.tickled import *


class CommandInterpret:
    def __init__(self):
        pass

    def to_command(self, args):
        if args[0].startswith("a"):
            return AddCommand(args[1])
        elif args[0].startswith("d"):
            arg_idx = int(args[1])
            return DeleteCommand(arg_idx)
        elif args[0].startswith("c"):
            arg_idx = int(args[1])
            return CompleteCommand(arg_idx)
        elif args[0].startswith("l") or args[0] == "ls":
            return ListCommand()
        elif args[0].startswith("i"):
            return InboxFilterCommand()
        elif args[0].startswith("p"):
            return ProjectsFilterCommand()
        elif args[0].startswith("e"):
            return EditCommand()
        elif args[0].startswith("t"):
            return TickledFilterCommand()
