#
# Regular cron jobs for the python-cfengine package
#
0 4	* * *	root	[ -x /usr/bin/python-cfengine_maintenance ] && /usr/bin/python-cfengine_maintenance
