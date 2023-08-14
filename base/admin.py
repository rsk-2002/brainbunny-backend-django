from django.contrib import admin
from .models import Message, Blog

# Register your models here.
admin.site.register(Message)
admin.site.register(Blog)