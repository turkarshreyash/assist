from textblob import TextBlob
from nltk.corpus import stopwords 

news_subcategory = [ "business", "entertainment", "health", "science", "sports", "technology"]
countries = {'argentina':'ar','australia':'au','austria':'at','aelgium':'be','arazil':'br','bulgaria':'bg','canada':'ca','china':'cn','colombia':'co','cuba':'cu','czech republic':'cz','egypt':'eg','france':'fr','germany':'de','greece':'gr','hong kong':'hk','hungary':'hu','india':'in','indonesia':'id','ireland':'ie','israel':'il','italy':'it','japan':'jp','latvia':'lv','lithuania':'lt','malaysia':'my','mexico':'mx','morocco':'ma','netherlands':'nl','new zealand':'nz','nigeria':'ng','norway':'no','philippines':'ph','poland':'pl','portugal':'pt','romania':'ro','russia':'ru','saudi arabia':'sa','serbia':'rs','singapore':'sg','slovakia':'sk','slovenia':'si','south africa':'za','south korea':'kr','sweden':'se','switzerland':'ch','taiwan':'tw','thailand':'th','turkey':'tr','uae':'ae','ukraine':'ua','united kingdom':'gb','united states':'us','venuzuela':'ve'}
countries_inverse = {'ar': 'argentina', 'au': 'australia', 'at': 'austria', 'be': 'aelgium', 'br': 'arazil', 'bg': 'bulgaria', 'ca': 'canada', 'cn': 'china', 'co': 'colombia', 'cu': 'cuba', 'cz': 'czech republic', 'eg': 'egypt', 'fr': 'france', 'de': 'germany', 'gr': 'greece', 'hk': 'hong kong', 'hu': 'hungary', 'in': 'india', 'id': 'indonesia', 'ie': 'ireland', 'il': 'israel', 'it': 'italy', 'jp': 'japan', 'lv': 'latvia', 'lt': 'lithuania', 'my': 'malaysia', 'mx': 'mexico', 'ma': 'morocco', 'nl': 'netherlands', 'nz': 'new zealand', 'ng': 'nigeria', 'no': 'norway', 'ph': 'philippines', 'pl': 'poland', 'pt': 'portugal', 'ro': 'romania', 'ru': 'russia', 'sa': 'saudi arabia', 'rs': 'serbia', 'sg': 'singapore', 'sk': 'slovakia', 'si': 'slovenia', 'za': 'south africa', 'kr': 'south korea', 'se': 'sweden', 'ch': 'switzerland', 'tw': 'taiwan', 'th': 'thailand', 'tr': 'turkey', 'ae': 'uae', 'ua': 'ukraine', 'gb': 'united kingdom', 'us': 'united states', 've': 'venuzuela'}

stop_words = set(stopwords.words('english'))

def preprocessing(query):
    results = dict()
    query = query.lower()
    query_split = query.split()
    new_query = []
    year = []
    for i in query_split:
        if not i in stop_words:
            temp = "".join([j for j in i if j.isalpha()])
            if not temp == "": 
                if temp in news_subcategory:
                    results["category"] = temp
                elif temp in countries:
                    results["country_code"] = countries[temp]
                    results["country"] = temp
                elif temp in countries_inverse:
                    results["country_code"] = temp
                    results["country"] = countries_inverse[temp]
                else:
                    new_query.append(temp)
            temp = "".join([j for j in i if j.isnumeric()])
            if not temp == "" and int(temp)<2999: 
                year.append(temp)
    results["query"] = new_query
    results["year"] = year
    return results