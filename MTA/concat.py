#concatenates multiple text files into one for easier parsing in main.py's df with glob
# method derived from https://stackoverflow.com/questions/17749058/combine-multiple-text-files-into-one-text-file-using-python

import glob

interesting_files = glob.glob("*.txt") 

header_saved = False

with open('output.csv','w') as fout:
    for filename in interesting_files:
        with open(filename) as fin:
            header = next(fin)
            if not header_saved:
                fout.write(header)
                header_saved = True
            for line in fin:
                fout.write(line)