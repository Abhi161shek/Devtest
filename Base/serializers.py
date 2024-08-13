from rest_framework import serializers

from Base.models import Uploadfile

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploadfile
        fields = ['id', 'file', 'uploaded_at']