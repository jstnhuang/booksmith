import argparse
import importlib
import os
from xml.etree import ElementTree

import cse101


class Booksmith(object):
    def __init__(self, input_dir, output_dir):
        self._input_dir = input_dir
        self._output_dir = output_dir

    def start(self):
        if not os.path.isdir(self._output_dir):
            os.makedirs(self._output_dir)

        for filename in os.listdir(self._input_dir):
            input_path = os.path.join(self._input_dir, filename)
            tree = ElementTree.parse(input_path)
            output_tree = cse101.convert(tree)
            output_name = os.path.join(self._output_dir, filename[:-4])
            output_name = '{}.html'.format(output_name)
            output_tree.write(output_name, encoding='unicode', method='html')


def main():
    parser = argparse.ArgumentParser(
        description='Convert XML notes into CSE 101 HTML.')
    parser.add_argument('input_dir', help='Directory with the input files.')
    parser.add_argument('--output_dir',
        default='output',
        help='Output directory (default: output/)')
    args = parser.parse_args()
    booksmith = Booksmith(args.input_dir, args.output_dir)
    booksmith.start()


if __name__ == '__main__':
    main()
