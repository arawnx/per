from commands import *


class CompleteCommand(Command):
    def __init__(self, idx):
        super(CompleteCommand, self).__init__()
        self.idx = idx

    def execute(self, items):
        items[self.idx].completed_date = datetime.now().strftime("%Y/%m/%d %H:%M")


