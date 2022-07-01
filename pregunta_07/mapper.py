#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
  
  
    for line in sys.stdin:
      l= line.split(' ')[0]
      f= line.split(' ')[1]
      nu= int(line.split(' ')[2])
      sys.stdout.write("{}\t{}\t{}\n".format(l,f,n))
