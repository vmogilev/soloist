from django.db import models
from categories.models import CategoryProjectsAll


class ProjectWorklogsAll(models.Model):
    pwa_id = models.BigIntegerField(primary_key=True)
    cpa = models.ForeignKey(CategoryProjectsAll, models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    pwa_note = models.TextField()

    class Meta:
        managed = True
        db_table = 'project_worklogs_all'

    def __str__(self):
        return "{}: {}".format(self.pwa_id, self.created_at)
