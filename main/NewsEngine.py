from newsapi import NewsApiClient
import nltk 
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer 

news_subcategory = [ "business", "entertainment", "health", "science", "sports", "technology"]
countries = {'argentina':'ar','australia':'au','austria':'at','aelgium':'be','arazil':'br','bulgaria':'bg','canada':'ca','china':'cn','colombia':'co','cuba':'cu','czech republic':'cz','egypt':'eg','france':'fr','germany':'de','greece':'gr','hong kong':'hk','hungary':'hu','india':'in','indonesia':'id','ireland':'ie','israel':'il','italy':'it','japan':'jp','latvia':'lv','lithuania':'lt','malaysia':'my','mexico':'mx','morocco':'ma','netherlands':'nl','new zealand':'nz','nigeria':'ng','norway':'no','philippines':'ph','poland':'pl','portugal':'pt','romania':'ro','russia':'ru','saudi arabia':'sa','serbia':'rs','singapore':'sg','slovakia':'sk','slovenia':'si','south africa':'za','south korea':'kr','sweden':'se','switzerland':'ch','taiwan':'tw','thailand':'th','turkey':'tr','uae':'ae','ukraine':'ua','united kingdom':'gb','united states':'us','venuzuela':'ve'}
ps = PorterStemmer() 
stop_words = set(stopwords.words('english'))

newsapi = NewsApiClient(api_key='c9057c453e2446f5a4712ee31fd63ede')



def GetNews(search):

    search = search.lower()
    eachword = search.split()
    country_code = None
    country = None
    category = None
    words = []
    for i in eachword:
        if i in countries:
            country_code = countries[i]
            country = i
        elif i in news_subcategory:
            category = i
        else:
            if i not in stop_words:
                words.append( ps.stem(i))
    print("WORDS : ",words)
    words = " ".join(words)
    if country and category:
        articles  = newsapi.get_top_headlines(q=words,country = country_code,category=category)['articles']
    elif country:
        articles  = newsapi.get_top_headlines(q=words,country = country_code)['articles']
    elif category:
        articles  = newsapi.get_top_headlines(q=words,category=category)['articles']
    else:
        articles  = newsapi.get_top_headlines(q=words)['articles']

    if articles == []:
        articles  = newsapi.get_everything(q=search)['articles']
        
    return (articles,country,category,words)



    
