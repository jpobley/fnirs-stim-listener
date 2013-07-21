#!/usr/bin/python
######
# Local server for fNIRS trials that records stim marks and timings
######

import os, logging, time, serial
from urlparse import urlparse, parse_qs

import BaseHTTPServer

#####
# define custom HTTP handler
####
class StimRequestHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def do_GET(self):
           
           try:
               result = urlparse(self.path)
               params = parse_qs(result.query)
               state = params['state'][0]
               aux = state_codes[state]
               msg = params['msg'][0]
               if state == "start":
                   pID = params['pID'][0]
                   setup_log(pID)
               log_msg = "%f\t%s" % (time.time(), msg)
               logging.debug(log_msg)
               ser.write(aux)
               if state == "stop":
                   ser.close()
               self.send_response(200)

           except:
               print 'error'
               self.send_response(500)
           
           self.end_headers()
           return
           

####
# run the HTTP server
#####

def run_server():
    """Main function that runs the server"""
    server_address = ('127.0.0.1', 1234)
    httpd = BaseHTTPServer.HTTPServer(server_address, StimRequestHTTPHandler)
    print('http server is running...')
    httpd.serve_forever()

######
# dict for mapping widget event codes to auxiliary serials ports
######

state_codes = {"recording":2, "stopped recording":4, "start": 8, "stop": 8, "new_stim": 1}

######
# serial port object
######

ser = serial.Serial(3, 19200, timeout=1)

######
# function to create unique log file for this session
######

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
# run application
######

run_server()
