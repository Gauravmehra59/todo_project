from django.shortcuts import render


def task_list(request):
    return render(request, "tasks/list.html")


def add_task(request):
    return render(request, "tasks/add_form.html")


def detail_task(request, id):
    return render(request, "tasks/edit_form.html")
