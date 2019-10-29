from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "pollApp admin"
admin.site.site_title = "pollApp admin area"
admin.site.site_index = "welcome pollApp admin"
# Register your models here.
#with this we can manage these models in the admin section
#admin.site.register(Question)
#admin.site.register(Choice)
#the choices let you select one quesion, we dont want that scheme
#in the admin panel
#we use a tabular inline for that
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{"fields":['question_text']}),
    ('Date_information',{"fields":['pub_data'],'classes':["collapse"]}),]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
