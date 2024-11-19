from django.core.management.base import BaseCommand
from base.models import PyrlClient
from datetime import datetime
from base.models import AbstractAuditingFields

class Command(BaseCommand):
    help = 'Creates a company based upon specified input'

    # def add_arguments(self, parser):
    #     # Add optional and positional arguments here
    #     parser.add_argument('--name', type=str, help='Name to greet', required=False)

    def handle(self, *args, **kwargs):
        
        fields = PyrlClient._meta.get_fields()
        filtered_fields = [field for field in fields if not field.auto_created]
        field_dict = {}
        auditing_fields = [
            AbstractAuditingFields.CREATED_AT.attname,
            AbstractAuditingFields.CREATED_BY.attname,
            AbstractAuditingFields.LAST_UPDATED_AT.attname,
            AbstractAuditingFields.LAST_UPDATED_BY.attname
            ]
        
        for field in filtered_fields:
            if field.attname in auditing_fields:
                continue
            
            field_dict[field.attname] = input(f'{field.attname}: ')
            
        print(field_dict)
        
        field_dict['created_at'] = datetime.now()
        
        instance = PyrlClient(**field_dict)
        instance.save()
        
        # The main logic of your command
        
        self.stdout.write(f'Company: {field_dict["client_name"]} is saved!')