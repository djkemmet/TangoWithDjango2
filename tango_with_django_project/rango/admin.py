from django.contrib import admin
from rango import models

class PageAdmin(admin.ModelAdmin):
    # Fields are the values you're able to change 
    # from the Admin console. so I could hide URLs from 
    # being edited by dropping it from the list of fields.
    fields = ['title', 'views',]

    # The list_display variable sets which attributes
    # of the model are going to be displayed in the list
    # of models displayed in the admin page for a given
    # model. 
    list_display = ['category','title', 'url']


class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = { 'slug':('name',)}

    fields = ['name', 'views', 'likes', 'slug']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'user']



# Register your models here.
admin.site.register(models.Page, PageAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.UserProfile, UserProfileAdmin)