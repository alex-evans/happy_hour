from django.shortcuts import render
from journal.models import Entry


def journal_view(request):
    entries = Entry.objects.all()
    journal_entries = []
    for entry in entries:
        journal_entries.append({
            'id': entry.id,
            'date': entry.created_date
        })
    context = {
        'entries': journal_entries
    }
    return render(request, 'journal/journal_view.html', context)


def entry_view(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    context = {'text': entry.text}
    return render(request, 'journal/entry_view.html', context)
