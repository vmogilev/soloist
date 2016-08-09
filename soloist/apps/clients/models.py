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


class ClientUsersAll(models.Model):
    cua_id = models.BigIntegerField(primary_key=True)
    pca = models.ForeignKey(PortalClientsAll, models.DO_NOTHING)
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
        managed = True
        db_table = 'client_users_all'
        unique_together = (('pca', 'cua_email'),)

    def __str__(self):
        return "{}: {} - {}".format(self.cua_id, self.cua_username, self.cua_email)


class ClientTeamsAll(models.Model):
    cta_id = models.BigIntegerField(primary_key=True)
    pca = models.ForeignKey(PortalClientsAll, models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    cta_code = models.CharField(max_length=30)
    cta_name = models.CharField(max_length=128)

    # https://docs.djangoproject.com/en/1.9/topics/db/models/#intermediary-manytomany
    # this doesn't actually create a field in the table - just an APP level relationship
    team_users = models.ManyToManyField(ClientUsersAll, through='TeamUsersAll')

    class Meta:
        managed = True
        db_table = 'client_teams_all'
        unique_together = (('pca', 'cta_code'),)

    def __str__(self):
        return "{}: {} - {}".format(self.cta_id, self.cta_code, self.cta_name)


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
        managed = True
        db_table = 'team_users_all'
        unique_together = (('cta', 'cua'),)
