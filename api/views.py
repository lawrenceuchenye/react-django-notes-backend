from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializer import NoteSerializer

from .models import Note
# Create your views here.

@api_view(["GET"])
def getRoutes(request):
  routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
  return Response(routes)


@api_view(["GET"])
def getNotes(request):
  notes=Note.objects.all()
  notesSerialized=NoteSerializer(notes,many=True)
  return Response(notesSerialized.data)


@api_view(["GET"])
def getNote(request,pk):
  note=Note.objects.get(id=pk)
  noteSerialized=NoteSerializer(note,many=False)
  return Response(noteSerialized.data)


@api_view(["POST"])
def addNote(request):
   data=request.data
   Note.objects.create(**data)
   return Response("Note Created")


@api_view(["PUT"])
def updateNote(request,pk):
  data=request.data
  note=Note.objects.get(id=pk)
  data=custom_clean_data(request.data,note)
  serializer=NoteSerializer(instance=note,data=data)
  if serializer.is_valid():
     serializer.save()
  return Response(serializer.data)


def custom_clean_data(data,obj):
  new_data={"title":obj.title,"body":obj.body}
  if data["title"] != "":
     new_data["title"]=data["title"]
  if data["body"] != "":
     new_data["body"]=data["body"]
  return new_data


@api_view(["DELETE"])
def deleteNote(request,pk):
   note=Note.objects.get(id=pk)
   note.delete()
   return Response("Note Deleted")
