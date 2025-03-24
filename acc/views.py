from django.shortcuts import render
from django.http import JsonResponse
from .models import TableEntry
from django.views.decorators.csrf import csrf_exempt
import json

def table_view(request):
    """Retrieve all table entries and display them in correct order."""
    entries = TableEntry.objects.order_by("date")  # Load entries by date
    return render(request, 'table.html', {'entries': entries})

@csrf_exempt
def save_entry(request):
    """Save or update an entry when edited in the frontend."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            entry_id = data.get('id')

            if entry_id:
                entry = TableEntry.objects.get(id=entry_id)
            else:
                entry = TableEntry()  # Create new entry if no ID

            entry.date = data.get('date')
            entry.site_name = data.get('site_name', '').strip()
            entry.description = data.get('description', '').strip()
            entry.income = float(data.get('income', 0) or 0)
            entry.expense = float(data.get('expense', 0) or 0)

            # Get the most recent entry before this date
            previous_entry = TableEntry.objects.filter(date__lt=entry.date).order_by('-date').first()
            previous_balance = previous_entry.balance if previous_entry else 0

            # Calculate balance
            entry.balance = previous_balance + entry.income - entry.expense
            entry.save()

            return JsonResponse({'id': entry.id, 'balance': float(entry.balance)})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)

