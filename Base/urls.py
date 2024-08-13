from django.urls import path
from Base.views import FileUploadView  # Import the class directly

urlpatterns = [
   path('upload_file', FileUploadView.as_view(), name='upload_file'),
]