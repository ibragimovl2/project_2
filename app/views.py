from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import *
from app.forms import PostForms

def index(request):
    home = Home.objects.all()

    ctx = {
        "home": home,
    }
    return render(request, 'index.html', ctx)



def biz_haqimiz(request, id):


    return render(request, "biz haqimiz.html")




def blog(request, id):

    return render(request, "blog.html")



def post(request):
    module = Post()
    form = PostForms(request.POST, instance=module)
    print(request.POST)
    if form.is_valid():
        print("asas")
        form.save()
        messages.success(request, f"Sizning habaringiz muvaffaqiyatli junatildi !!")
        return redirect("post")

    ctx = {
        "form": form
    }

    return render(request, "shikoyatlar.html", ctx)


def bandqilish(request, id):

    return render(request, "bandqilish.html")
