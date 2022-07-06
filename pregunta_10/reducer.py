#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

from collections import defaultdict
import operator

if __name__ == '__main__':

    dicciona = defaultdict(list)

    for line in sys.stdin:

        numero, val = line.replace("\n","").strip().split("	")
        val = val.split(",")
        numero = int(numero)
        for elemento in val:
            dicciona[elemento].append(numero)

    dicciona1 = sorted(diccio.items(), key = operator.itemgetter(0))

    for clave, valor in dicciona1:
        num = sorted(valor, key = int)
        val = ",".join(map(str, num))
        sys.stdout.write("{}	{}\n".format(clave, val))
