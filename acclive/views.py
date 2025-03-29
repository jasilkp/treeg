from django.shortcuts import render
from django.http import JsonResponse
from .models import TableEntry
from django.views.decorators.csrf import csrf_exempt
import json

def table_view(request):
    entries = TableEntry.objects.filter(deleted=False).order_by("date")
    return render(request, 'table.html', {'entries': entries})

@csrf_exempt
def save_entry(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            entry_id = data.get("id")

            if entry_id:
                entry = TableEntry.objects.get(id=entry_id)
            else:
                entry = TableEntry()

            entry.date = data.get("date")
            entry.site_name = data.get("site_name")
            entry.description = data.get("description")
            entry.bank = data.get("bank", False)
            entry.income = float(data.get("income") or 0)
            entry.expense = float(data.get("expense") or 0)
            entry.transaction_type = data.get("transaction_type")
            entry.amount = float(data.get("amount") or 0)
            entry.check_number = data.get("check_number")

            # Auto Calculate Balances
            entry.balance = entry.income - entry.expense
            entry.amount_balance = entry.amount

            entry.save()
            return JsonResponse({"id": entry.id, "balance": entry.balance, "amount_balance": entry.amount_balance}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def delete_entry(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            entry_id = data.get("id")

            if entry_id:
                entry = TableEntry.objects.get(id=entry_id)
                entry.deleted = True
                entry.save()
                return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)
