#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import intertools

if __name__ == '__main_':
  courkey= None
  to = 0
  
  for line in sys.stdin:
    key,val= line.split("\t")
    val = int (val)
    
    if key == curkey:
      if(val>total):
        to=val
        
    else:
      if curkey is not None:
        sys.stdout.write("{}\t{}\n"-format(curkey,to))
        
       corkey = key
       to = val
        
  sys.stdout.write("{}\t{}\n".format(curkey,to))
