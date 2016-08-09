from django.db import models
from soloist.apps.clients.models import ClientCategoriesAll, ClientPurchaseOrdersAll, TeamUsersAll


class CategoryProjectsAll(models.Model):
    cpa_id = models.BigIntegerField(primary_key=True)
    cca = models.ForeignKey(ClientCategoriesAll, models.DO_NOTHING)
    cpoa = models.ForeignKey(ClientPurchaseOrdersAll, models.DO_NOTHING, blank=True, null=True)
    tua = models.ForeignKey(TeamUsersAll, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    cpa_code = models.CharField(max_length=30)
    cpa_title = models.CharField(max_length=160)
    cpa_title_deleted = models.CharField(max_length=160, blank=True, null=True)
    cpa_summary = models.CharField(max_length=512, blank=True, null=True)
    cpa_url = models.CharField(unique=True, max_length=160)
    cpa_url_deleted = models.CharField(max_length=160, blank=True, null=True)
    cpa_deleted = models.BooleanField()
    cpa_deleted_date = models.DateTimeField(blank=True, null=True)
    cpa_deleted_by = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'category_projects_all'
        unique_together = (('cpa_code', 'cca'), ('cpa_title', 'cca'),)

    def __str__(self):
        return "{}: {} - {}".format(self.cpa_id, self.cpa_code, self.cpa_title)
