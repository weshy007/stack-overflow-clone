from django.contrib import admin

from stackoverflow.models import Question, Comment

# Register your models here.
admin.site.register(Question)
admin.site.register(Comment)
