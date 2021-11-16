import argparse


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-x', '--execute', action="store",
                        help='Help text for option X')
    group.add_argument('-y', help='Help text for option Y', default=False)

    parser.add_argument('-z', help='Help text for option Z', type=int)
    print(parser.parse_args())

if __name__ == '__main__':
    get_args()