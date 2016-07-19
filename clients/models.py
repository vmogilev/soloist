from django.db import models
from portals.models import PortalClientsAll


class ClientCategoriesAll(models.Model):
    cca_id = models.BigIntegerField(primary_key=True)
    pca = models.ForeignKey(PortalClientsAll, models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    cca_code = models.CharField(max_length=30)
    cca_name = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'client_categories_all'
        unique_together = (('pca', 'cca_code'),)

    def __str__(self):
        return "{}: {} - {}".format(self.cca_id, self.cca_code, self.cca_name)


class ClientPurchaseOrdersAll(models.Model):
    cpoa_id = models.BigIntegerField(primary_key=True)
    pca = models.ForeignKey(PortalClientsAll, models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    cpoa_number = models.CharField(max_length=30)
    cpoa_date = models.DateTimeField()
    cpoa_total = models.DecimalField(max_digits=17, decimal_places=2)
    cpoa_soa = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'client_purchase_orders_all'
        unique_together = (('pca', 'cpoa_number'),)

    def __str__(self):
        return "{}: {} - {}".format(self.cpoa_id, self.cpoa_number, self.cpoa_total)
