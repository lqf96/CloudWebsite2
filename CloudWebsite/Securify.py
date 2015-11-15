# Beautiful soup
from bs4 import BeautifulSoup
# Django settings
from django.conf import settings

# Rewrite elements and properties
REWRITE_TABLE = {
    "link": "href",
    "script": "src",
    "img": "src",
    "audio": "src",
    "video": "src"
}

# Rewrite resource addresses to make HTML secure and working
def Securify(raw_html):
    # Create BS4 document object
    html_soup = BeautifulSoup(raw_html,"html.parser")
    # Modify all elements
    for tag_name in REWRITE_TABLE:
        # Unify rewrite property as a list
        rewrite_prop = REWRITE_TABLE[tag_name]
        if (type(rewrite_prop).__name__=="str") or (type(rewrite_prop).__name__=="unicode"):
            rewrite_prop = [rewrite_prop,]
        # Recursively check all related elements
        for element in html_soup.find_all(tag_name):
            # Rewrite properties if necessary
            for prop in rewrite_prop:
                if (element.has_attr(prop)) and (element[prop][:7]=="http://"):
                    element[prop] = settings.ICP_ADDR+element[prop][7:]
    # Return modified HTML
    return unicode(html_soup)
