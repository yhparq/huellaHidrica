from django.contrib import admin

# Register your models here.

from .models import Question, ChooseAnswer

admin.site.register(Question)
admin.site.register(ChooseAnswer)