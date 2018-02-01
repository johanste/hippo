import argparse
import os
import zipfile

def pack(ns):
    with zipfile as zipfile.ZipFile()
        zipfile.write(ns.module)
        for module_reference in 

def eval(ns):
    pass

def _create_parser():
    parser = argparse.ArgumentParser(prog='hippo')
    sbs = parser.add_subparsers(title='action')

    pack_parser = sbs.add_parser('pack')
    pack_parser.add_argument('module', help='Module to pack')
    pack_parser.add_argument('--repository', '-r', nargs='+')
    pack_parser.add_argument('--name', '-n', help='Name of generated module')
    pack_parser.set_defaults(func=pack)

    eval_parser = sbs.add_parser('eval', help='evaluate the given module')
    eval_parser.add_argument('module')
    eval_parser.add_argument('parameters', nargs='+')
    eval_parser.add_argument('references', nargs='+')

     return parser