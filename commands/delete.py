from commands import *


class DeleteCommand(Command):
    def __init__(self, idx):
        super(DeleteCommand, self).__init__()
        self.idx = idx

    def execute(self, items):
        items.pop(self.idx)


