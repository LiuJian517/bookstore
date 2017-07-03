from django.contrib import admin

# Register your models here. 注册模型类

from . import models
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','content','gender','book']
admin.site.register(models.BookInfo,BookInfoAdmin)
admin.site.register(models.HeroInfo,HeroInfoAdmin)