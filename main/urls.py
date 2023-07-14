from django.urls import path
from .views import NotesList, NotesDetail

urlpatterns = [
    path('notes/', NotesList.as_view()),
    path('notes/<int:pk>/', NotesDetail.as_view())
]
