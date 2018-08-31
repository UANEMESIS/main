import requests
from bs4 import BeautifulSoup
import re
import json
#from colorama import init
#from colorama import Fore, Back, Style

#init()
USER_ID = "300488588" #"105248644" #"125138801" # Идишка аккаунта # 125138801
WIN_HERO_RATE = {} 
MEDIANA_LIST_RESULT = []

# Блок получения винрейта для каждого героя

def get_all_win_rates():
	url = "https://ru.dotabuff.com/heroes/winning"

	r = requests.get(url, headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64)"})
	html = r.text

	soup = BeautifulSoup(html, 'html.parser')

	text_filter_1 = soup.get_text().split("УСП")[1]
	text_filter_2 = text_filter_1.split("Обновлено")[0].replace(" ", "")
	text_filter_2_2 = text_filter_2.replace("Anti-Mage", "AntiMage")
	text_filter_2_3 = text_filter_2_2.replace("Nature'sProphet", "NaturesProphet")
	text_filter_3 = re.findall("[a-zA-Z]+", text_filter_2_3)
	top_30_heroes = text_filter_3[0:119]


	hero_stats = re.split("[a-zA-Z]+", text_filter_2_3)[1:119]
	hero_stats_only_percent = [per.split("%")[0] for per in hero_stats]

	# Заполняем WIN_HERO_RATE в виде key (герой) value (винрейт героя)
	for h, s in zip(top_30_heroes, hero_stats_only_percent):
		WIN_HERO_RATE[h] = float(s)

get_all_win_rates()
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

get_20_last_matches_ids()
#print(LAST_20_MATCHES)

#------------------------------------------------------------------------

# вытянуть id героев

def get_hero_ids():
	RAW_HEROES_IDS = "https://raw.githubusercontent.com/UANEMESIS/main/master/dota_2/heroes.json"

	raw_get_heroes_ids = requests.get(RAW_HEROES_IDS)
	raw_get_heroes_conver_json = json.loads(raw_get_heroes_ids.text)

	# Replace keys and values
	list_of_keys = [itm for itm in raw_get_heroes_conver_json.keys()]
	list_of_values = [vl for vl in raw_get_heroes_conver_json.values()]
	FINAL_HERO_IDS = {v:k for v,k in zip(list_of_values, list_of_keys)}
	return FINAL_HERO_IDS

HERO_IDS = get_hero_ids()



#print(HERO_IDS)

#------------------------------------------------------------------------
#Вытягиваем необходимую инфу по матчу 

def details_of_matches(m_id):
	MEDIANA_FOR_MATCH = None
	WINNER = None
	RESULT = None
	OFFSET = None
	matches_url_detailed = f"https://api.opendota.com/api/matches/{m_id}"
	request_details_of_match = requests.get(matches_url_detailed)
	details_of_match_convert_json = json.loads(request_details_of_match.text)

	win_result = details_of_match_convert_json["radiant_win"]
	if win_result == True:
		WINNER = "Radiant"
	else:
		WINNER = "Dire"

	rhero_1 = WIN_HERO_RATE[HERO_IDS[details_of_match_convert_json["players"][0]["hero_id"]]]
	rhero_2 = WIN_HERO_RATE[HERO_IDS[details_of_match_convert_json["players"][1]["hero_id"]]]
	rhero_3 = WIN_HERO_RATE[HERO_IDS[details_of_match_convert_json["players"][2]["hero_id"]]]
	rhero_4 = WIN_HERO_RATE[HERO_IDS[details_of_match_convert_json["players"][3]["hero_id"]]]
	rhero_5 = WIN_HERO_RATE[HERO_IDS[details_of_match_convert_json["players"][4]["hero_id"]]]

	dhero_1 = WIN_HERO_RATE[HERO_IDS[details_of_match_convert_json["players"][5]["hero_id"]]]
	dhero_2 = WIN_HERO_RATE[HERO_IDS[details_of_match_convert_json["players"][6]["hero_id"]]]
	dhero_3 = WIN_HERO_RATE[HERO_IDS[details_of_match_convert_json["players"][7]["hero_id"]]]
	dhero_4 = WIN_HERO_RATE[HERO_IDS[details_of_match_convert_json["players"][8]["hero_id"]]]
	dhero_5 = WIN_HERO_RATE[HERO_IDS[details_of_match_convert_json["players"][9]["hero_id"]]]

	
	radiant_mediana = round((rhero_1 + rhero_2 + rhero_3 + rhero_4 + rhero_5)/5, 3)
	dire_mediana = round((dhero_1 + dhero_2 + dhero_3 + dhero_4 + dhero_5)/5, 3)
	
	if radiant_mediana > dire_mediana and WINNER == "Radiant":
		MEDIANA_FOR_MATCH = "Success!"
		RESULT = f"Winner: {WINNER} %(Radiant|Dire): {radiant_mediana} | {dire_mediana} Mediana: {MEDIANA_FOR_MATCH}"
	elif radiant_mediana > dire_mediana and WINNER == "Dire":
		OFFSET = round(radiant_mediana - dire_mediana, 3)
		MEDIANA_FOR_MATCH = "Failed!"
		RESULT = f"Winner: {WINNER} %(Radiant|Dire): {radiant_mediana} | {dire_mediana} Mediana: {MEDIANA_FOR_MATCH} OFFSET: {OFFSET}"
	elif radiant_mediana < dire_mediana and WINNER == "Radiant":
		OFFSET = round(dire_mediana - radiant_mediana, 3)
		MEDIANA_FOR_MATCH = "Failed!"
		RESULT = f"Winner: {WINNER} %(Radiant|Dire): {radiant_mediana} | {dire_mediana} Mediana: {MEDIANA_FOR_MATCH} OFFSET: {OFFSET}"
	elif radiant_mediana < dire_mediana and WINNER == "Dire":
		MEDIANA_FOR_MATCH = "Success!"
		RESULT = f"Winner: {WINNER} %(Radiant|Dire): {radiant_mediana} | {dire_mediana} Mediana: {MEDIANA_FOR_MATCH}"
	else:
		RESULT = "UNKNOWN ERROR!!!"
	print(RESULT) # Опционально
	MEDIANA_LIST_RESULT.append(RESULT)




counter = 0

while counter < len(LAST_20_MATCHES):
	for i in LAST_20_MATCHES:
		details_of_matches(i)
		counter +=1


