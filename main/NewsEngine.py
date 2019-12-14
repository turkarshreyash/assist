from newsapi import NewsApiClient
from . import TextPreProcessor


newsapi = NewsApiClient(api_key='c9057c453e2446f5a4712ee31fd63ede')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def GetNews(result):


    if "country_code" in result and "category" in result:
        articles  = newsapi.get_top_headlines(q=" ".join(result["query"]),country = result["country_code"],category=result["category"])['articles']
    elif "country_code" in result:
        articles  = newsapi.get_top_headlines(q=" ".join(result["query"]),country = result["country_code"])['articles']

    elif "category" in result:
        articles  = newsapi.get_top_headlines(q=" ".join(result["query"]),category=result["category"])['articles']
    else:
        articles  = newsapi.get_top_headlines(q=" ".join(result["query"]))['articles']

    if articles == []:
        articles  = newsapi.get_everything(q=" ".join(result["query"]))['articles']
        
    return (articles)



    
