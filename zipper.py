
## This one works but for one file at a time only.

'''from zipfile import ZipFile

base = R"C:\\zips"

with ZipFile(base) as zObject:

	zObject.extractall(path="C:\\zips\\TESTING")'''

## This one doesn't Work.

'''from zipfile import ZipFile

with ZipFile("C:\\zips\\sample.zip", 'r') as zObject:

	for file in zObject.namelist():
		if file.endswith(".zip"):
			archive.extract(path="C:\\zips\\TESTING")'''

## This one works but is convoluted. There must be a simpler way...

'''import zipfile
import os
import glob

base = R"C:\\zips" #Replace portion inside quotations with full path to desired directory.

for arc_name in glob.iglob(os.path.join(base, "*.zip")):
    arc_dir_name = os.path.splitext(os.path.basename(arc_name))[0]
    zf = zipfile.ZipFile(arc_name)
    zf.extractall(path=os.path.join(base, "TESTING", arc_dir_name))
    zf.close()'''

## This one works and isn't too convoluted. I am satisfied.

from zipfile import ZipFile
import os

base = R"c:\\zips\\"  #Replace portion inside quotations with full path to desired directory.

list = os.listdir(base) 
for item in list:
	zObject = ZipFile(base + item)

	zObject.extractall(path="C:\\zips\\TESTING")