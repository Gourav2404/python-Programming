from doctest import testfile
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

url = input("Enter :")

uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)

lst = tree.findall('comments/comment/count')

counts = tree.findall('.//count')

num = 0
sum = 0
for each in counts:
    test = int(each.text)
    num = num + 1
    sum = sum + test
    print(each.text)

print(num)
print(sum)
