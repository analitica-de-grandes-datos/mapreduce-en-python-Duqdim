#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator

if __name__ == '__main__':

    dicciona = {}

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
        dicciona[key] = val

    dicciona1 = sorted(diccio.items(), key = operator.itemgetter(1))

    for campo in dicciona1:
        sys.stdout.write("{},{}\n".format(campo[0], campo[1]))
