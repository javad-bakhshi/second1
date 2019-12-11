from django.shortcuts import render
from  django.http import HttpResponse
from . import forms

def index(request):
    context={'my_name':"my name is javad",
            'your_name':"whats your name?"    }
    return render(request,'second_app\index.html',context)

def form_view(request):
    form=forms.MyForm()

    if request.method=='POST':
        form=forms.MyForm(request.POST)
        if form.is_valid():

            print("vaidation sucess!")
            print("name: "+ form.cleaned_data['name'])
            print("email: "+ form.cleaned_data['email'])
            print("text: "+ form.cleaned_data['text'])


    context={
    'form':form
    }
    return render(request,'second_app/form_page.html',context)
