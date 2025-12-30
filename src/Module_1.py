# BeautifulSoup4 Fundamentals

from bs4 import BeautifulSoup

# Sample HTML
html_doc = """
<html>
<head><title>Sample Page</title></head>
<body>
    <h1 class="main-title">Welcome</h1>
    <div class="content">
        <p id="intro">This is a paragraph.</p>
        <p id="intro">talal atef ahmed.</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')

# print("Title:", soup.title.string)
# print("H1:", soup.h1.string)

title = soup.find('h1', class_='main-title')
intro = soup.find(id='intro')

# print("Title:", title.string)
# print("Intro:", intro.string)

all_items = soup.find_all('li')
# for item in all_items:
#     print(item.string)

content_div = soup.select_one('div.content')
# print("Content Div:", content_div.prettify())
all_paragraphs = soup.select('p')
# for p in all_paragraphs:
#     print(p.string)

# Parent, siblings, children
h1 = soup.find('h1')
parent = h1.parent
# print(parent.string)

next_sibling = h1.find_next_sibling()
# print(next_sibling.string)

children = list(soup.body.children)
# for child in children:
#     print(child.string)

# print("\nAll Text Content:")
# for text in soup.stripped_strings:
#     print(text)

# print("\nAll Links:")
# for link in soup.find_all('a'):
#     print(link.get('href'))




