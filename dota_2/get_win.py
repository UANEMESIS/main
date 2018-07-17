import requests
from bs4 import BeautifulSoup
import re

#soup = BeautifulSoup
url = "https://ru.dotabuff.com/heroes/winning"

r = requests.get(url, headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64)"})
html = r.text

soup = BeautifulSoup(html, 'html.parser')

text_filter_1 = soup.get_text().split("УСП")[1]
text_filter_2 = text_filter_1.split("Обновлено")[0].replace(" ", "")
text_filter_3 = re.findall("[a-zA-Z]+", text_filter_2)
top_30_heroes = text_filter_3[0:31]


hero_stats = re.split("[a-zA-Z]+", text_filter_2)[1:31]

print("-----------------------------")
print("Top 30 heroes, this month:")
for h, s in zip(top_30_heroes, hero_stats):
	print(h + " : " + s)
print("-----------------------------")


inf_user = "For what hero do you want to know counters?(Enter hero name!Note: if hero have 2 words in name, then write '-' between)"
user_ask = str(input(inf_user).lower())

counters_url = f"https://ru.dotabuff.com/heroes/{user_ask}/counters"

r_counters = requests.get(counters_url, headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64)"})
html_counters = r_counters.text

soup_2 = BeautifulSoup(html_counters, 'html.parser')

counters_filter_1 = soup_2.get_text().split("Сыграно матчей")[1]
counters_filter_2 = counters_filter_1.split("Обновлено")[0].replace(" ", "")
counters_filter_3 = re.findall("[a-zA-Z]+", counters_filter_2)
top_15_counter_heroes = counters_filter_3[0:31]

counter_hero_stats = re.split("[a-zA-Z]+", counters_filter_2)[1:31]

print("-----------------------------")
print(f"{user_ask} counters is:")
for hc, sc in zip(top_15_counter_heroes, counter_hero_stats):
	print(hc + " : " + sc)
print("-----------------------------")

#print(counters_filter_2)
	






