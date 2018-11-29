from googlesearch import search

from urllib.parse import unquote
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

# set some keys words
q_str = "العصر الجاهلي"

# foreach url in search list --> open and purify
for num, url in enumerate(search(q_str, lang="en", stop=3), start=1):
    # decode the url and open it content
    # url 	= unquote(url);
    # url 	= url.encode('cp1252').decode('cp1256')
    # url = unquote(url)
    text = ""
    try:
        # escape urls that give errors
        text = urlopen(url).read().decode('utf_8')
    except HTTPError:
        pass

    # filter the html components (script, style, meta, link, cdata)
    filtredPage = re.sub(r"<(script|style)(.|\n)*?>(.|\n)*?</\1>", '', text)
    filtredPage = re.sub(r"<(meta|link)(.|\n)*?/>", '', filtredPage)
    filtredPage = re.sub(r"<[!]\[CDATA\[(.|\n)*?>", '', filtredPage)

    # remove html tag and get only text
    result = BeautifulSoup(filtredPage, "lxml")

    # write the result into a file
    with open("file_ar_0" + str(num), "w", encoding="utf-8") as myfile:
        myfile.write(result.get_text().strip('\n'))