from rdyn import RDyn
import sys

def main(argv):

    gen = RDyn()
    gen.execute(simplified=True)

if __name__ == '__main__':
    sys.exit(main(sys.argv))