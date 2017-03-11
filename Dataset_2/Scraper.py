import bs4 as bs
import urllib.request
import codecs

sauce = urllib.request.urlopen('http://www.presidency.ucsb.edu/ws/index.php?pid=119039').read()

soup = bs.BeautifulSoup(sauce,'lxml')

#Debate_Data --> string to append the text data.
Debate_Data =''

for p in soup.find_all("p"):
    
    Debate_Data += p.text
    
print(Debate_Data)

f = codecs.open('Debate_3.txt', 'w', encoding='utf8')
f.write(Debate_Data)

