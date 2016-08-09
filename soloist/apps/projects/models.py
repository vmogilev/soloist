from django.db import models
from soloist.apps.categories.models import CategoryProjectsAll
from lib import utils

class ProjectWorklogsManager(models.Manager):
    def worklog_hours(self, p_cpa_id):
        from django.db import connection
        with connection.cursor() as c:
            c.execute("""SELECT w.pwa_id, w.cpa_id, w.created_at, w.created_by,
                                w.modified_at, w.modified_by,
                                coalesce(SUM(h.wha_hours),0) as total_hours,
                                coalesce(SUM(h.wha_hours*h.wha_rate),0) as total_amount
                           FROM project_worklogs_all w
                                left outer join worklog_hours_all h on (h.pwa_id = w.pwa_id)
                          WHERE w.cpa_id = %s
                       GROUP BY w.pwa_id, w.cpa_id, w.created_at, w.created_by,
                                w.modified_at, w.modified_by
                       ORDER BY w.created_at DESC""", [p_cpa_id])
            result_list = []
            for row in c.fetchall():
                p = self.model(pwa_id=row[0], cpa_id=row[1],
                               created_at=row[2], created_by=row[3],
                               modified_at=row[4], modified_by=row[5])
                p.total_hours = row[6]
                p.total_amount = row[7]
                result_list.append(p)
        return result_list

    def project_hours(self, p_cpa_id):
        from django.db import connection
        with connection.cursor() as c:
            c.execute("""SELECT coalesce(SUM(h.wha_hours),0) AS total_hours,
                                coalesce(SUM(h.wha_hours*h.wha_rate),0) as total_amount
                           FROM project_worklogs_all w JOIN worklog_hours_all h ON (h.pwa_id = w.pwa_id)
                          WHERE w.cpa_id = %s""", [p_cpa_id])
            row = c.fetchone()
        return {'total_hours': row[0], 'total_amount': row[1]}

    def worklog_nav(self, p_cpa_id, p_pwa_id):
        from django.db import connection

        with connection.cursor() as c:
            c.execute("""SELECT pwa_id id
                           FROM project_worklogs_all w
                          WHERE w.pwa_id > %s
                            AND w.cpa_id = %s
                          ORDER BY pwa_id LIMIT 1""", [p_pwa_id, p_cpa_id])
            next_id = c.fetchone()

        with connection.cursor() as c:
            c.execute("""SELECT pwa_id id
                           FROM project_worklogs_all w
                          WHERE w.pwa_id < %s
                            AND w.cpa_id = %s
                          ORDER BY pwa_id DESC LIMIT 1""", [p_pwa_id, p_cpa_id])
            prev_id = c.fetchone()

        return {'next_id': utils.if_none_this(next_id, 0, None),
                'prev_id': utils.if_none_this(prev_id, 0, None)}


class ProjectWorklogsAll(models.Model):
    pwa_id = models.BigIntegerField(primary_key=True)
    cpa = models.ForeignKey(CategoryProjectsAll, models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    modified_at = models.DateTimeField()
    modified_by = models.CharField(max_length=30)
    pwa_note = models.TextField()

    objects = models.Manager()
    gall = ProjectWorklogsManager()

    class Meta:
        managed = True
        db_table = 'project_worklogs_all'

    def __str__(self):
        return "{}: {}".format(self.pwa_id, self.created_at)
