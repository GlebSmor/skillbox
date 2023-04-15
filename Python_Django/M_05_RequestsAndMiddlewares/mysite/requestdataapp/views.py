from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


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
    return render(request, "requestdataapp/user-bio-form.html")


def file_upload(request: HttpRequest):
    if request.method == "POST" and request.FILES.get("myfile"):
        file = request.FILES["myfile"]
        max_size = 1
        
        if file.size / 1048576 > max_size:
             return HttpResponse(f"<h1>File size error!</h1>\n" \
                                 f"<h2>File bigger than {max_size} mb</h2>")
         
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        print("Saved file", filename)
        
    return render(request, "requestdataapp/file-upload.html")
    
    