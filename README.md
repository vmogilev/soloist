# Soloist

Soloist helps freelancers get paid by providing daily status updates to their clients.

The version in this repo is a standalone Django implementation for a single user (not multi-tenant).  It's dependencies are:

* Elasticsearch 2.3.4+
* PostgreSQL 9.5.3+
* Python 3.5+
* Django 1.9.8+

Don't want to maintain above dependencies and stack?  I am building [Soloist Cloud](http://www.hashjoin.com/soloist) - sign up for updates [here](http://hashjoin.us9.list-manage1.com/subscribe?u=70cb2018620821cd32026ce37&id=b51607c078)   

## Why

The goal of the Soloist is to encourage you (the freelancer) to provide a measurable, daily value to a client. And as a result to be distinguished as an independent, highly skilled professional.

And detailed communication about your daily activity is the key to providing ongoing value. It’s equally important for value based projects and projects billed by the hour.

It puts the client at ease and reduces anxiety and doubt. Questions like:

* “Did I hire the right person?”
* “Are they making any progress?”
* “How much is this going to cost me at the end of the week?”

are all answered by providing daily status updates.

## Tech

Refer to sections below for **Dev Workflow** and **Prod Deployment**

### Dev Workflow

Set up dev.env file as follows:

    export DJANGO_SECRET_KEY='**************************************'
    export DJANGO_SOLOIST_DB_NAME=scdb
    export DJANGO_SOLOIST_DB_USER=scapp
    export DJANGO_SOLOIST_DB_PASS=scapp
    export DJANGO_SOLOIST_DB_HOST=127.0.0.1
    export DJANGO_SOLOIST_DB_PORT=5432
    export DJANGO_DEBUG=True
    export DJANGO_LOG_LEVEL=DEBUG
    export ES_INDEX=soloist
    export ES_HOST=localhost:9200
    export AWS_ACCESS_KEY_ID=*****************
    export AWS_SECRET_ACCESS_KEY=******************************
    export AWS_DEFAULT_REGION=us-east-1
    export S3_UPLOAD_BUCKET=your-S3-bucket
    export S3_UPLOAD_PREFIX=uploads

Then a start_dev.sh as follows:

    #!/usr/bin/env bash
    
    cat << EOF
        start pg:
            pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
        stop pg:
            pg_ctl -D /usr/local/var/postgres stop -s -m fast
    
        start elastic:
            elasticsearch
    EOF
    
    . dev.env
    python manage.py runserver

Start development server (example):

    source ~/.env/soloist/bin/activate; cd ~/dev/python/soloist
    ./start_dev.sh

### Prod Deployment

TBD...

## License
Apache License 2.0 - see LICENSE
