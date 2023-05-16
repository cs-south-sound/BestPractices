from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# links to security best practices website
ibm    = "https://www.ibm.com/topics/cloud-security"
google = "https://cloud.google.com/security/best-practices"
aws    = ""
#microsoft azure is a pdf.  see the ingest pdf file
cloud_list = [ibm,google,aws]
just_like_my_browser = {
    'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"
}
for site in cloud_list:
    if site != "":
        print("site: ", site)
        req = Request(site,headers=just_like_my_browser)
        page = urlopen(req)
        soup = BeautifulSoup(page)
        print("----------------------------")
        print(soup)
        print("\n")

#def save_in_wip(from_url,txt):
#    with open('../wip/textfile.html', 'w') as f:
#    f.writelines(txt)