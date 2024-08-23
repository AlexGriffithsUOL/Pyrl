from django.db import models

class request_analytics(models.Model):
    class Meta:
        db_table = 'request_analytics'

    request_id = models.UUIDField(verbose_name='Request ID', null=False, default="ERROR")
    request_time = models.DecimalField(verbose_name='Request Exec Time', null=False, default=0.0, max_digits=32, max_length=100, decimal_places=16)
    request_page = models.TextField(verbose_name='Request Path', default='ERROR', null=False)
