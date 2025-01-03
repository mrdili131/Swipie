from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from django.http import JsonResponse, FileResponse
from .models import Post
from django.core.serializers import serialize
from .forms import PostUpload
from conf.settings import MEDIA_ROOT
import os, random

class IndexView(View):
    def get(self,request):
        query = request.GET.get('q','')
        if query:
            content = Post.objects.filter(text__icontains=query)
        else:
            content = Post.objects.all().order_by('?')
        page_number = request.GET.get('page',1)
        paginator = Paginator(content,10)
        page_obj = paginator.get_page(page_number)
        return render(request,'index.html',{"images":page_obj,"has_next":page_obj.has_next(),"query":query})
    
    
def upload(request):
    if request.method == 'GET':
        form = PostUpload()
        return render(request,'upload.html',{"form":form})
    elif request.method == 'POST':
        form = PostUpload(request.POST,request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
        return render(request,'upload.html',{"form":form})
    

def image_view(request,id):
    image = Post.objects.get(id=id)
    return render(request,'image_view.html',{"image":image})

def download(request,media,dir,file_name):
    path = os.path.join(MEDIA_ROOT,'images',file_name)
    if os.path.exists(path):
        response = FileResponse(open(path,'rb'),as_attachment=True,filename=f'swipie_{random.randint(1,100),random.randint(1,100)}')
        return response
    else:
        return redirect('home')
    