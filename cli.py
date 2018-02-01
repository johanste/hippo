import sys

import _parser

def pack(module):
    pass

def cli(args):
    parser = _parser._create_parser()
    ns = parser.parse_args(args)

if __name__ == "__main__":
    cli(sys.argv)