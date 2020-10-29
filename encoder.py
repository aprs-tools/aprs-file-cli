import base64
import textwrap
from afsk2.ax25 import EncodeAPRS
import random
import string
import sys
try:
    callsign = sys.argv[1]
    filee = sys.argv[2]
    offset = 9 - len(callsign) 
    offer = ' '* offset
    csignmesagi = callsign + offer
    ID = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(3))
    with open(filee, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        #base64_message = base64_encoded_data.decode('utf-8')
        file72 = textwrap.fill(base64_encoded_data, 64)
        open(filee + ".base64", "w").write(file72)
        cyyc=1
        with open(filee + ".base64") as f:
                EncodeAPRS(callsign,':' + csignmesagi + ':' + 'APRSFile|' + filee + '|' + ID + '|' + 'BASE64 Encoded Data',filee + str(0) + '.wav')
                for line in f:
                    EncodeAPRS(callsign,':' + csignmesagi + ':' + ID + line,filee + str(cyyc) + '.wav')
                    cyyc = cyyc + 1
except IndexError:
    print("Usage: python encoder.py CALLSIGN filename.")
