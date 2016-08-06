#! /usr/bin/env python

import sys, getopt, os
import psycopg2
import psycopg2.extras
from elasticsearch import Elasticsearch
from elasticsearch import helpers


def get_db():
    conn = psycopg2.connect(
        database=os.getenv('DJANGO_SOLOIST_DB_NAME', 'scdb'),
        user=os.getenv('DJANGO_SOLOIST_DB_USER', 'scapp'),
        host=os.getenv('DJANGO_SOLOIST_DB_HOST', '127.0.0.1'),
        port=os.getenv('DJANGO_SOLOIST_DB_PORT', '5432'),
        password=os.getenv('DJANGO_SOLOIST_DB_PASS', 'scapp')
    )
    return conn


def index_all(rows):
    idx = 'soloist'
    es = Elasticsearch()
    es.indices.delete(index=idx, ignore=400)
    es.indices.create(index=idx)
    helpers.bulk(es, rows, index=idx, raise_on_error=True)


def sync_worklogs_all():
    conn = get_db()
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
        c.execute("""
                  SELECT pwa.pwa_id as "_id",
                         'worklog' as "_type",
                         pwa.created_by::TEXT||'@'||
                            to_char(pwa.created_at,'YYYY/MM/DD HH24:MI:SS')::TEXT||': '||
                            cpa.cpa_title as "title",
                         pa.pa_code as "pa_code",
                         pca.pca_code as "pca_code",
                         cpa.cpa_id as "cpa_id",
                         pwa.pwa_note as "body"
                  FROM project_worklogs_all pwa
                  ,    category_projects_all cpa
                  ,    client_categories_all cca
                  ,    portal_clients_all pca
                  ,    portals_all pa
                  WHERE pwa.cpa_id = cpa.cpa_id
                    AND cpa.cca_id = cca.cca_id
                    AND cca.pca_id = pca.pca_id
                    AND pca.pa_id = pa.pa_id
                  """)
        res = c.fetchall()

    for row in res:
        print(row)

    conn.close()

    index_all(res)


def main(argv):
    sync_worklogs_all()

if __name__ == "__main__":
    main(sys.argv[1:])