from django.contrib import admin
from news.models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display =('title',"news_desc")

admin.site.register(News,NewsAdmin)
