#! /usr/bin/env python

import sys, getopt, os
import psycopg2
import psycopg2.extras
from elasticsearch import Elasticsearch
from elasticsearch import helpers
# use certifi for CA certificates
import certifi


def get_db():
    conn = psycopg2.connect(
        database=os.getenv('DJANGO_SOLOIST_DB_NAME', 'scdb'),
        user=os.getenv('DJANGO_SOLOIST_DB_USER', 'scapp'),
        host=os.getenv('DJANGO_SOLOIST_DB_HOST', '127.0.0.1'),
        port=os.getenv('DJANGO_SOLOIST_DB_PORT', '5432'),
        password=os.getenv('DJANGO_SOLOIST_DB_PASS', 'scapp')
    )
    return conn


def get_es():
    es = Elasticsearch(
        [os.getenv('ES_HOST', 'localhost:9200')],
        # sniff before doing anything
        # sniff_on_start=True,
        # # refresh nodes after a node fails to respond
        # sniff_on_connection_fail=True,
        # # and also every 60 seconds
        # sniffer_timeout=60,
        use_ssl=bool(os.getenv('ES_USE_SSL', False)),
        verify_certs=True,
        ca_certs=certifi.where()
    )
    return es


def index_all(rows):
    idx = os.getenv('ES_INDEX', 'soloist')
    es = get_es()
    es.indices.delete(index=idx, ignore=[400, 404])
    es.indices.create(index=idx)
    helpers.bulk(es, rows, index=idx, raise_on_error=True)


def sync_worklogs_all():
    conn = get_db()
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
        c.execute("""
                  SELECT pwa.pwa_id AS "_id",
                         'worklog' AS "_type",
                         cpa.cpa_title AS "cpa_title",
                         pwa.created_by AS "pwa_created_by",
                         pwa.created_at AS "pwa_created_at",
                         pa.pa_code AS "pa_code",
                         pca.pca_code AS "pca_code",
                         cpa.cpa_id AS "cpa_id",
                         concat_ws(' ', pwa.pwa_note::text, (SELECT string_agg(wfa_name, ' ') AS wfa_name_list \
                         FROM worklog_files_all WHERE pwa_id = pwa.pwa_id GROUP BY pwa_id)::text) AS "pwa_note"
                  FROM project_worklogs_all pwa
                  ,    category_projects_all cpa
                  ,    client_categories_all cca
                  ,    portal_clients_all pca
                  ,    portals_all pa
                  WHERE pwa.cpa_id = cpa.cpa_id
                    AND cpa.cca_id = cca.cca_id
                    AND cca.pca_id = pca.pca_id
                    AND pca.pa_id = pa.pa_id
                    AND cpa.cpa_deleted = FALSE
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
