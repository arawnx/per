import sys
from datetime import datetime

import yaml

from commands import *


def text_red(text):
    return f"\033[31m{text}\033[39m"


def text_yellow(text):
    return f"\033[33m{text}\033[39m"


def text_green(text):
    return f"\033[32m{text}\033[39m"


def text_gray(text):
    return f"\033[90m{text}\033[39m"


def text_blue(text):
    return f"\033[34m{text}\033[39m"


def text_italic(text):
    return f"\033[3m{text}\033[0m"


def text_bold(text):
    return f"\033[1m{text}\033[39m"

class Item:
    def __init__(self, id):
        self.id = id
        self.title = ""
        self.notes = ""
        self.due_date = ""
        self.defer_date = ""
        self.completed_date = ""
        self.dropped_date = ""
        self.added_date = datetime.now().strftime("%Y/%m/%d %H:%M")
        self.project = ""
        # Special tags:
        ## TICKLED — defer_date represents the tickled time that this item is waiting for
        self.tags = []
        self.estimated_duration = 0
        self.flagged = False
        self.review_frequency = ""
        self.repeat_frequency = ""
        self.status = ""


class Filter:
    def __init__(self):
        self.criterion = lambda x: True

    def filter_items(self, items):
        res = []
        for item in items:
            if self.criterion(item):
                res.append(item)
        return res


# Virtual
class Command:
    def __init__(self):
        pass

    def execute(self, items):
        pass


# TODO : Instead of just reading "items.yaml," let the user set an environment variable for the items directory
if __name__ == '__main__':
    command_interpret = CommandInterpret()
    command = command_interpret.to_command(sys.argv[1:])

    try:
        items_fl = open("items.yaml", "r")
        items_raw = items_fl.read()
        items_fl.close()
        items_ls = yaml.load(items_raw, Loader=yaml.Loader)
        items = {}
        for item in items_ls:
            items[item.id] = item
    except FileNotFoundError:
        print("Could not find items.yaml")
        items = {}

    if isinstance(command, EditCommand):
        command.execute()
    else:
        command.execute(items)
    # If you want to use arguments for a virtual function other than the base ones (self, items), do this:
    #   if isinstance(command, CustomCommandType):
    #       command.execute(items, custom_param)
    #       ...
    #   else:
    #       command.execute(items)

    items_fl = open("items.yaml", "w")
    items_ls = list(items.values())
    items_raw = yaml.dump(items_ls)
    items_fl.write(items_raw)
