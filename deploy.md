# Deploying Django Application | Part 11

## Create Postgres database on Railway
Login to [Railway](https://railway.app?referralCode=4hWimF)
- create a database and copy variables 
- connect the database with your project


## Create .env file and Add variables that you want to hide

basic variables of database are these

`
SECRET_KEY=
DEBUG=False
DATABASE_PUBLIC_URL=
DATABASE_URL=
PGDATA=
PGDATABASE=
PGHOST=
PGPASSWORD=
PGPORT=
PGUSER=
POSTGRES_DB=
POSTGRES_PASSWORD=
POSTGRES_USER=
SSL_CERT_DAYS=

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=

`

## Add a railway.json file 

`
{
    "$schema": "https://railway.app/railway.schema.json",
    "build": {
        "builder": "NIXPACKS"
    },
    "deploy": {
        "startCommand": "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn brainbunny.wsgi",
        "restartPolicyType": "ON_FAILURE",
        "restartPolicyMaxRetries": 10
    }
}
`

## Add runtime.txt file

`
python-3.11
`

## Changes to be made in settings.py file

- Access environment variables in settings.py file

[Doc Link](https://pypi.org/project/django-environ/)

- White noise setup
[whitenoise](https://pypi.org/project/whitenoise/)

- pip install gunicorn
to install gunicorn

- Update your requirement.txt
pip freeze > requirement.txt

- Connect to Postgres database
`
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': os.environ["PGDATABASE"],
'USER': os.environ["PGUSER"],
'PASSWORD': os.environ["PGPASSWORD"],
'HOST': os.environ["PGHOST"],
'PORT': os.environ["PGPORT"],
`

- Grant access of your git repo and try to deploy


- Create S3 bucket and add IAM user, add permission, add profile user.png file 

- Connect to S3 Bucket
pip install boto3
pip install django-storages

add 'storages' to INSTALLED_APPS

don't forget to update your requirement.txt
`
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'us-east-2' 

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGES = 'storages.backends.s3boto3.S3Boto3Storage'
`