CNL fNIRS Stim Listener
===================
A small Python web server that will listen for GET requests from a remote site and send the appropriate information to a serial port on an fNIRS machine.

About
-------------------
Our lab is doing a study using [functional Near Infrared Spectroscopy](http://fnirs.org/). We are running participants through tasks that are run locally and from a hosted website. During these tasks we need to send signals to the fNIRS machine that will create stim marks on the machine readout. These marks will help us identify when certain events occur:
-   When the task begins
-   When the participant sees a new set of stimuli
-   When the participant begins recording a video
-   When the participant stops recording a video
-   When the task ends

Usage
-------------------

Authors
-------------------
