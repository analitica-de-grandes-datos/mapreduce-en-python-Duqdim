#
# >>> Escriba el codigo del mapper a partir de este punto <<<

import sys
if __name__ == "__main__":
    tab = [line.replace("\n", "") for line in sys.stdin]
    tab = [line.split("   ") for line in tab]
    colum = [tabla[i][1] for i in range(len(tab))]
    colum = [line.split("-") for line in colum]
    colum1 = [colum[i][1] for i in range(len(colum))]

    for line in colum1:
        sys.stdout.write("{}\t1\n".format(line))
