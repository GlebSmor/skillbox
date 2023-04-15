from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .forms import  UserBioForm, UploadFileForm


def process_get_view(request: HttpRequest):
    a = request.GET.get("a", "")
    b = request.GET.get("b", "")
    result = a + b
    context = {
        "a": a,
        "b": b,
        "result": result,
    }
    return render(request, "requestdataapp/request-query.html", context=context)


def user_form(request: HttpRequest):
    form = UserBioForm()
    context = {
        "form": form
    }
    return render(request, "requestdataapp/user-bio-form.html", context=context)


def file_upload(request: HttpRequest):
    
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data["file"]
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            print("Saved file", filename)
    else:
        form = UploadFileForm()
    context = {
            "form": form
        }
        
    return render(request, "requestdataapp/file-upload.html", context=context)
    
    