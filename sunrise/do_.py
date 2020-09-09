from . import actions


def do(command):
    action, params = actions.find(command)
    return action(**params).execute()

