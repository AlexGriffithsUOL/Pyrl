from django.db import models
from chart_of_accounts.models import Account, TransactionType

sick_of_retyping = {
    'blank': False,
    'null': False
}

class VatTreatmentChoices(models.TextChoices):
    ZERO = "ZER", "0%"
    HALF = "TEN", "10%"
    FULL = "FUL", "20%"

class Transaction(models.Model):
    class Meta:
        db_table = 'transaction'
        
    transaction_id = models.BigAutoField(primary_key=True)
    reference_description = models.TextField()
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, **sick_of_retyping)
    net = models.DecimalField(decimal_places=4, max_digits=15, **sick_of_retyping)
    vat_type = models.CharField(choices=VatTreatmentChoices, default=VatTreatmentChoices.FULL, **sick_of_retyping)
    vat = models.DecimalField(decimal_places=4, max_digits=15, blank=True)
    gross = models.DecimalField(decimal_places=4, max_digits=15, blank=True)
    date_of_transaction = models.DateField(blank=True,  )
    transaction_type = models.ForeignKey(to=TransactionType, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.reference_description} - {self.gross} / {self.date_of_transaction}'
    
    def calculate_vat(self):
        match self.vat_type:
            case "ZER":
                self.vat = 0
                return 0.0
            
            case "TEN":
                self.vat = self.net * 0.1 
                return self.vat
            
            case "FUL":
                self.vat = self.net * 0.2
                return self.vat
            
    def calculate_gross(self):
        self.gross = self.net + self.vat
        return self.gross
            
    
    