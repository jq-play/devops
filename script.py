import re
import argparse


def main(file_input, file_output):
    with open(file_input, 'r') as fin:
        content = ''.join(fin.readlines())

        content = re.sub(r'</.+?>', '', content)
        content = re.sub(r'<ul>|<p>', '', content)
        content = re.sub(r' *<li>', '- ', content)
        content = re.sub(r' *<h1>', '# ', content)

        with open(file_output, 'w') as fout:
            fout.write(content)


if __name__ == '__main__':
    argParser = argparse.ArgumentParser(
        prog='workflow testing',
        epilog='workflow testing'
    )

    argParser.add_argument(
        'input',
        help='in'
    )

    argParser.add_argument(
        'output',
        help='out'
    )

    args = argParser.parse_args()

    input_file = args.input
    out = args.output

    main(input_file, out)
