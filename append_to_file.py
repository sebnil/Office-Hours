import sys
from time import gmtime, strftime
import os

# change current directory to script directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# get first argument. usually "IN" or "OUT" but could be any string
try:
    action = sys.argv[1]
except:
    action = '?'

# append to log file
with open(os.path.join(dname, 'office_hours.txt'), 'a') as log_file:
    log_file.write("{action}\t{time}\n".format(
        action=action, time=strftime("%Y-%m-%d %H:%M:%S", gmtime())))
