from base.models import PyrlClient
from django.conf import settings

def build_base_url(client_id):
    client = PyrlClient.objects.get(client_id=client_id)
    return f'{client.domain}.{settings.DOMAIN}'