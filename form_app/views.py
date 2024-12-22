from django.shortcuts import render
from . forms import StudentForm,contactForm

# Create your views here.

def djangoForm(request):
    if request.method =='POST':
        form = contactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
    else:
        form = contactForm()
    return render(request, "./practice_form.html", {"form":form})
