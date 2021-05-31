import hashlib
from os import listdir
from os.path import isdir, islink
for filename in listdir("."):
    if not isdir(filename) and not islink(filename):
        try:
            f = open(filename, "rb")
        except IOError as e:
            print(e)
        else:
            data = f.read()
            f.close()
            print("** %s **" % filename)
            for algorithm in hashlib.algorithms_guaranteed:
                h = hashlib.new(algorithm)
                h.update(data)
                try:
                    hexdigest = h.hexdigest()
                except TypeError:
                    hexdigest = h.hexdigest(128)
                print("%s: %s" % (algorithm, hexdigest))
            print()
 #Todo lo anterior genera el encriptado en los distintos algoritmos
#el a anexa la informacion
            file = open("Hash3.txt","a")
            file.write(str(("%s: '\n' %s" '\n' % (algorithm, hexdigest ))))
            file.close()
        
            
