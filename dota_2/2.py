import requests
from bs4 import BeautifulSoup
import re

USER_ID = "125138801"

#soup = BeautifulSoup
url = "https://ru.dotabuff.com/heroes/winning"

r = requests.get(url, headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64)"})
html = r.text

soup = BeautifulSoup(html, 'html.parser')

text_filter_1 = soup.get_text().split("УСП")[1]
text_filter_2 = text_filter_1.split("Обновлено")[0].replace(" ", "")
text_filter_2_2 = text_filter_2.replace("Anti-Mage", "AntiMage")
text_filter_3 = re.findall("[a-zA-Z]+", text_filter_2_2)
top_30_heroes = text_filter_3[0:118]


hero_stats = re.split("[a-zA-Z]+", text_filter_2_2)[1:118]
hero_stats = [per.split("%")[0] for per in hero_stats]


#print("-----------------------------")
#print("Top 30 heroes, this month:")
#for h, s in zip(top_30_heroes, hero_stats):
#	print(h + " : " + s)
#print("-----------------------------")


url_of_matches = f"https://ru.dotabuff.com/players/{USER_ID}/matches"

rm = requests.get(url_of_matches, headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64)"})

htmlm = rm.text
soupm = BeautifulSoup(htmlm, 'html.parser')

text_filter_m_1 = soupm.get_text()#.split("УСП")[1]

print(text_filter_m_1)