from nltk.corpus import stopwords 
from . import models

stop_words = set(stopwords.words('english'))

def wordFilter(word):
    new_word = ""
    for i in word:
        if i.isalnum() or i.isspace(): 
            new_word+=i
    return new_word


def GetQuotedText(search):
    search = search.split("'")
    quoted_search = []
    simple_search = []
    if len(search)%2:
        for i in search[1:-1]:
            if not i == "":
                quoted_search.append(i)
        if not search[0] == "":
            simple_search.append(wordFilter(search[0]))
        if not search[-1] == "":
            simple_search.append(wordFilter(search[-1]))
    else:
        flag = False
        for i in search:
            if flag and not i == "":
                quoted_search.append(i)
            elif not i == "" :
                simple_search.append(wordFilter(i))
            flag = not flag
    return (quoted_search,simple_search)

def PreProcessor(simple_search):
    words = simple_search.split(" ")
    preprocesed = []
    for i in words:
        if not i in stop_words:
            preprocesed.append(i)
    return preprocesed

def FilterPreProcesed(preprocesed):
    language = ""
    country = ""
    category = ""
    q = []
    

    return q,language,country,category

def QueryProcessor(search):
    results = dict()
    q,temp = GetQuotedText(search)
    preprocessed_words = PreProcessor(temp)
    temp, language, country, category = FilterPreProcesed(preprocessed_words)
    q.append(temp)
    results["q"] = q
    results["language"] = language
    results["country"] = country
    results["category"] = category
    return results