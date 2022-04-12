import requests
from bs4 import BeautifulSoup
import webbrowser

url = 'https://www.postimees.ee/rss'

xml_data = requests.get(url).content
soup = BeautifulSoup(xml_data, "xml")
# print(soup)

items = soup.find_all('channel')
for titles in items:
    allText = titles.text
print(allText)


f = open('index.html','w', encoding='utf-16')
message = '''
<html>
    <head>
        <title>POSTIMEES</title>
    </head>
    <body>
        <div>
'''
for item in items[:5]:
    title = item.find('title').text
    message += f"<h2>(title)</h2>"
    image_url = item.find('enclosure')['url']
    message += f"<h2>(image_url)</h2>"
    message += """
        </div>
    </body>
</html>
"""

f.write(message)
f.close()

webbrowser.open_new_tab('index.html')