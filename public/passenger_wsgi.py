import sys
import os
import gbp.wsgi

INTERP = "/var/www/python/envs/gbp/bin/python"

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

application = gbp.wsgi.application
