from django.shortcuts import render

def About(request):
    return render(request,'navigation/about.html')
def Contact(request):
    return render(request,'navigation/contact.html')
