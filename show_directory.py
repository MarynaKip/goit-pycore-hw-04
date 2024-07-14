import sys
from pathlib import Path
from colorama import Fore
import os

try:
    path = Path(sys.argv[1])

    def parse_file(path, depth_level = 0):
        for el in path.iterdir():
            if el.is_dir():
                print(Fore.BLUE + ' ' * 4 * depth_level + str(el).split('/')[-1] + '/')
                parse_file( path = el, depth_level = depth_level+1 )
            else:
                print(Fore.GREEN + ' ' * 4 * depth_level + str(el).split('/')[-1])

    parse_file(path)
except FileNotFoundError:
    print('Wrong directory!')
except IndexError as err:
    print('Path should be passed as an argument!')
