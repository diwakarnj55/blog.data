from django.shortcuts import render, redirect
from . models import Apply, Comment
from . forms import ContactForm, ApplyForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def index(request):
    app=Apply.objects.all()
    data ={
        "app":app
    }
    return render(request,"index.html",data)
def post(request, id):
    app=Apply.objects.get(id=id)
    comm=Comment.objects.all()
    co=CommentForm()
    data ={
        "app":app,
        "co":co,
        "comm":comm,
    }
    if request.method=="POST":
        comment=CommentForm(request.POST,)
        if comment.is_valid():
            comment.save()
    return render(request,"post.html",data)
def contact(request):
    con=ContactForm()
    data1 ={
        "con":con,
    }
    if request.method=="POST":
        Contact=ContactForm(request.POST)
        if Contact.is_valid():
            Contact.save()
            return redirect("home")
    return render(request,"contact.html",data1)
@login_required
def create(request):
    form=ApplyForm()
    data2 ={
        "form":form,
    }
    if request.method=="POST":
        apply=ApplyForm(request.POST, request.FILES)
        if apply.is_valid():
            apply.save()
            return redirect("home")
    return render(request,"create.html",data2)
def about(request):
    return render(request,"about.html")
def signup(request):
    form=UserCreationForm()
    contex={
        "form":form
    }
    if request.method=='POST':
        data=UserCreationForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect("home")
    return render(request,"signup.html",contex) 
def delete(request,id):
    app=Apply.objects.get(id=id)
    if request.method=='POST':
        app.delete()
        return redirect("home")
def update(request,id):
    app=Apply.objects.get(id=id)
    form=ApplyForm(instance=app)
    data2 ={
        "app":app,
        "form":form,
    }
    if request.method=="POST":
        apply=ApplyForm(request.POST, request.FILES, instance=app)
        if apply.is_valid():
            apply.save()
            return redirect("home")
    return render(request,"update.html",data2)

   

