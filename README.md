# Project Structure
## Packages
Main packages:
Django
Redis
Psycopg2
Plaid-python
*see*
> pip freeze
*for a full rundown*

## APIs
### External APIs
External APIs should be done through python packages if possible,
otherwise each API should have their own folder, and adjustments marked below:
- Plaid:
    - Plaid needs it's own webhooks files

## Auth
Currently auth is done through user model, keep it basic and build up necessary features over time

## Whitelabelling
White labelling is currently done through a middleware, this is important to allow multi-tenant environments in the Django app

## Logging
Logging is done through the syslog (see journalctl)
> sudo journalctl -xe

## Databases
First iteration: 
- Postgres
- Run as part of the EC2 setup

Second iteration:
- Severless Postgres RDS on AWS, to keep costs low and availability high


## App Structures
### Typical structure
admin.py
apps.py
forms.py
models.py
tests.py
urls.py
views.py
webhooks/
    example_webhooks.py

