import urllib.request
import xml.dom.minidom


file = urllib.request.urlopen('https://www.reddit.com/.rss')
DOMTree = xml.dom.minidom.parse(file)
file.close()
print(type(DOMTree))

DOMTree

collection = DOMTree.documentElement
if collection.hasAttribute("xmlns"):
    print("category element namespace: %s"%collection.getAttribute("xmlns"))


entries = collection.getElementsByTagName('entry')
print(type(entries))
print(len(entries))


for entry in entries:
    authors = entry.getElementsByTagName("author")
    for author in authors:
        print("---author----")
        print(author.getElementsByTagName('name')[0].childNodes[0].data)
        print(author.getElementsByTagName('uri')[0].childNodes[0].data)
    print('id=',entry.getElementsByTagName('id')[0].childNodes[0].data)
    print('link=',entry.getElementsByTagName('link')[0].getAttribute('href'))