from django.db import models

class SoftDeleteMixin(models.Model):
    class Meta:
        abstract = True
    
    deleted = models.BooleanField(default=False, null=False)
    
    def delete(self):
        self.deleted = True
        self.save()