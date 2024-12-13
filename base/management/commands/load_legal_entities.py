from django.core.management.base import BaseCommand
from base.entity_list import LEGAL_ENTITY_DICT
from relationships.models import EntityTypes

class Command(BaseCommand):
    help = 'Load in the predefined list of legal entities'    

    def handle(self, *args, **kwargs):
        
        entities = LEGAL_ENTITY_DICT['entities']
        
        for entity in entities:
            try:
                EntityTypes(entity_id = entity['code'], description=entity['description']).save()
                print(f'Loaded {entity["description"]} ({entity["code"]})')
            except:
                print(f'WARNING Error loading {entity["description"]} ({entity["code"]}), likely already loaded')
                
        print('Finished loading legal entities')