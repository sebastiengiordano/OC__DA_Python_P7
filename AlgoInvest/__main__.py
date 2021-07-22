from genericpath import exists
from time import time
from argparse import ArgumentParser
from memory_profiler import profile

from AlgoInvest.brutal_force.brutal_force import brutal_force
from AlgoInvest.brutal_force.brutal_force_itertools import (
    brutal_force_itertools)
from AlgoInvest.brutal_force.brutal_force_optimized import brutal_force_optimized
from AlgoInvest.optimized.glutton import glutton
from AlgoInvest.optimized.path_pattern import path_pattern
from .utils.path_manager import path_join, folder_path


def set_parser():
    parser = ArgumentParser(
        description=(
            "Run brutal_force or optimized algorithm,\n"
            + "on specified file or on default shares file."))
    parser.add_argument(
        "-bf", "--brutal_force",
        help='If set, used brutal_force algorithm',
        action='store_true', required=False)
    parser.add_argument(
        "-bfi", "--brutal_force_itertools",
        help='If set, used brutal_force_itertools algorithm',
        action='store_true', required=False)
    parser.add_argument(
        "-g", "--glutton",
        help='If set, used glutton algorithm',
        action='store_true', required=False)
    parser.add_argument(
        "-p", "--path_pattern",
        help='If set, used path pattern algorithm',
        action='store_true', required=False)
    parser.add_argument(
        "-ap", "--absolute_path",
        help='File absolute path which contains share\'s informations',
        type=str,
        required=False)
    parser.add_argument(
        "-rp", "--relative_path",
        help=(
            'File relative path, from AlgiInvest/data,'
            + 'which contains share\'s informations'),
        type=str,
        required=False)
    return parser.parse_args()


def set_data_path(args):
    default_data_folder = path_join(
        folder_path(__file__),
        "./data"
        )

    if args.absolute_path is not None:
        path = args.absolute_path
        print(f"\n\tabsolute_path: {path}")
    elif args.relative_path is not None:
        path = path_join(default_data_folder, args.relative_path)
        print(f"\n\trelative_path: {path}")
    else:
        path = path_join(default_data_folder, "actions_list.csv")
        print(f"\n\tdefault path: {path}")

    if not exists(path):
        import errno
        import os
        raise FileNotFoundError(
            errno.ENOENT,
            os.strerror(errno.ENOENT),
            path)
    else:
        return path

@profile(precision=4, )
def run_algo(args, path):
    no_algo_set = True
    start = time()
    if args.brutal_force:
        no_algo_set = False
        brutal_force(path, start)
    if args.brutal_force_itertools:
        no_algo_set = False
        start = time()
        brutal_force_itertools(path, start)
    if args.glutton:
        no_algo_set = False
        start = time()
        glutton(path)
    if args.path_pattern:
        no_algo_set = False
        start = time()
        path_pattern(path, start)
    if no_algo_set:
        brutal_force_optimized(path, start)

    print(f"\n\tAlgo duration: {(time() - start):.3f}s")


if __name__ == '__main__':
    args = set_parser()
    path = set_data_path(args)
    run_algo(args, path)

    # s=time()
    # for _ in range(100):
    #     run_algo(args, path)
    # print(f"\n\tAlgo mean duration: {(time() - s)/100:.3f}s")
