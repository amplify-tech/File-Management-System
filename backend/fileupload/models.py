from django.db import models

class FileUpload(models.Model):
    upload = models.FileField(upload_to='uploads/')
