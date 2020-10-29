import os.path
import sys
import base64
from collections import OrderedDict  
def get_file(fname,fname2):
    if os.path.isfile(fname2):
        print("Output file allready exists. Please move it out of the directory and run again.")
        return -1
    content_array = []
    filenames = []
    sstring = ""
    with open(fname) as f:
            for line in f:
                    h = line
                    indx = h.find(" :")
                    h = h[indx:]
                    h2 = h[2:]
                    content_array.append(h2)
            content_array = OrderedDict.fromkeys(content_array)
            for line in content_array:
               if  line.startswith('APRSFile'):
                   x = line.split("|")
                   filenames.append(x[2])
                   if fname2 in x:
                       for line in content_array:
                          if  line.startswith(x[2]):
                              text = line[3:]
                              sstring = sstring + text
                       mystring = sstring.replace('\n', '').replace('\r', '')
                       text_file = open(fname2, "w")
                       text_file.write(base64.b64decode(mystring))
                       text_file.close()    
try:
    get_file(sys.argv[1],sys.argv[2])
except IndexError:
    print("Usage: python decoder_file.py inputfile aprsfilename.")