from django.contrib import admin

# Register your models here.

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Question infor', {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)