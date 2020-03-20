from django.shortcuts import render
from journal.models import Entry


def journal_view(request):
    entries = Entry.objects.all()

    context = {
        entries: entries
    }
    return render(request, 'journal/journal_view.html', context)
