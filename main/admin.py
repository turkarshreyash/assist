from django.contrib import admin
from . models import Query, Category, Languages, Countries, PropertiesOfSearch, LanguagesCountry




admin.site.register(Query)
admin.site.register(Category)
admin.site.register(Languages)
admin.site.register(Countries)
admin.site.register(PropertiesOfSearch)
admin.site.register(LanguagesCountry)
