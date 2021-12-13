# file_parser_with_description.py

import argparse

def file_parser(input_file, output_file=''):
    print(f'Processing {input_file}')
    print('Finished processing')
    if output_file:
        print(f'Creating {output_file}')

def main():
    parser = argparse.ArgumentParser(
            'File parser',
            description='PyParse - The File Processor',
            epilog='Thank you for choosing PyParse!',
            )
    parser.add_argument('--infile', help='Input file for conversion')
    parser.add_argument('--out', help='Converted output file')
    args = parser.parse_args()
    if args.infile:
        file_parser(args.infile, args.out)

if __name__ == '__main__':
    main()
