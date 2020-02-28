from django.contrib import admin
from .models import  Profile,FormDB

@admin.register(FormDB)
class FormDBAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','Best_Course', 'Best_Language', 'Certification', 'Interested_Area','Coding_Skills','Communication_Skills','Mangerial_Skills','Self_Learning','Reading_Writing_Skills','Working_Strategy','Solution_Provider','Suggestion')

