#from django.contrib import
# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import Articles

admin.site.register(Articles)
