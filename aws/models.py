from django.db import models

class TestFile(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='test-uploads/')  # Files will be uploaded to S3
