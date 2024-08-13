from turtle import pd
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Base.models import Uploadfile

class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        file_obj = request.FILES['file']
        if not file_obj.name.endswith(('.csv', '.xlsx')):
            return Response({'error': 'Invalid file format. Only CSV and Excel files are accepted.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            uploaded_file = Uploadfile(file=file_obj)
            uploaded_file.save()
            if file_obj.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file.file.path)
            elif file_obj.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file.file.path)
            summary = f"Rows: {df.shape[0]}, Columns: {df.shape[1]}"
            return Response({'summary': summary}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)