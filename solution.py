import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-k","--key", nargs='+')
parser.add_argument('-v','--value')

args = parser.parse_args('--k i am heare!'.split())
if args.value:
    print('Ho-Ho, i save it!')
else:
    print('Dont say, jast looke! {}'.format(args.key))
