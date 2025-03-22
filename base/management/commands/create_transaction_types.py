from django.core.management.base import BaseCommand
from chart_of_accounts.models import TransactionType

class Command(BaseCommand):
    help = 'Creates a company based upon specified input'

    # def add_arguments(self, parser):
    #     # Add optional and positional arguments here
    #     parser.add_argument('--name', type=str, help='Name to greet', required=False)

    def handle(self, *args, **kwargs):
        model = TransactionType
        data = model.objects.all()
        
        if len(data) == 0:
            model(transaction_type='Cr').save()
            model(transaction_type='Dr').save()
            self.stdout.write('Credit and Debit transaction types Created')
            return
        
        if len(data) == 2:
            Cr = False
            Dr = False
            for item in data:
                if item.transaction_type == 'Cr':
                    Cr = True
                if item.transaction_type == 'Dr':
                    Dr = True      
            if Dr and Cr:
                self.stdout.write('Both transaction types exist')
                return
            else:
                raise Exception('There are 2 transaction types, but they do not cover both Cr and Dr')
        
        if len(data) > 2:
            raise Exception('There are more than 2 transaction types... wtf?')
        
        if len(data) < 2:
            self.stdout.write('There are less than 2 transaction types. Needs insert')
            
            if data[0].transaction_type == 'Cr':
                Cr = True
                Dr = False
            elif data[0].transaction_type == 'Dr':
                Cr = False
                Dr = True
            else:
                raise Exception('The only transaction type is neither Cr nor Dr')
            
            if Cr:
                model(transaction_type='Dr', full_type_name='Debit').save()
                self.stdout.write('Debit transaction type Created')
                return
            if Dr:
                model(transaction_type='Cr', full_type_name='Credit').save()
                self.stdout.write('Credit transaction type Created')
                return
            

            