#!python3

import argparse


def get_args():
    """ """

    parser=argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )
#    return parser.parse_args()

    parser.add_argument('-x', action='store',required=True,
                        help='Help text for option X')
    parser.add_argument('-y', help='Help text for option Y', default=False)
    print(parser.parse_args())


if __name__ == '__main__':
    get_args()
