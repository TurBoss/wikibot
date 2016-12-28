#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import tasbot3
from tasbot3.customlog import Log

def main(argv):
	tasbot3.check_min_version((1,))
	configfile = "Main.conf"
	config = tasbot3.config.Config(configfile)
	Log.init(config.get('tasbot3', 'logfile', 'bot.log'),
			 config.get('tasbot3', 'loglevel', 'info'), True)

	r = False
	for arg in argv:
		if arg.strip() == "-r":
			r = True
			Log.Notice("Registering account")
	pidfile = config.get('tasbot3', 'pidfile', 'bot.pid')
	Log.notice('using pidfile {0}'.format(pidfile))
	inst = tasbot3.DefaultApp(configfile, pidfile, r, True)
	if int(config.get('tasbot3', 'debug', 0)):
		inst.run()# exec in fg
	else:
		inst.start()

if __name__=="__main__":
    main(sys.argv)
