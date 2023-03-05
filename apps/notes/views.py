from django.shortcuts import render, redirect,  get_object_or_404
from .models import Note


def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/view_note.html', {'note': note})


def search_notes(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(title__icontains=query)
    else:
        notes = Note.objects.all()
    return render(request, 'notes/search_notes.html', {'notes': notes})


def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        note = Note.objects.create(title=title, content=content)
        return redirect('view_note', note.id)
    return render(request, 'notes/add_note.html')

