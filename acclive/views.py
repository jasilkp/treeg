from django.shortcuts import render
from django.http import JsonResponse
from .models import TableEntry
from django.views.decorators.csrf import csrf_exempt
import json
from decimal import Decimal, InvalidOperation
from django.db import transaction, OperationalError
import time

MAX_RETRIES = 3
RETRY_DELAY = 0.1  # 100ms

def table_view(request):
    entries = TableEntry.objects.filter(deleted=False).order_by("date")
    return render(request, 'table.html', {'entries': entries})

@csrf_exempt
def save_entry(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

    retries = 0
    while retries < MAX_RETRIES:
        try:
            data = json.loads(request.body)
            entry_id = data.get("id")

            # Validate required fields
            required_fields = ["date", "site_name", "description"]
            missing_fields = [field for field in required_fields if not data.get(field)]
            if missing_fields:
                return JsonResponse({"error": f"Missing required fields: {', '.join(missing_fields)}"}, status=400)

            # Start a transaction to ensure data consistency
            with transaction.atomic():
                if entry_id:
                    try:
                        entry = TableEntry.objects.select_for_update().get(id=entry_id)
                    except TableEntry.DoesNotExist:
                        return JsonResponse({"error": f"Entry with id {entry_id} not found"}, status=404)
                else:
                    entry = TableEntry()

                entry.date = data.get("date")
                entry.site_name = data.get("site_name")
                entry.description = data.get("description")
                entry.bank = data.get("bank", False)
                
                try:
                    entry.income = Decimal(str(data.get("income") or 0))
                    entry.expense = Decimal(str(data.get("expense") or 0))
                    entry.amount = Decimal(str(data.get("amount") or 0))
                except (InvalidOperation, TypeError) as e:
                    return JsonResponse({"error": f"Invalid numeric value: {str(e)}"}, status=400)

                entry.transaction_type = data.get("transaction_type")
                
                # Handle check number based on transaction type
                check_number = data.get("check_number")
                if entry.bank and entry.transaction_type in ["Withdrawal", "Transfer"]:
                    # Convert None to empty string before stripping
                    check_number = str(check_number or "").strip()
                    entry.check_number = check_number if check_number else ""
                else:
                    entry.check_number = ""

                # Save the entry
                entry.save()

                return JsonResponse({
                    "id": entry.id,
                    "balance": float(entry.balance),
                    "amount_balance": float(entry.amount_balance),
                    "check_number": entry.check_number
                }, status=200)

        except OperationalError as e:
            if "database is locked" in str(e):
                retries += 1
                if retries < MAX_RETRIES:
                    time.sleep(RETRY_DELAY)
                    continue
            return JsonResponse({"error": "Database is temporarily locked, please try again"}, status=503)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Server error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Failed to save after multiple attempts"}, status=503)

@csrf_exempt
def delete_entry(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

    retries = 0
    while retries < MAX_RETRIES:
        try:
            data = json.loads(request.body)
            entry_id = data.get("id")

            if not entry_id:
                return JsonResponse({"error": "Entry ID is required"}, status=400)

            with transaction.atomic():
                try:
                    entry = TableEntry.objects.select_for_update().get(id=entry_id)
                    entry.deleted = True
                    entry.save()
                    return JsonResponse({"success": True})
                except TableEntry.DoesNotExist:
                    return JsonResponse({"error": f"Entry with id {entry_id} not found"}, status=404)

        except OperationalError as e:
            if "database is locked" in str(e):
                retries += 1
                if retries < MAX_RETRIES:
                    time.sleep(RETRY_DELAY)
                    continue
            return JsonResponse({"error": "Database is temporarily locked, please try again"}, status=503)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Server error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Failed to delete after multiple attempts"}, status=503)

