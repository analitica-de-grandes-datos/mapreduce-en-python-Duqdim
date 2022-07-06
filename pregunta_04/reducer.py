#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    tot = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == curkey:

            tot += val
        else:

            if curkey is not None:

                sys.stdout.write("{},{}\n".format(curkey, tot))

            curkey = key
            tot = val

    sys.stdout.write("{},{}\n".format(curkey, tot))
