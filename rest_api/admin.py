"""
Admin related stuff for example
registering models for accessing from admin panel
"""

from django.contrib import admin

from rest_api.models import (
    Article,
    Author,
)


admin.site.register(Article)
admin.site.register(Author)
