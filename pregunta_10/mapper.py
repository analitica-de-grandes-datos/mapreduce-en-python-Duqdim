#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    tab = [line.replace("\n", "") for line in sys.stdin]
    tab = [line.split("	") for line in tabla]
    colum0 = [tabla[i][0] for i in range(len(tabla))]
    colum1 = [tabla[i][1] for i in range(len(tabla))]

    for line in range(len(tab)):
        sys.stdout.write("{}\t{}\n".format(colum0[line],colum1[line]))
