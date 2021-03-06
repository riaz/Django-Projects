from django.contrib import admin
from polls.models import Question,Choice

#since StackedInline takes lots of space , we can use TabularInline
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin): #This class is to update the default model to form modelling 
	#fields = ['pub_date','question_text']
	#Note: By default django displays the __str__ of each Question object, but this is also 
	#programmable using list_display
	#note: even returning functions may be used to display in the list
	
	list_display = ('question_text','pub_date','was_published_recently')
	list_filter = ['pub_date']

	search_fields = ['question_text']
	
	fieldsets = [
		(None , {'fields': [ 'question_text']}),
		('Date Information', { 'fields' : ['pub_date'] , 'classes': ['collapse'] })
	]
	inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)  -- since it was added inline


