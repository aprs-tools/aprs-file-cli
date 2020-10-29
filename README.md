# aprs-file-cli
This is a basic command line utility for the APRS File protocol. There are three python 2.7 scripts in the directory. To use them, first install the python requirements with “pip install -r requirements.txt”. You can then run the scripts with python.  If you cannot get the dependencies working, decoder_file.py should still work.

The first script, decoder_file.py is for decoding the file from a txt file with the raw APRS data. 

Usage: python decoder_file.py inputfile aprsfilename.

The second script, decoder_web.py will fetch the latest raw data from findu.com and can decode files this way.  

Usage: python decoder_file.py CALLSIGN. This will show the available files. To get a file, run python decoder_file.py CALLSIGN filename.

The third script, is for encoding the files. It will generate wav files in the directory that have the data in them. These wav files can then be transmitted over the radio. Please note that they have to be played in order for it to work correctly. Also, missing a packet will not allow the file to correctly decode. It does not matter if a packet is repeated twice, as the decoding code can handle this.

Usage: python encoder.py CALLSIGN filename.
