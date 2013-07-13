CNL fNIRS Stim Listener
===================
A small Python web server that will listen for GET requests from a remote site and send the appropriate information to a serial port on an fNIRS machine.

About
-------------------
Our lab is doing a study using [functional Near Infrared Spectroscopy](http://fnirs.org/). We are running participants through tasks that are run locally and from a hosted website. During these tasks we need to send signals to the fNIRS machine that will create stim marks on the machine readout. These marks will help us identify when certain events occur:
-   the task begins
-   the participant sees a new set of stimuli
-   the participant begins sub-task
-   the participant stops sub-task
-   the task ends
The fNIRS machine has 4 serial ports that receive signals. The difficulty is figuring out how to get the local machine that runs the fNIRS software to send this stim marks when a participant is working through a task on a remote site.

We came up with the idea of having a small Python server running at the localhost and using jQuery's getJSONP() method to send GET requests to a route on the localhost. The local server then parses the query paramenters and sends a signal to the appropriate serial port. We wanted the server to be run inside of [PsychoPy](http://www.psychopy.org "PsychoPy") so that it was easy for RA's to use. However, PsychoPy wasn't able to import the WSGIRef Python module for some reason. Our lab manager had the great idea of copying the BaseHTTPServer module into the local directory where the script would run. This solved the issue of PsychoPy being unable to run a server.

Usage
-------------------

Open the <code>stim_listenter.py</code> file from within PsychoPy and click "Run." Alternatively, the script will from from the command line:
<pre><code>python stim-listener.py</code></pre>
The script will check for a "logs" directory and create one, if necessary.

Each log file is a tab-separated list of time and events. For example:
<pre>
1373296487.745540 task started
1373296494.710930 seeing stimuli
1373296502.828394 stimuli task begins
1373296507.389035 stimuli task stops
1373296559.990404 task ended
</pre>
Authors
-------------------
jpobley
mbod
