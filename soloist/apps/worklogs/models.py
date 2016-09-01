from django.db import models
from soloist.apps.projects.models import ProjectWorklogsAll

class WorklogFilesAll(models.Model):
    wfa_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=30)
    pwa = models.ForeignKey(ProjectWorklogsAll, models.DO_NOTHING)
    wfa_name = models.CharField(unique=True, max_length=128)
    wfa_mime_type = models.CharField(max_length=128)
    wfa_content_type = models.CharField(max_length=128)
    wfa_doc_size = models.FloatField()
    wfa_public = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'worklog_files_all'

    def __str__(self):
        return "{}: {} {}".format(self.wfa_id, self.wfa_name, self.wfa_doc_size)


class WorklogHoursAll(models.Model):
    wha_id = models.AutoField(primary_key=True)
    pwa = models.ForeignKey(ProjectWorklogsAll, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=30)
    wha_hours = models.DecimalField(max_digits=17, decimal_places=2)
    wha_rate = models.DecimalField(max_digits=17, decimal_places=2)
    wha_summary = models.CharField(max_length=128)
    wha_inv_date = models.DateTimeField(blank=True, null=True)
    wha_inv_number = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'worklog_hours_all'

    def __str__(self):
        return "{}: {} {}".format(self.wha_id, self.wha_summary, self.wha_hours)


class WorklogActionsAll(models.Model):
    waa_id = models.AutoField(primary_key=True)
    pwa = models.ForeignKey(ProjectWorklogsAll, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=30)
    waa_type = models.SmallIntegerField()
    waa_value = models.TextField()

    class Meta:
        managed = True
        db_table = 'worklog_actions_all'

    def __str__(self):
        return "{}: {} {}".format(self.waa_id, self.waa_type, self.waa_value)
