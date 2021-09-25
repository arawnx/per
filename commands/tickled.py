from main import text_yellow, text_red, text_blue, text_green, text_gray, text_italic
from datetime import timedelta
import datetime
from commands import *


class TickledFilterCommand(Command):
    def __init__(self):
        super(TickledFilterCommand, self).__init__()

    def is_tickled(self, item):
        res = False
        if "TICKLED" in item.tags and item.defer_date != "":
            res = True
        return res

    def execute(self, items):
        for id, item in items.items():
            if not self.is_tickled(item):
                continue
            # Print main section of item
            defer_in_past = datetime.strptime(item.defer_date, "%Y/%m/%d %H:%M").timestamp() <= datetime.now().timestamp()
            if defer_in_past:
                print(f"{id} {item.title}\t", end='')
            else:
                print(text_italic(text_gray(f"{idx} {item.title}\t")), end='')
            list_attributes = []
            if item.defer_date != "":  # Should always resolve to True
                list_attributes.append(text_green(item.defer_date) if defer_in_past else text_yellow(item.defer_date))
            if item.project != "":
                list_attributes.append(text_blue(item.project))
            if item.flagged:
                list_attributes.append(text_red("!"))
            # Print other attributes in brackets
            for idx, attr in enumerate(list_attributes):
                # Enable bold
                print("\033[1m", end='')
                if idx == list_attributes.__len__() - 1 == 0:
                    print(f"[{attr}] ", end='')
                elif idx == 0:
                    print(f"[{attr}", end='')
                elif idx >= list_attributes.__len__() - 1:
                    print(f"|{attr}] ", end='')
                else:
                    print(f"|{attr}", end='')
            # Reset from bold
            print("\033[0m", end='')
            print("")
