from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['category']}),
        (None, {'fields': ['url']})
    ]

    list_display = ('title', 'category', 'url')

    #fields = ['title', 'category', 'url']

admin.site.register(Category)
admin.site.register(Page, PageAdmin)

# Register your models here.
