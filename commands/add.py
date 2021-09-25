from commands import *


class AddCommand(Command):
    def __init__(self, title):
        super(AddCommand, self).__init__()
        self.title = title;

    def next_id(self, items):
        res = 0
        for item in items.values():
            if item.id > res:
                break
            else:
                res += 1
        return res

    def execute(self, items):
        new_id = self.next_id(items)
        new_item = Item(new_id)
        new_item.title = self.title
        items[new_id] = new_item
