import requests
from bs4 import BeautifulSoup
import re
import json
 
USER_ID = "300488588" # Идишка аккаунта
WIN_HERO_RATE = {} 


# Блок получения винрейта для каждого героя

def get_all_win_rates():
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
	hero_stats_only_percent = [per.split("%")[0] for per in hero_stats]

	# Заполняем WIN_HERO_RATE в виде key (герой) value (винрейт героя)
	for h, s in zip(top_30_heroes, hero_stats_only_percent):
		WIN_HERO_RATE[h] = s

#get_all_win_rates()
#print(WIN_HERO_RATE)

#------------------------------------------------------------------------

# Идишки матчей на челике, костыльна цифра '4' в строке с определением переменной html_match_result
MATCHES_ID = []
FINAL_ID_100_games = []

def append_100_last_matches():
	url_of_matches = f"https://ru.dotabuff.com/players/{USER_ID}/matches"

	rm = requests.get(url_of_matches, headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64)"})
	htmlm = rm.text

	soupm = BeautifulSoup(htmlm, 'html.parser')
	html_match_result = list(soupm.find_all("a", href=re.compile("/matches/4"))) # костыль!!!

	for numb in html_match_result:
		MATCHES_ID.append(str(numb))

	for links in MATCHES_ID:
		v = re.findall('\d+', links)
		FINAL_ID_100_games.extend(v)

#append_100_last_matches()
#print(FINAL_ID_100_games)

#------------------------------------------------------------------------

# с помощью api.opendota.com вытягиваем latest matches - их 20 штук, нам нужны идишки, которые мы запишем в LAST_20_MATCHES
LAST_20_MATCHES = []

def get_20_last_matches_ids():
	matches_url = f"https://api.opendota.com/api/players/{USER_ID}/recentMatches"

	rmm_match_id_request = requests.get(matches_url) #, headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64)"})

	rmm_20_ids_convert_json = json.loads(rmm_match_id_request.text)

	for ids in rmm_20_ids_convert_json:
		LAST_20_MATCHES.append(str(ids["match_id"]))

#get_20_last_matches_ids()
#print(LAST_20_MATCHES)

#------------------------------------------------------------------------

#Вытягиваем необходимую инфу по матчу 

def details_of_matches():
	matches_url_detailed = f"https://api.opendota.com/api/matches/4037097511"
	request_details_of_match = requests.get(matches_url_detailed)
	details_of_match_convert_json = json.loads(request_details_of_match.text)

	print(details_of_match_convert_json["radiant_win"])
	rhero_1 = details_of_match_convert_json["players"][0]["hero_id"]
	rhero_2 = details_of_match_convert_json["players"][1]["hero_id"]
	rhero_3 = details_of_match_convert_json["players"][2]["hero_id"]
	rhero_4 = details_of_match_convert_json["players"][3]["hero_id"]
	rhero_5 = details_of_match_convert_json["players"][4]["hero_id"]

	dhero_1 = details_of_match_convert_json["players"][5]["hero_id"]
	dhero_2 = details_of_match_convert_json["players"][6]["hero_id"]
	dhero_3 = details_of_match_convert_json["players"][7]["hero_id"]
	dhero_4 = details_of_match_convert_json["players"][8]["hero_id"]
	dhero_5 = details_of_match_convert_json["players"][9]["hero_id"]

	print(dhero_1, dhero_2, dhero_3, dhero_4, dhero_5)
	
	#f = open('1', 'w')
	#with open('1.txt', 'w') as f:
		#write_data = f.write(str(z))

details_of_matches()
RAW_HEROES_IDS = "https://raw.githubusercontent.com/kronusme/dota2-api/master/data/heroes.json"