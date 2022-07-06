#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys
if __name__ == "__main__":
    tab = [line.replace("\n", "") for line in sys.stdin]
    tab = [line.split("   ") for line in tab]
    colum0 = [tab[i][0] for i in range(len(tab))]
    colum2 = [tab[i][2] for i in range(len(tab))]

    for line in range(len(tabla)):
        sys.stdout.write("{}\t{}\n".format(colum0[line],colum2[line]))
