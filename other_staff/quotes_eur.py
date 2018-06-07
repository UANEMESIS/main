import requests
import json

a = requests.get("http://www.cmegroup.com/CmeWS/mvc/Quotes/Future/58/G?pageSize=500&_=1526404120619")

text = a.text

obj = json.loads(text)
#print(obj)
#print(obj["expirationMonth"])

#for i in obj.values():
	#print(i)

print(obj["quotes"][0]["last"])

#{"quoteDelayed":true,"quoteDelay":"10 minutes","tradeDate":"15 May 2018","quotes":
#[{"last":"1.18885","change":"-0.0083","priorSettle":"1.19715","open":"1.1957","close":"-","high":"1.1966","low":"1.1848","highLimit":"1.23715","lowLimit":"1.15715","volume":"291,758","mdKey":"6EM8-XCME-G","quoteCode":"6EM8","escapedQuoteCode":"6EM8","code":"ECM8","updated":"12:06:37 CT<br /> 15 May 2018","expirationMonth":"JUN 2018","expirationCode":"M8","expirationDate":"20180601","productName":"Euro FX Futures","productCode":"6E","uri":"/trading/fx/g10/euro-fx.html","productId":58,"exchangeCode":"XCME","optionUri":"-","hasOption":false,"priceChart":
#{"enabled":true,"code":"6E","monthYear":"M8","venue":0,"title":"JUN_2018_Euro_FX_","year":2018},"netChangeStatus":"statusAlert","highLowLimits":"1.23715 / 1.15715"},
#{"last":"1.1928","change":"-0.0071","priorSettle":"1.1999","open":"1.19875","close":"-","high":"1.19915","low":"1.18785","highLimit":"1.2399","lowLimit":"1.1599","volume":"1,631","mdKey":"6EN8-XCME-G","quoteCode":"6EN8","escapedQuoteCode":"6EN8","code":"ECN8","updated":"11:43:11 CT<br /> 15 May 2018","expirationMonth":"JUL 2018","expirationCode":"N8","expirationDate":"20180701","productName":"Euro FX Futures","productCode":"6E","uri":"/trading/fx/g10/euro-fx.html","productId":58,"exchangeCode":"XCME","optionUri":"-","hasOption":false,"priceChart":
#{"enabled":true,"code":"6E","monthYear":"N8","venue":0,"title":"JUL_2018_Euro_FX_","year":2018},"netChangeStatus":"statusAlert","highLowLimits":"1.2399 / 1.1599"}