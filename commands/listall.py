from commands import *
from main import text_blue, text_red


class ListCommand(Command):
    def __init__(self):
        super(ListCommand, self).__init__()

    def execute(self, items):
        for idx, item in enumerate(items):
            # Print main section of item
            print(f"{idx} {item.title}\t", end='')
            list_attributes = []
            if item.project != "":
                list_attributes.append(text_blue(item.project))
            if item.flagged:
                list_attributes.append(text_red("!"))
            # Print other attributes in brackets
            for idx, attr in enumerate(list_attributes):
                # Enable bold
                print("\033[1m", end='')
                if idx == list_attributes.__len__()-1 == 0:
                    print(f"[{attr}] ", end='')
                elif idx == 0:
                    print(f"[{attr}", end='')
                elif idx >= list_attributes.__len__()-1:
                    print(f"|{attr}] ", end='')
                else:
                    print(f"|{attr}", end='')
            # Reset from bold
            print("\033[0m", end='')
            print("")


