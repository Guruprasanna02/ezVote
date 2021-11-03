from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.site_header = "ezVote Admin"
admin.site.site_title = "ezVote Admin Area"
admin.site.index_title = "Welcome to the ezVote Admin Area"


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Timer', {
        'fields': ['when']}),]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
