from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


class FormDB(models.Model):
    Choice_Language=(('Java/Kotlin/Swift','Java/Kotlin/Swift'),('C++/C#','C++/C#'),('HTML/CSS/BOOTSTRAP','HTML/CSS/BOOTSTRAP'),('PHP/JS','PHP/JS'),('Python/R','Python/R'))
    Choice_Course= (('Android Development','Android Development'),('Web Technologies','Web Technologies'),('Machine Learning/Artificial Intelligence','Machine Learning/Artificial Intelligence'),('Database Systems','Database Systems'),('OOP and Data Structures','OOP and Data Structures'),('Computer Networks','Computer Networks'),('Project Management','Project Management'))
    Choice_Certification=(('None','None'),('Mobile Application Development','Mobile Application Development'),('Web Development','Web Development'),('Web Designing','Web Designing'),('Unity','Unity'))
    Choice_Area=(('Android','Android'),('Web','Web'),('Machine Learning','Machine Learning'),('Designing','Designing'),('Development','Development'),('Management','Management'),('Teaching','Teaching'))
    Choice_Coding=(('Good','Good'),('Average','Average'),('Poor','Poor'))
    Choice_Communication=(('Good','Good'),('Average','Average'),('Poor','Poor'))
    Choice_Mangerial=(('Good','Good'),('Average','Average'),('Poor','Poor'))
    Choice_Self=(('Good','Good'),('Average','Average'),('Poor','Poor'))
    Choice_Reading=(('Good','Good'),('Average','Average'),('Poor','Poor'))
    Choice_Work=(('Team','Team'),('Individual','Individual'))
    Choice_Solution=(('Yes','Yes'),('No','No'))
    Best_Course=models.CharField(max_length=50,choices=Choice_Course)
    Best_Language=models.CharField(max_length=50,choices=Choice_Language)
    Certification=models.CharField(max_length=50,choices=Choice_Certification)
    Interested_Area=models.CharField(max_length=50,choices=Choice_Area)
    Coding_Skills=models.CharField(max_length=50,choices=Choice_Coding)
    Communication_Skills=models.CharField(max_length=50,choices=Choice_Communication)
    Mangerial_Skills=models.CharField(max_length=50,choices=Choice_Mangerial)
    Self_Learning=models.CharField(max_length=50,choices=Choice_Self)
    Reading_Writing_Skills=models.CharField(max_length=50,choices=Choice_Reading)
    Working_Strategy=models.CharField(max_length=50,choices=Choice_Work)
    Solution_Provider=models.CharField(max_length=50,choices=Choice_Solution)
    Suggestion=models.CharField(default="None",max_length=100)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=1)



    def __str__(self):
        template='{0.id} {0.Best_Course} {0.Best_Language} {0.Certification} {0.Interested_Area} {0.Coding_Skills} {0.Communication_Skills} {0.Mangerial_Skills} {0.Self_Learning} {0.Reading_Writing_Skills} {0.Working_Strategy} {0.Solution_Provider}'
        return template.format(self)




class FormDBAdmin(admin.ModelAdmin):
    list_display = ('Best_Course', 'Best_Language', 'Certification', 'Interested_Area','Coding_Skills','Communication_Skills','Mangerial_Skills','Self_Learning','Reading_Writing_Skills','Working_Strategy','Solution_Provider')