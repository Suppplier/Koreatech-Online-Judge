from django.contrib import admin
from django import forms
from .models import Problem, Testcase, Submit, Article, Comment, Contest, ConParticipants, ConProblems
#from ckeditor.widgets import CKEditorWidget


class TestcaseAdmin(admin.StackedInline):
    model = Testcase


class ProblemAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [TestcaseAdmin]

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title']

class Con_Participants(admin.StackedInline):
    model = ConParticipants

class Con_Problems(admin.StackedInline):
    model = ConProblems

class ContestAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [Con_Participants, Con_Problems]
    #inlines = [Con_Problems]


class TestcaseAdmin(admin.ModelAdmin):
    pass
class Con_Participants(admin.StackedInline):
    pass
class Con_Problems(admin.StackedInline):
    pass

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Testcase, TestcaseAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(Submit)
admin.site.register(Comment)
