from django.db import models

class Stock_info(models.Model):
    cik_str = models.BigIntegerField(unique=True)
    ticker = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.ticker
    
class Filing(models.Model):
    company = models.ForeignKey(Stock_info, on_delete=models.CASCADE)
    filing_type = models.CharField(max_length=10)  # e.g., 10-K, 10-Q
    filing_date = models.DateField()
    document_url = models.URLField()
    accession_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.company.name} {self.filing_type} - {self.filing_date}"
    
class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker