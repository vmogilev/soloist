# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CategoryProjectsAll(models.Model):
    cpa_id = models.BigIntegerField(primary_key=True)
    cca = models.ForeignKey('ClientCategoriesAll', models.DO_NOTHING)
    cpoa = models.ForeignKey('ClientPurchaseOrdersAll', models.DO_NOTHING, blank=True, null=True)
    tua = models.ForeignKey('TeamUsersAll', models.DO_NOTHING, blank=True, null=True)
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
        managed = False
        db_table = 'category_projects_all'
        unique_together = (('cpa_code', 'cca'), ('cpa_title', 'cca'),)


class ClientCategoriesAll(models.Model):
    cca_id = models.BigIntegerField(primary_key=True)
    pca = models.ForeignKey('PortalClientsAll', models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    cca_code = models.CharField(max_length=30)
    cca_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'client_categories_all'
        unique_together = (('pca', 'cca_code'),)


class ClientPurchaseOrdersAll(models.Model):
    cpoa_id = models.BigIntegerField(primary_key=True)
    pca = models.ForeignKey('PortalClientsAll', models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    cpoa_number = models.CharField(max_length=30)
    cpoa_date = models.DateTimeField()
    cpoa_total = models.DecimalField(max_digits=17, decimal_places=2)
    cpoa_soa = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_purchase_orders_all'
        unique_together = (('pca', 'cpoa_number'),)


class ClientTeamsAll(models.Model):
    cta_id = models.BigIntegerField(primary_key=True)
    pca = models.ForeignKey('PortalClientsAll', models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    cta_code = models.CharField(max_length=30)
    cta_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'client_teams_all'
        unique_together = (('pca', 'cta_code'),)


class ClientUsersAll(models.Model):
    cua_id = models.BigIntegerField(primary_key=True)
    pca = models.ForeignKey('PortalClientsAll', models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    cua_username = models.CharField(max_length=30)
    cua_email = models.CharField(max_length=128)
    cua_fname = models.CharField(max_length=45)
    cua_lname = models.CharField(max_length=45)
    cua_mname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_users_all'
        unique_together = (('pca', 'cua_email'),)


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
        managed = False
        db_table = 'portal_clients_all'
        unique_together = (('pca_code', 'pa'),)


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
        managed = False
        db_table = 'portals_all'


class ProjectWorklogsAll(models.Model):
    pwa_id = models.BigIntegerField(primary_key=True)
    cpa = models.ForeignKey(CategoryProjectsAll, models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    pwa_note = models.TextField()

    class Meta:
        managed = False
        db_table = 'project_worklogs_all'


class TeamUsersAll(models.Model):
    tua_id = models.BigIntegerField(primary_key=True)
    cta = models.ForeignKey(ClientTeamsAll, models.DO_NOTHING)
    cua = models.ForeignKey(ClientUsersAll, models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    tua_active = models.BooleanField()
    tua_role = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'team_users_all'
        unique_together = (('cta', 'cua'),)


class WorklogActionsAll(models.Model):
    waa_id = models.BigIntegerField(primary_key=True)
    pwa = models.ForeignKey(ProjectWorklogsAll, models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    waa_type = models.SmallIntegerField()
    waa_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'worklog_actions_all'


class WorklogFilesAll(models.Model):
    wfa_id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    pwa = models.ForeignKey(ProjectWorklogsAll, models.DO_NOTHING)
    wfa_name = models.CharField(unique=True, max_length=128)
    wfa_mime_type = models.CharField(max_length=128)
    wfa_content_type = models.CharField(max_length=128)
    wfa_doc_size = models.FloatField()
    wfa_public = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'worklog_files_all'


class WorklogHoursAll(models.Model):
    wha_id = models.BigIntegerField(primary_key=True)
    pwa = models.ForeignKey(ProjectWorklogsAll, models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    wha_hours = models.DecimalField(max_digits=17, decimal_places=2)
    wha_rate = models.DecimalField(max_digits=17, decimal_places=2)
    wha_summary = models.CharField(max_length=128)
    wha_inv_date = models.DateTimeField(blank=True, null=True)
    wha_inv_number = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worklog_hours_all'
