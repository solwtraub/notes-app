from django.urls import path
from . import views
urlpatterns = [
    path("", views.NotesView, name="notes"),
    path("save-note/", views.save_note, name="save_note"),
    path("create-note/", views.create_note, name="create_note")
]