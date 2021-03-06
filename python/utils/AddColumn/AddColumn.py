#!/usr/bin/env python3

'''

    Add one or more columns.

    @Author: wavefancy@gmail.com, Wallace Wang.

    Usage:
        AddColumn.py -c int (-v text | -i int) [-t txt]
        AddColumn.py -h | --help | --version | -f | --format

    Notes:
        1. Read data from stdin, and output to stdout.

    Options:
        -c int        After which column(int, 1 based) from the input for insertting new column.
        -v text       The value for the new insertting column(s).
                        eg. v1|v1,v2. v1,v2 add two columns, split values by ','
        -t text       The title for the new insertting column(s).
                        eg. t1|t1,t2. Split values by ','. len(-t) == len(-v).
        -i int        Add index value for each row, index start from 'int'.
        -h --help     Show this screen.
        --version     Show version.
        -f --format   Show input/output file format example.

'''
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) #prevent IOError: [Errno 32] Broken pipe. If pipe closed by 'head'.
from docopt import docopt

def ShowFormat():
    '''File format example'''
    print('''
#Input file format(stdin)
------------------------
1       2
1       2

cat test.txt | python3 AddColumn.py -c 1 -v 0,0 -t t1,t2
------------------------
1       t1      t2      2
1       0       0       2

cat test.txt | python3 AddColumn.py -c 1 -i 3
1       3       2
1       4       2
          ''');

if __name__ == '__main__':
    args = docopt(__doc__, version='1.0')
    # print(args)
    # sys.exit(-1)

    if(args['--format']):
        ShowFormat()
        sys.exit(-1)

    COL     = int(args['-c'])
    VALS    = args['-v'].split(',') if args['-v'] else None
    INDEXV  = int(args['-i'])       if args['-i'] else None
    TITLES  = args['-t'].split(',') if args['-t'] else VALS
    if VALS and len(VALS) != len(TITLES):
        sys.stderr.write('ERROR: the element length for -t and -v should be the same!\n')
        sys.exit(-1)

    for line in sys.stdin:
        line = line.strip()
        if line :
            ss = line.split()
            out = ss[:COL]
            if TITLES:
                out = out + TITLES + ss[COL:]
                TITLES = None
            else:
                if VALS:
                    out = out + VALS + ss[COL:]
                else:
                    out = out + [str(INDEXV)] + ss[COL:]
                    INDEXV += 1

            sys.stdout.write('%s\n'%('\t'.join(out)))

sys.stdout.flush()
sys.stdout.close()
sys.stderr.flush()
sys.stderr.close()
