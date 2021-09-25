from commands import *

from subprocess import run


class EditCommand(Command):
    def __init__(self):
        super(EditCommand, self).__init__()

    def execute(self):
        run(["vim", "items.yaml"])
