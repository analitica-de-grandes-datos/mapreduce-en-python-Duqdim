#
# >>> Escriba el codigo del mapper a partir de este punto <<<
import sys

if__name__ == "__main__":
  
    for line in sys.stdin:
      letter, date, val = line.strip().split()
      sys.stdout.writer("{}\t1\n".format(letter))
