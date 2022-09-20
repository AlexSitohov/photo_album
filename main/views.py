from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from main.forms import UserRegistrationForm, LoginForm, CreateCategoryForm, UploadPhotoForm
from main.models import *


def main_view(request):
    user = request.user
    categories = Category.objects.filter(category_author=user.id)

    context = {'categories': categories}
    return render(request, 'main/main.html', context)


def category_view(request, category_id):
    user = request.user
    category = get_object_or_404(Category, id=category_id)
    if category.category_author == user:
        photos = Photo.objects.filter(category=category)
        context = {'photos': photos, 'category': category}
        return render(request, 'main/category.html', context)


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')

    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'main/registration.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')

    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'main/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('main')


def create_category_view(request):
    if request.method == 'POST':
        data = request.POST

        category = Category.objects.create(category_author=request.user, name=data.get('name'))
        category.save()
        return redirect('main')
    else:
        form = CreateCategoryForm()
        context = {'form': form}
        return render(request, 'main/create_category.html', context)


# @login_required(login_url='login')
def upload_photo_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if category.category_author == request.user:
        if request.method == 'POST':
            form = UploadPhotoForm(request.POST, request.FILES)
            if form.is_valid():
                photo = Photo.objects.create(
                    category=category,
                    photo_description=form.cleaned_data['photo_description'],
                    photo=form.cleaned_data['photo']
                )
                photo.save()
                # form.save()
            return redirect('category', category.pk)
        else:
            form = UploadPhotoForm()
            context = {'form': form, 'category': category}
            return render(request, 'main/upload_photo.html', context)
    else:
        return HttpResponse('Нет доступа')


def update_category_view(request, id):
    try:
        category = Category.objects.get(id=id)
        user = request.user
        if category.category_author == user:
            if request.method == 'POST':
                category.name = request.POST.get('name')
                category.save()
                return redirect('main')
            else:
                context = {'category': category}
                return render(request, 'main/update_category.html', context)
        else:
            return HttpResponse('Нет доступа')
    except:
        pass


def delete_category_check_view(request, id):
    try:
        category = Category.objects.get(id=id)
        user = request.user
        if category.category_author == user:
            # category.delete()
            context = {'category': category}
            return render(request, 'main/delete_category.html', context)

        else:
            return HttpResponse('Нет доступа')
    except:
        pass


def delete_category_view(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        return redirect('main')
    except:
        pass


def update_photo_view(request, id, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
        photo = Photo.objects.get(id=id)
        user = request.user
        if request.method == 'POST':
            photo.photo_description = request.POST.get('photo_description')
            photo.save()
            print(photo.photo_description)
            return redirect('category', category.pk)
        else:
            form = UploadPhotoForm()
            context = {'form': form, 'photo': photo, 'category': category}
            return render(request, 'main/update_photo.html', context)

    except:
        pass


def delete_photo_view(request, id, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
        photo = Photo.objects.get(id=id)
        photo.delete()
        return redirect('category', category.pk)
    except:
        pass
