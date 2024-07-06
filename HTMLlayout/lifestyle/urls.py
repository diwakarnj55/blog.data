from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name="home"),
    path("post/<int:id>",views.post,name="post"),
    path("contact",views.contact,name="contact"),
    path("create",views.create,name="create"),
    path("about",views.about,name="about"),
    path("signup",views.signup,name="signup"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("update/<int:id>/", views.update, name="update"),
]