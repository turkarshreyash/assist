from nltk.corpus import stopwords 
from . import models
from . import NewsEngine
import threading
import concurrent.futures
from textblob import TextBlob

stop_words = set(stopwords.words('english'))


def wordFilter(word):
    new_word = ""
    for i in word:
        if i.isalnum() or i.isspace(): 
            new_word+=i
    return new_word


def GetQuotedText(search):
    search = search.split("'")
    quoted_search = ""
    simple_search = ""
    if len(search)%2:
        for i in search[1:-1]:
            if not i == "":
                quoted_search+=i
        if not search[0] == "":
            simple_search+=wordFilter(search[0])
        if len(search) != 1 and not search[-1] == "":
            simple_search+=wordFilter(search[-1])
    else:
        flag = False
        for i in search:
            if flag and not i == "":
                quoted_search+=i
            elif not i == "" :
                simple_search+=wordFilter(i)
            flag = not flag
    simple_search =  simple_search.split()
    quoted_search = quoted_search.split()
    return (quoted_search,simple_search)

def PreProcessor(simple_search):
    preprocesed = []
    for i in simple_search:
        if not i in stop_words:
            preprocesed.append(i)
    return preprocesed

def FilterPreProcesed(preprocesed):
    language = None
    language_code = None
    country = None
    country_code = None
    category = None
    q = []
    country_database = models.Countries.objects.all()
    category_database = models.Category.objects.all()
    language_database = models.Languages.objects.all()
    print("preprocessed : ",preprocesed)
    for i in preprocesed:
        print("I : ",i)
        if not country:
            try:
                temp = country_database.get(name__contains=i)
                country = temp.name
                country_code = temp.code
            except:
                if not category:
                    try:
                        category = category_database.get(name__contains=i).name
                    except:
                        q.append(i)
                else:
                    q.append(i)
        elif not category:
            try:
                category = category_database.get(name__contains=i).name
            except:
                q.append(i)
        else:
            q.append(i)
    print("Q : ",q)
    return q,language,language_code,country,country_code,category

def QueryProcessor(search):
    temp = models.Query()
    results = dict()
    results["searched"] = search
    print(f"Searched : {search}")
    corrected = str(TextBlob(search).correct())
    if corrected != search:
        results["corrected"] = corrected
    else:
        results["corrected"] = None
    print(f"Corrected Text : {results['corrected']}")
    q,temp = GetQuotedText(search)
    print("q: ",q," temp: ",temp)
    preprocessed_words = PreProcessor(temp)
    temp,language,language_code,country,country_code,category = FilterPreProcesed(preprocessed_words)
    q.extend(temp)
    results["q"] = " ".join(q)
    results["language"] = language
    results["country"] = country
    results["language_code"] = language_code
    results["country_code"] = country_code
    results["category"] = category
    return results