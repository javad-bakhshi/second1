from django.shortcuts import render
from  django.http import HttpResponse

def index(request):
    context={'my_name':"my name is javad",
            'your_name':"whats your name?"    }
    return render(request,'second_app\index.html',context)
