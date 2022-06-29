#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        vec=line.split('\n')[0]
        cred=vec.split(',')[2]
        sys.stdout.write("{}\t1\n".format(cred))
