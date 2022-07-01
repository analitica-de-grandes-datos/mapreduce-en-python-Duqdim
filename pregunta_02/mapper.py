#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == __main__":
  for line in sys.stdin:
    vector= line.split('\n')[0]
    purpose= vector.split(',')[3]
    amount= vector.split (',')[4]
    sys.stdout.write("{}\t{}\n".format(purpose,amount))
