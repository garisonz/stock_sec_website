from django.db import models

class Stock_info(models.Model):
    cik_str = models.BigIntegerField(unique=True)
    ticker = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.ticker
    
class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker