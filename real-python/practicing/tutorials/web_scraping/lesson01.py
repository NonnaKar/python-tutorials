import time
import mechanicalsoup
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# * Extract Text From HTML With String Methods
# Example 1
our_url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(our_url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
title_index = html.find("<title>")
print(title_index)
start_index = title_index + len("<title>")
print(start_index)
end_index = html.find("</title>")
print(end_index)
title = html[start_index:end_index]
print(title)

# * A Primer on Regular Expressions
# Example 2
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(match_results.group())

# Example 3
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)

# * Extract Text From HTML With Regular Expressions
# Example 4
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)  # Remove HTML tags
print(title)

# * Use an HTML Parser for Web Scraping in Python
# Example 5
# todo: $ python3 -m pip install beautifulsoup4
# todo: $ python3 -m pip show beautifulsoup4

base_url = "http://olympus.realpython.org"
html_page = urlopen(base_url + "/profiles")
html_text = html_page.read().decode("utf-8")
soup = BeautifulSoup(html_text, "html.parser")
for link in soup.find_all("a"):
    link_url = base_url + link["href"]
    print(link_url)

# * Submit a Form With MechanicalSoup
# Example 6
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)
print(profiles_page.url)
links = profiles_page.soup.select("a")
for link in links:
    address = link["href"]
    text = link.text
    print(f"{text}:{address}")

# Example 7
browser = mechanicalsoup.Browser()
login_url = "http://olympus.realpython.org/login"
login_page = browser.get(login_url)
login_html = login_page.soup

form = login_html.form
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"
profiles_page = browser.submit(form, login_page.url)
print(profiles_page.soup.title)

# * Interact With Websites in Real Time
# Example 1
browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text
print(f"The result of your dice roll is: {result}")

# Example 2
browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    # Wait 10 seconds if this isn't the last request
    if i < 3:
        time.sleep(5)
