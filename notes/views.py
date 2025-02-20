from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import NoteForm
from .models import Note
# Create your views here.
def NotesView(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }

    return render(request, 'notes/notes.html', context)
def create_note(request):
    return render(request, 'notes/create-note.html', {})
@csrf_exempt  # Disable CSRF (or use CSRF token in request)
def save_note(request):
    if request.method == "POST":
        content = request.POST.get('content', '').strip()  # Get content from form
        title = request.POST.get('title', '').strip()
        if content and title:  # Make sure content is not empty
            Note.objects.create(content=content, title=title)  # Save the note
        return redirect('notes')  # Redirect to home page after saving
    #if request.method == "POST":
    #    data = json.loads(request.body)
    #    content = data.get("content", "")
    #    title = data.get("title", "")
    #    Note.objects.create(content=content, title=title)
    #    return JsonResponse({"redirect": "/"})
    return render(request, 'notes/create-note.html', {})