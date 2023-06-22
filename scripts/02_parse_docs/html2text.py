""" for each html file in the 'wip' directory 
    get all the body text and save as a text file
"""

import os # operating system access
from bs4 import BeautifulSoup # html manipulation
from pathlib import Path # queasy path manipulation

relative_path_to_wip = "../wip"
absolute_parent_directory = str( Path(__file__).absolute().parent )
wip_absolute_path_object = Path( os.path.join( absolute_parent_directory, \
                                               relative_path_to_wip ) )

for filename in os.listdir(wip_absolute_path_object):
    if filename.endswith('.html'):
        fname = os.path.join(wip_absolute_path_object, filename)
        with open(fname, 'r') as f:
            soup = BeautifulSoup(f.read(),'html.parser')

            basename, suffix = filename.split(".")
            print("saving as text file: ", basename)
            txt = soup.get_text()
            fname2 = os.path.join(wip_absolute_path_object, basename + ".txt")
            with open(fname2, 'w') as f2:
                f2.writelines(txt)
