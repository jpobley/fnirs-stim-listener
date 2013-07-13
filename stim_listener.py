######
# Local server for fNIRS trials that records stim marks and timings
######

import os, sys, logging, time
#import bottle
#from bottle import  response, request, run, route

import BaseHTTPServer

#####
# define custom HTTP handler
####
class StimRequestHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    # handle a GET
    def do_GET(self):
           # want to extract the state=[1248] part of the path 
           print self.path
           
           #get request params
           try:
               # have to parse the req params from the path string yourself - so put them into a dictionary (not super robust)
               param_str=self.path.split('?')[1]
               params = dict([(param.split('=')) for param in param_str.split('&')])
               print params
               state = params['state']
               aux = state_codes[state]
               msg = params['msg']
               if state == "start":
                   pID = params['pID']
                   setup_log(pID)
               log_msg = "%f\t%s" % (time.time(), msg)
               logging.debug(log_msg)
               
               
           except:
               print 'error'

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

####
# run the HTTP server
#####

def run_server():
    server_address = ('127.0.0.1', 1234)
    httpd = BaseHTTPServer.HTTPServer(server_address, StimRequestHTTPHandler)
    print('http server is running...')
    httpd.serve_forever()
    
######
# run application
######

run_server()

