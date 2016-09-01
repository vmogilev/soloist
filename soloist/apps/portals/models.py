from django.db import models


class PortalsAll(models.Model):
    pa_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=30)
    pa_code = models.CharField(unique=True, max_length=30)
    pa_name = models.CharField(max_length=128)
    pa_desc = models.CharField(max_length=512)

    class Meta:
        managed = True
        db_table = 'portals_all'

    def __str__(self):
        return "{}: {} - {}".format(self.pa_id, self.pa_code, self.pa_desc)


class PortalClientsAll(models.Model):
    pca_id = models.BigIntegerField(primary_key=True)
    pa = models.ForeignKey(PortalsAll, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=30)
    pca_code = models.CharField(max_length=30)
    pca_name = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'portal_clients_all'
        unique_together = (('pca_code', 'pa'),)

    def __str__(self):
        return "{}: {} - {}".format(self.pca_id, self.pca_code, self.pca_name)
