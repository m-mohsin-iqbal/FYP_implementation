from django import forms
from .models import FormDB
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class Career_Prediction(forms.ModelForm):
    # Best_Course = forms.ChoiceField( choices=[('Android Development','Android Development'),('Web Technologies','Web Technologies'),('Machine Learning/Artificial Intelligence','Machine Learning/Artificial Intelligence'),('Database Systems','Database Systems'),('OOP and Data Structures','OOP and Data Structures'),('Computer Networks','Computer Networks'),('Project Management','Project Management')])
    # Best_Language = forms.ChoiceField( choices=[('Java/Kotlin/Swift','Java/Kotlin/Swift'),('C++/C#','C++/C#'),('HTML/CSS/BOOTSTRAP','HTML/CSS/BOOTSTRAP'),('PHP/JS','PHP/JS'),('Python/R','Python/R')])
    # Certification= forms.ChoiceField( choices=[('None','None'),('Mobile Application Development','Mobile Application Development'),('Web Development','Web Development'),('Web Designing','Web Designing'),('Unity','Unity')])
    # Interested_Area= forms.ChoiceField(choices=[('Android','Android'),('Web','Web'),('Machine Learning','Machine Learning'),('Designing','Designing'),('Development','Development'),('Management','Management'),('Teaching','Teaching')])
    # Coding_Skills = forms.ChoiceField(choices=[('Good','Good'),('Average','Average'),('Poor','Poor')])
    # Communication_Skills = forms.ChoiceField(choices=[('Good','Good'),('Average','Average'),('Poor','Poor')])
    # Mangerial_Skills = forms.ChoiceField(choices=[('Good','Good'),('Average','Average'),('Poor','Poor')])
    # Self_Learning = forms.ChoiceField(choices=[('Good','Good'),('Average','Average'),('Poor','Poor')])
    # Reading_Writing_Skills = forms.ChoiceField(choices=[('Good','Good'),('Average','Average'),('Poor','Poor')])
    # Working_Strategy =forms.ChoiceField(choices=[('Team','Team'),('Individual','Individual')])
    # Solution_Provider = forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])

    class Meta:
        model=FormDB
        fields = '__all__'
        exclude=['Suggestion','user_id']



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'example@example.com'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username123'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
