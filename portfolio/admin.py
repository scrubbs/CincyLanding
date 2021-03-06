from django.contrib import admin
from .models import PortfolioItem, Package

# Register your models here.
@admin.register(PortfolioItem)
class PortfolioAdmin(admin.ModelAdmin):
    fields = ('project_name',
              'project_url',
              'project_description',
              'picture',
              'url',
              'start_date',
              'github_link',
              'trello_link',
              'status',
              'packages'
              )
    search_fields = ['project_description']

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    fields = ('name',
              'docs_link',
              )
