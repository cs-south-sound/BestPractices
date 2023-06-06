from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os       # access filesystem
from pathlib import Path # queasy path manipulation
import logging   # info, error, and warn messages

logging.basicConfig( level=logging.INFO )
logger = logging.getLogger(__name__)


# constants
NAME = 0    # first item in the sites list
URL=1       # second item in the sites list

# links to security best practices websites
ibm    = ["ibm","https://www.ibm.com/topics/cloud-security"]
google = ["google","https://cloud.google.com/security/best-practices"]
aws    = ["aws","https://aws.amazon.com/security/"]
#microsoft azure is a pdf.  see the ingest pdf file
cloud_list = [ibm,google,aws]
just_like_my_browser = {
    'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"
}

#

def ck_dir_exists(path_obj):
    return path_obj.exists()

#

def create_directory(path_obj):

    '''
    path_obj must contain the absolute path to the directory

    '''
    path_string = str( path_obj.resolve() )
    msg = "Creating directory: " + path_string
    logger.info( msg )
    mode = 0o755
    os.makedirs( path_string, mode)

    if path_obj.exists() == True:
        logger.info( "Creation completed" )

#

def save_in_wip(file_name, suffix, txt):
    relative_path_to_wip = "../wip"
    relative_path_to_file = "../wip/" + file_name + "."+ suffix
    absolute_parent_directory = str( Path(__file__).absolute().parent )
    wip_absolute_path_object = Path( os.path.join( absolute_parent_directory, \
                                               relative_path_to_wip ) )
    file_absolute_path_object = Path( os.path.join( absolute_parent_directory,\
                                               relative_path_to_file ) )

    # before writing check if the directory exists
    expected_directory_available = ck_dir_exists(wip_absolute_path_object)
    if not expected_directory_available:
        create_directory(wip_absolute_path_object)

    msg = "writing to str(file_absolute_path_object): " + \
           str(file_absolute_path_object)
    logger.info(msg)

    with open(str(file_absolute_path_object), 'w') as f:
        f.writelines(txt)

#

if __name__ == "__main__":
    # request all the remote html to local files
    # stored in a work-in-progress directory (wip)
    for site_list in cloud_list:
        if site_list != "":
            msg = "site_list[NAME]: " + site_list[NAME]
            logger.info(msg)
            msg = "site_list[URL]: " + site_list[URL]
            logger.info(msg)
            req = Request(site_list[URL], headers=just_like_my_browser)
            page = urlopen(req)
            soup = BeautifulSoup(page, features="html.parser")
            save_in_wip(site_list[NAME],"html", soup.prettify())
