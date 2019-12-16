from newsapi import NewsApiClient
from . import TextPreProcessor
from . import WeatherData
import concurrent.futures


newsapi = NewsApiClient(api_key='c9057c453e2446f5a4712ee31fd63ede')

def GetNewsByLocation(location):
    articles  = newsapi.get_top_headlines(country = location["country_code"])['articles']
    return (None,articles)

def GetNews(search):
    query = TextPreProcessor.QueryProcessor(search)
    articles = []
    executor = concurrent.futures.ThreadPoolExecutor()
    everything_flag = True
    topheadline_flag = True

    if query["q"] and query["language_code"]:
        everything = executor.submit(newsapi.get_everything,q=query["q"],language=query["language_code"])
    elif query["language_code"]:
        everything =  executor.submit(newsapi.get_everything,language=query["language_code"])
    elif query["q"]:
        everything = executor.submit(newsapi.get_everything,q=query["q"])
    else:
        everything_flag = False

        
    if query["country_code"] and query["category"] and query["q"]:
        topheadline = executor.submit(newsapi.get_top_headlines,q=query["q"],country=query["country_code"],category=query["category"])
    elif query["category"] and query["q"]:
        topheadline = executor.submit(newsapi.get_top_headlines,q=query["q"],category=query["category"])
    elif query["country_code"] and query["q"]:
        topheadline = executor.submit(newsapi.get_top_headlines,q=query["q"],country=query["country_code"])
    elif query["country_code"]:
        topheadline = executor.submit(newsapi.get_top_headlines,country=query["country_code"])
    elif query["category"]:
        topheadline = executor.submit(newsapi.get_top_headlines,category=query["category"])
    else:
        topheadline_flag = False

    if topheadline_flag:
        articles = topheadline.result()["articles"]
    else:
        articles = []
    if everything_flag:
        articles += everything.result()["articles"]

    return (query,articles)



    
