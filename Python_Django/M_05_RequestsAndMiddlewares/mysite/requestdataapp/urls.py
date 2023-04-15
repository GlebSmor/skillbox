from django.urls import path
from .views import process_get_view, user_form, file_upload
app_name = "requestdataapp"

urlpatterns = [
    path("get/", process_get_view, name="get-view"),
    path("bio/", user_form, name="user_form"),
    path("upload/", file_upload, name="file_upload"),

]