import time
import random
from tests import test_routes

COMMANDS = {
    'start': 'Gives information about the bot',
    'help': 'Gives information about all of the available commands',
    'ping': 'Measure the execution time to run test and send a message',
    'caps your sentence': 'Converts your sentence to uppercase',
    'rand your sentence': 'Choose a random word from sentence, separated by space',
    'team n_team your sentence': 'Generate a random team from sentence, separated by space'
}


def get_running_time(start_time):
    test_routes.test_index()
    return time.time() - start_time


def get_random_team(n_team, member_list):
    result = ''
    if n_team > len(member_list):
        result = 'Too many teams!'
    elif n_team < 1:
        result = 'Too few teams!'
    else:
        n_plus = len(member_list) % n_team
        length = len(member_list)
        result = ''
        for i in range(n_team):
            result += 'Team {}:\n'.format(i+1)
            if i < n_plus:
                result += member_list.pop(
                    random.randint(0,
                                   len(member_list) - 1)) + '\n'
            for j in range(length // n_team):
                result += member_list.pop(
                    random.randint(0,
                                   len(member_list) - 1)) + '\n'
            result += '\n'
    return result


def hello():
    return "Hello, World!"


def content():
    return '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            '''
