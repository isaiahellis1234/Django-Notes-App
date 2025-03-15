from django.shortcuts import render, redirect

from .models import Note

# Create your views here.
def frontpage(request):
    notes = Note.objects.all()  # Fetch all notes
    return render(request, 'notes/frontpage.html', {'notes': notes})


def create_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Note.objects.create(user=request.user, title=title)
        return redirect("frontpage")  # ✅ Redirect after creating

    return render(request, 'notes/create_note.html')  # ✅ Render the correct template
