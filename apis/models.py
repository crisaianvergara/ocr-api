from django.db import models


class Receipt(models.Model):
    date = models.CharField(max_length=30)
    vendor = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=4)
    description = models.TextField()
    status = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "receipts"
        db_table = "apis_receipts"

    def __str__(self) -> str:
        return self.vendor
