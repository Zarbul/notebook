from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .models import Notes
from django.utils import timezone
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def home(request):
    notes_list = Notes.objects.filter(user=request.user).order_by('-create_date')
    paginator = Paginator(notes_list, 3)

    page = request.GET.get('page')
    try:
        note = paginator.page(page)
    except PageNotAnInteger:
        note = paginator.page(1)
    except EmptyPage:
        note = paginator.get_page(paginator.num_pages)

    if request.method == "POST":
        form_add = NoteForm(request.POST)
        if form_add.is_valid():
            post = form_add.save(commit=False)
            post.create_date = timezone.now()
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form_add = NoteForm()

    content = {
        'form': form_add,
        # 'notes': notes_list,
        'notes': note,
        # 'pages': paginator.page(page),
        # 'pages': note,

    }
    return render(request, 'note/index.html', content)


def detail(request, id=None):
    instance = get_object_or_404(Notes, id=id)
    content = {
        'name': instance.name,
        'link': instance.link,
        'instance': instance,
        # 'text': instance.text,
        'username': auth.get_user(request).username,
    }
    return render(request, 'note/detail.html', content)


def edit(request, id=None):
    note = get_object_or_404(Notes, id=id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            link = form.save(commit=False)
            link.create_date = timezone.now()
            link.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note/edit.html', {'form': form})


def delete(request, id=None):
    note = get_object_or_404(Notes, id=id)
    note.delete()
    return redirect('home')

# def new(request, id=None):
#     if request.method == "POST":
#         form_add = NoteForm(request.POST)
#         if form_add.is_valid():
#             post = form_add.save(commit=False)
#             post.create_date = timezone.now()
#             post.save()
#             return redirect('home')
#     else:
#         form_add = NoteForm()
#
#     content = {
#         'form': form_add,
#         'pprint': pprint(form_add),
#     }
#     return render(request, 'note/new.html', content)
# #
#
