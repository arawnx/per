from commands import *


class ProjectsFilterCommand(Command):
    def __init__(self):
        super(ProjectsFilterCommand, self).__init__()

    def execute(self, items):
        projects = {}
        # Parent projects
        for item in items:
            if item.project == '':
                continue

            if projects.get(item.project) is None:
                projects[item.project] = 1
            else:
                projects[item.project] += 1

        for project in sorted(projects.keys()):
            print(f"{project} [{projects[project]}]")
