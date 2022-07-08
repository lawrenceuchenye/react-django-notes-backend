from django.urls import path
from . import views


urlpatterns=[
   path("",views.getRoutes,name="home"),
   path("notes/",views.getNotes,name="notes"),
   path("notes/<str:pk>/",views.getNote,name="note"),
   path("notes/addnote",views.addNote,name="addnote"),
   path("notes/<str:pk>/update/",views.updateNote,name="updatenote"),
   path("notes/<str:pk>/delete/",views.deleteNote,name="deletenote")
  ]
