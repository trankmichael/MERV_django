from django.contrib import admin
from recommender.models import Task

class TaskAdmin(admin.ModelAdmin):
	# fields display on change list
	list_display = ['title','description']
	#fields to filter the change list with
	list_filter = ['published','created']
	# fields to search in change list
	search_fields = ['title', 'description', 'content']
	#enable the date drill down on change list
	date_heirarchy = 'created'
	#enable the save buttons on top on change form
	save_on_top = True
	#prepopulate the slug from the title 
	prepopulated_fields = {"slug":("title",)}

	



admin.site.register(Task, TaskAdmin)

# Register your models here.
