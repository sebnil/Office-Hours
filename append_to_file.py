import sys
from time import gmtime, strftime
import os

# change current directory to script directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

try:
    action = sys.argv[1]
except:
    action = '?'

with open(r"C:\ProjectArea\Office-Hours\office_hours.txt", "a") as myfile:
    myfile.write("{action}\t{time}\n".format(action=action, time=strftime("%Y-%m-%d %H:%M:%S", gmtime())))
