from django import forms
from . models import Contact, Apply, Comment
from django . forms import Textarea,TextInput, FileInput, DateInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields =['name','email','subject','message']

        widgets ={
            'name':TextInput(attrs={
             "class":"form-control mr-0 ml-auto", 
             "name":"name", 
             "id":"name", 
             "type":"text",
            }),
            'email':TextInput(attrs={
             "class":"form-control mr-0 ml-auto", 
             "name":"email", 
             "id":"email", 
             "type":"email",
            }),
            'subject':TextInput(attrs={
             "class":"form-control mr-0 ml-auto", 
             "name":"subject",
             "id":"subject", 
             "type":"text",
            }),
            'message':Textarea(attrs={
             "class":"form-control mr-0 ml-auto", 
             "name":"message", 
             "id":"message", 
             "rows":"8",
            }),
        }
class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields =['app_name','app_contant','app_image','app_date',]
        widgets ={
            'app_name':TextInput(attrs={
                "class":"form-control", 
                "name":"name", 
                "type":"text",
            }),
            'app_contant':Textarea(attrs={
                "class":"form-control",
                "contact":"contact",
                "name":"content"
            }),
            'app_image':FileInput(attrs={
                 "class":"form-control",
                "image":"image",
                "type":"file",
            }),
            'app_date':DateInput(attrs={
                "class":"form-control",
                "type":"date",
            }),
        }
class LoginForm(AuthenticationForm):
    username = UsernameField(label='Enter Username', widget=forms.TextInput(attrs={"type":"text","class":"form-control","aria-describedby":"emailHelp","placeholder":"Enter Username"}))
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={"type":"password","class":"form-control","id":"exampleInputPassword1","placeholder":"Password"}))

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields =['co_name','co_email','co_message']
        widgets ={
            'co_name':TextInput(attrs={
                "class":"form-control", 
                "name":"name",  
                "type":"text",
            }),
            'co_email':TextInput(attrs={
                "class":"form-control", 
                "name":"email", 
                "type":"text",
            }),
            'co_message':Textarea(attrs={
                 "class":"form-control", 
                 "name":"message", 
                 "rows":"6",
            }),
        }
