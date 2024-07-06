from django.db import models

class Apply(models.Model):
    app_name=models.TextField(max_length=200)
    app_contant=models.TextField(max_length=200)
    app_image=models.ImageField(upload_to='images/', blank=True)
    app_date=models.TextField(max_length=200)
    def __str__(self):
        return self.app_name

class Contact(models.Model):
    name=models.TextField(max_length=200)
    email=models.CharField(max_length=200)
    subject=models.TextField(max_length=200)
    message=models.TextField(max_length=200) 
    def __str__(self):
        return self.name
class Comment(models.Model):
    co_name=models.TextField(max_length=200)
    co_email=models.CharField(max_length=200)
    co_message=models.TextField(max_length=200)
    def __str__(self):
        return self.co_name



