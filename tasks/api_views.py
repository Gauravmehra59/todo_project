import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .services.task_service import TaskService


def parse_json(request):
    """Safely parse JSON body from request."""
    try:
        return json.loads(request.body)
    except Exception:
        return None


def api_list(request):
    """
    GET /api/list/
    Returns all tasks in JSON format.
    """
    if request.method != "GET":
        return JsonResponse({"error": "GET required"}, status=405)

    rows = TaskService.all()

    tasks = [
        {
            "id": r[0],
            "title": r[1],
            "description": r[2],
            "due_date": r[3],
            "status": r[4],
        }
        for r in rows
    ]

    return JsonResponse({"tasks": tasks}, status=200)


def api_create(request):
    """
    POST /api/create/
    Creates a new task from JSON body.
    """
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    body = parse_json(request)
    if not body:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    if "title" not in body or "due_date" not in body:
        return JsonResponse({"error": "title and due_date are required"}, status=400)

    TaskService.create(
        body["title"],
        body.get("description", ""),
        body["due_date"],
        body.get("status", "pending")
    )

    return JsonResponse({"message": "Task created successfully"}, status=201)


@csrf_exempt
def api_delete(request, id):
    """
    DELETE /api/delete/<id>/
    Deletes the task with given ID.
    """
    if request.method != "DELETE":
        return JsonResponse({"error": "DELETE required"}, status=405)

    if not id:
        return JsonResponse({"error": "Record ID required"}, status=400)

    task = TaskService.get(id)
    if not task:
        return JsonResponse({"error": "Task not found"}, status=404)

    TaskService.delete(id)

    return JsonResponse({"message": "Task deleted successfully"}, status=200)


@csrf_exempt
def api_detail(request, id):
    """
    GET /api/detail/<id>/
    Returns details of a specific task.
    """
    if request.method != "GET":
        return JsonResponse({"error": "GET required"}, status=405)

    task = TaskService.get(id)

    if not task:
        return JsonResponse({"error": "Task not found"}, status=404)

    return JsonResponse({
        "id": task[0],
        "title": task[1],
        "description": task[2],
        "due_date": task[3],
        "status": task[4]
    }, status=200)


@csrf_exempt
def api_update(request, id):
    """
    PUT /api/update/<id>/
    Updates task details.
    """
    if request.method != "PUT":
        return JsonResponse({"error": "PUT required"}, status=405)

    body = parse_json(request)
    if not body:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    task = TaskService.get(id)
    if not task:
        return JsonResponse({"error": "Task not found"}, status=404)

    TaskService.update(
        id,
        body.get("title", task[1]),
        body.get("description", task[2]),
        body.get("due_date", task[3]),
        body.get("status", task[4]),
    )

    return JsonResponse({'message': "Task updated successfully"}, status=200)
