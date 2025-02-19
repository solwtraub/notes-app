from django.shortcuts import render

from .forms import NoteForm
# Create your views here.
def NotesView(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NoteForm()
    context = {
        'form' : form
    }

    return render(request, 'notes/notes.html', context)