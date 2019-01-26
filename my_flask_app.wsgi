#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.append('/var/www/ItemCatalog/ItemCatalog')
 
from my_flask_app import app as application
application.secret_key = 'super_secret_key'


