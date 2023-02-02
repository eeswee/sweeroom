from django.shortcuts import redirect, render, get_object_or_404
from .models import User

# Create your views here.

def home (request):
    name=User.objects.all()
    context={"name":name
    }
    return render(request,'base/home.html',context)