
news_subcategory = [ "business", "entertainment", "health", "science", "sports", "technology"]
countries = {'argentina':'ar','australia':'au','austria':'at','aelgium':'be','arazil':'br','bulgaria':'bg','canada':'ca','china':'cn','colombia':'co','cuba':'cu','czech republic':'cz','egypt':'eg','france':'fr','germany':'de','greece':'gr','hong kong':'hk','hungary':'hu','india':'in','indonesia':'id','ireland':'ie','israel':'il','italy':'it','japan':'jp','latvia':'lv','lithuania':'lt','malaysia':'my','mexico':'mx','morocco':'ma','netherlands':'nl','new zealand':'nz','nigeria':'ng','norway':'no','philippines':'ph','poland':'pl','portugal':'pt','romania':'ro','russia':'ru','saudi arabia':'sa','serbia':'rs','singapore':'sg','slovakia':'sk','slovenia':'si','south africa':'za','south korea':'kr','sweden':'se','switzerland':'ch','taiwan':'tw','thailand':'th','turkey':'tr','uae':'ae','ukraine':'ua','united kingdom':'gb','united states':'us','venuzuela':'ve'}

def GetNews(search):
    search = search.lower()
    eachword = search.split()
    country = None
    category = None
    words = ""
    for i in eachword:
        if i in countries:
            country = countries[i]
        elif i in news_subcategory:
            category = i
        else:
            words += i
    print(f"category {category}, country {country}, words {words}")

    return
    



    
if __name__ == "__main__":

    while True:
        search = input("Enter Text : ")
        GetNews(search)
