from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth


def home(request):
    # list_workers = Worker.objects.all
    # content = {
    #     # 'title': 'Список рабочих',
    #     'workers': list_workers,
    #     'username': auth.get_user(request).username,
    # }
    return render(request, 'base.html', {})
