from django.contrib import admin

# Register your models here.
from .models import Questions,Choice

# admin.site.register(Questions)
# admin.site.register(Choice)

# class QuestionAdmin(admin.ModelAdmin):
#     # fields = ['pub_date','question_text']
#     # fieldsets = [
#     #     (None, {'fields': ['question_text']}),
#     #     ('Date information', {'fields': ['pub_date']}),
#     # ]
#
#     fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]
#TODO 1 how to use list_display
    # list_display = ('question_text','pub_date','was_published_recently')

admin.site.register(Questions,QuestionAdmin)
admin.site.register(Choice)