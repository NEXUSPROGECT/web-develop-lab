from django.contrib import admin
from .models import Movie, Customer

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    title = ['release_year', 'length', 'title']
    search_fields = ['title', 'length', 'release_year']
    list_fields = ['release_year']
    list_display = ['title', 'release_year']

class CustomerAdmin(admin.ModelAdmin):
    list_editable = ['phone']
    search_fields = ['first_name', 'last_name', 'phone']
    list_filter = ['last_name']
    list_display = ['first_name', 'last_name', 'phone']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Customer, CustomerAdmin)