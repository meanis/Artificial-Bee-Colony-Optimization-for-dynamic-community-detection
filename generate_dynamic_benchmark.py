import rdyn
import sys

def main(argv):
    
    gen = rdyn.RDyn()
    gen.execute(simplified=True)

if __name__ == '__main__':
    sys.exit(main(sys.argv))