
Channel Access bindings
-----------------------

Channel Access python bindings in cothread/catools are documented here:
http://www.cs.diamond.ac.uk/docs/docshome/cothread/index.html
and externally visible here: 
http://controls.diamond.ac.uk/downloads/python/cothread/2-11-beta/docs/html/index.html


HDF5 file format and python bindings
------------------------------------

The HDF5 file format is widely used around Diamond and documentation can be found
here: http://controls.diamond.ac.uk/downloads/python/cothread/2-11-beta/docs/html/index.html

HDF5 files can be viewed with a couple of different viewers. The most common one
is 'hdfview' - you get it in your environment by running:

    module load hdfview
    hdfview


EPICS sscan record
------------------

The sscan EPICS record can be used to scan motors and read signals from other PVs. This is
all operated and configured from the client side.

Here is a link to the sscan record documentation: http://www.aps.anl.gov/bcda/synApps/sscan/sscanRecord.html

We are interested in developing a python client for the simple 1D scan use-case. We do not
use the referenced 'saveData' software module.

