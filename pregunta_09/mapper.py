#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

import sys
if __name__ == "__main__":
    tabla = [line.replace("\n", "") for line in sys.stdin]
    tabla = [line.split("   ") for line in tabla]
    colum0 = [tabla[i][0] for i in range(len(tabla))]
    colum1 = [tabla[i][1] for i in range(len(tabla))]
    colum2 = [tabla[i][2] for i in range(len(tabla))]

    for line in range(len(tabla)):
        sys.stdout.write("{},{},{}\n".format(colum0[line], colum1[line], colum2[line]))
