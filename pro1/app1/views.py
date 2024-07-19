from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person

# Create your views here.
def pview(request):
    form = PersonForm()
    if request. method == "POST":
        form = PersonForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/person.html",{"form":form})


def sview(request):
     obj = Person.objects.all()
     print(obj)
     return render(request,"app1/show.html",{"per":obj})

