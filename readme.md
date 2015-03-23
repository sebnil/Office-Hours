!! This is a work in progress !! 

At work I need to fill in my office hours into a website. Sometimes I forget.
By parsing logon and logout events in the windows event log, you can get approximate office hours. 
The event log has lots of entries though, and this tool does it all for you. 
  


```
$python main.py
# Date: 2015-03-22 18:32:31.489169
First login: 2015-03-22T12:33:02.000000000+0100
Last login: 2015-03-22T14:03:55.000000000+0100

# Date: 2015-03-21 18:32:31.489169
First login: 2015-03-21T14:14:38.000000000+0100
Last login: 2015-03-21T15:30:32.000000000+0100
```