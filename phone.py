import fnmatch
import os
import csv
import re

def main(rootPath, fileExtension, numberRegex):
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, fileExtension):
            fname = os.path.join(root, filename)
            file = open(fname, 'rU')
            next(file)
            try:
                reader = csv.reader(file)
                for row in reader:
                    if re.search(numberRegex, row[0]):
                        print row[0]
            finally:
                file.close()

if __name__ == '__main__':
    rootPath = '.'
    fileExtension = '*.csv'
    numberRegex = r"[789]\d{9}"
    main(rootPath, fileExtension, numberRegex)
