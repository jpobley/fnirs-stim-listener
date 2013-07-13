######
# Local server for fNIRS trials that records stim marks and timings
######

import os, sys, logging, time
import bottle
from bottle import  response, request, run, route

######
# create serial port object.mapping dictionary for upload widget codes
######

######
# dict for mapping widget event codes to auxiliary serials ports
######

state_codes = {"recording":2, "stopped recording":4, "start": 8, "stop": 8, "new_stim": 1}

def setup_log(pID):
    """Check for logs folder, create it if it doesn't exist. Create unique log file for each session"""
    cd = os.getcwd()
    logdir = '%s/logs' % (cd)
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    logname = '%s/%s' % (logdir, pID)
    logfile = "%s.txt" % (logname)
    count = 1
    while os.path.exists(logfile):
        temp_name = "%s_%d" % (logname, count)
        logfile = "%s.txt" % (temp_name)
        count += 1

    logging.basicConfig(filename=logfile, 
                        filemode="w",
                        format='%(message)s',
                        level=logging.DEBUG)


######
# define route
######

@route('/stim')
def start():
    state = request.query.state
    aux = state_codes[state]
    msg = request.query.msg
    if state == "start":
        pID = request.query.pID
        setup_log(pID)
    log_msg = "%f\t%s" % (time.time(), msg)
    logging.debug(log_msg)
    
######
# run application
######

run(host='localhost', port=1234)

