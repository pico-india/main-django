from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Image, Category
from django.contrib.auth.decorators import login_required
import random
import time
from django.contrib import messages
from django.core.files.images import get_image_dimensions
from django.http import HttpResponse
# Create your views here.


def index(request):
    images = list(Image.objects.all())
    random_images = random.sample(images, len(images))
    categories = Category.objects.all()

    return render(request, 'index.html', {'images': random_images, 'categories': categories})


def viewImage(request, pk):
    images = Image.objects.get(id=pk)
    images.views = images.views+1
    images.save()
    return render(request, 'view image.html', {'images': images})


def category(request, category):
    images = Image.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'category.html', {'images': images, 'categories': categories})


def search(request):
    picture = request.GET['picture']
    img = picture.split(' ')
    img = ''.join(img)
    images = Image.objects.filter(tags__icontains=img)
    categories = Category.objects.all()
    return render(request, 'search.html', {'images': images, 'picture': picture, 'categories': categories})


@login_required(login_url="/accounts/sign-in")
def upload(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.get('images')
        w, h = get_image_dimensions(images)
        
        if w >3000 or h> 3000:
            if data['category'] != None:
                category = Category.objects.get(id=data['category'])

                images = Image.objects.create(
                category=category,
                tags=data['tags'],
                image=images,
                user=request.user,
                )
                return redirect('/thanks')
        else:
            messages.info(request,f"This image is too small. A minimum of 3000 pixels at the longer dimension is required. Uploaded image: {w}x{h} pixels.")
            return redirect('/upload')
    else:
        categories = Category.objects.all()
        return render(request, 'upload image.html', {'categories': categories})

        


def thanks(request):
    return render(request, 'thanks.html')


def licence(request):
    return render(request, 'licence.html')


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')
