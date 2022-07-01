#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 
if __name__== "__main__":
  
  for line in sys.stdin:
    vector= line.split('\n')[0]
    datos=vector.split(',')
    sys.stdout.write("{},{}\n".format(datos[0],datos[1]))
