import sys, os

INTERP = "/var/www/python/envs/gbp/bin/python"

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

import gbp.wsgi

application = gbp.wsgi.application
