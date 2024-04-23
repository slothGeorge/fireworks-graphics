import argparse
from game import Game


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sparks-amount-range', '-s', type=str, default='20-30',
                        help='Sets a range amount of sparks. Min=20, Max=30')
    args = parser.parse_args()

    amount_of_sparks_range = tuple(int(num) for num in args.amount_of_sparks_range.split('-'))
    return amount_of_sparks_range


if __name__ == '__main__':
    parse_args()
    application = Game()
    application.run()
