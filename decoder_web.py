import os.path
import sys
import base64
import urllib
from bs4 import BeautifulSoup
from collections import OrderedDict
def get_file(callsign):
    fid=urllib.urlopen('http://www.findu.com/cgi-bin/raw.cgi?call='+ callsign + "&start=336&length=336")
    webpage=fid.read()
    parse = BeautifulSoup(webpage,"html.parser" )
    data = parse.get_text()
    content=''.join('''{}\n{}\n\n{}\n{}''' for item in data)
    text_file = open("aprs_temp_data.txt", "w")
    text_file.write(data)
    text_file.close()
    try:
        if os.path.isfile(sys.argv[2]):
            print("Output file allready exists. Please move it out of the directory and run again.")
            return -1
    except IndexError:
        print("Available files:")
    content_array = []
    filenames = []
    sstring = ""
    with open("aprs_temp_data.txt") as f:
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
                   try:
                       sys.argv[2]
                       filenames.append(x[2])
                       if sys.argv[2] in x:
                           for line in content_array:
                              if  line.startswith(x[2]):
                                  text = line[3:]
                                  sstring = sstring + text
                           mystring = sstring.replace('\n', '').replace('\r', '')
                           text_file = open(sys.argv[2], "w")
                           text_file.write(base64.b64decode(mystring))
                           text_file.close()
                   except IndexError:
                       print(x[1])                   
try:
    get_file(sys.argv[1])
except IndexError:
    print("Usage: python decoder_file.py CALLSIGN. This will show the available files. To get a file, run python decoder_file.py CALLSIGN filename.")