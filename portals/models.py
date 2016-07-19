from django.db import models


class PortalsAll(models.Model):
    pa_id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    pa_code = models.CharField(unique=True, max_length=30)
    pa_name = models.CharField(max_length=128)
    pa_desc = models.CharField(max_length=512)

    class Meta:
        managed = True
        db_table = 'portals_all'


class PortalClientsAll(models.Model):
    pca_id = models.BigIntegerField(primary_key=True)
    pa = models.ForeignKey('PortalsAll', models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    pca_code = models.CharField(max_length=30)
    pca_name = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'portal_clients_all'
        unique_together = (('pca_code', 'pa'),)
