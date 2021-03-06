import argparse

from gendiff import generator


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('-f', '--format',
                    help='set format of output')
parser.add_argument('first_file')
parser.add_argument('second_file')

args = parser.parse_args()


def main():
    diff = generator.generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
