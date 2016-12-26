#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import tasbot3
from tasbot3.customlog import Log

if __name__=="__main__":
	tasbot3.check_min_version((1,))
	configfile = "Main.conf"
	config = tasbot3.config.Config(configfile)
	Log.init(config.get('tasbot', 'logfile', 'bot.log'),
			 config.get('tasbot', 'loglevel', 'info'), True )

	r = False
	for arg in sys.argv:
		if arg.strip() == "-r":
			r = True
			Log.Notice("Registering account")
	pidfile = config.get('tasbot','pidfile','bot.pid')
	print(('using pidfile %s'%pidfile))
	inst = tasbot3.DefaultApp(configfile,pidfile,r,True)
	if int(config.get( 'tasbot','debug', 0 )):
		inst.run()#exec in fg
	else:
		inst.start()
