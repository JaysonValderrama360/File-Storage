from django.shortcuts import render, HttpResponse
from .models import IncomingFiles
from .forms import FileUploadForm 

# Create your views here.

def index(request):
    if request.method == 'POST':
        c_form = FileUploadForm(request.POST, request.FILES)

        if c_form.is_valid():
            name = c_form.cleaned_data['file_name']
            date = c_form.cleaned_data['date_received']
            status = c_form.cleaned_data['status']
            protocol = c_form.cleaned_data['protocol']
            notes = c_form.cleaned_data['notes']
            touched = c_form.cleaned_data['last_touched']
            file = c_form.cleaned_data['file']

            
            IncomingFiles(file_name=name, date_received=date, status=status, 
            protocol=protocol, notes=notes, last_touched=touched, file=file).save()
            

            return HttpResponse("file uploaded")
        else:
            return HttpResponse("error")


    else:

        context = {
        'form':FileUploadForm()

    }
    return render(request,'index.html', context)

def show_file(request):
    all_data = IncomingFiles.objects.all()

    context = {
        'data':all_data
    }

    return render(request, 'view.html', context)
