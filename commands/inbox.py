from commands import *


class InboxFilterCommand(Command):
    def __init__(self):
        super(InboxFilterCommand, self).__init__()

    def is_inbox(self, item):
        res = True
        if item.project != '':
            res = False
        return res

    def execute(self, items):
        for idx, item in enumerate(items):
            if not self.is_inbox(item):
                continue
            # Print main section of item
            print(f"{idx} {item.title}\t", end='')
            list_attributes = []
            if item.added_date != "": # Should always resolve to True
                list_attributes.append(text_green(item.added_date))
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


