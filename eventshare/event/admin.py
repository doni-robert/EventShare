from django.contrib import admin
from .models import Category, User, Event

admin.site.register([Category, User, Event])

# Register your models here.
