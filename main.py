#!/usr/bin/env python3
from argparse import ArgumentParser
from hello import SDK_MONIKER, format_as_ndjson

def main():

    arguments = ArgumentParser(
        description='',
    )

    arguments.add_argument('-m', '--message', type=str, required=False, default='hello python', help='')
    arguments.add_argument('-v', '--version', action='version', version=SDK_MONIKER, help='Show version and exit')    
    args = arguments.parse_args()

    obj = {"messsage": args.message}
    print(format_as_ndjson(obj))

if __name__ == '__main__':
    main()
