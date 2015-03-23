# Windows Event Log Viewer
# FB - 201012116

import pandas as pd
import time
import datetime
import re
import string


def date2sec(evt_date):
    '''
    This function converts dates with format
    '12/23/99 15:54:09' to seconds since 1970.
    '''
    regexp = re.compile('(.*)\\s(.*)')  #store result in site
    reg_result = regexp.search(evt_date)
    date = reg_result.group(1)
    the_time = reg_result.group(2)
    (mon, day, yr) = map(lambda x: string.atoi(x), string.split(date, '/'))
    (hr, min, sec) = map(lambda x: string.atoi(x), string.split(the_time, ':'))
    tup = [yr, mon, day, hr, min, sec, 0, 0, 0]

    sec = time.mktime(tup)

    return sec


def get_eventlog():
    import win32evtlog  # requires pywin32 pre-installed

    server = 'localhost'  # name of the target computer to get event logs
    logtype = 'Security'  #'System' # 'Application' # 'Security'
    hand = win32evtlog.OpenEventLog(server, logtype)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    #EVENTLOG_FORWARDS_READ EVENTLOG_BACKWARDS_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)
    print('total: {}'.format(total))
    i = 0
    break_loop = False
    tmp_array = []
    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if events:
            for event in events:
                tmp_array.append((
                event.EventCategory,
                datetime.datetime.fromtimestamp(date2sec(event.TimeGenerated.Format())),
                event.SourceName,
                event.EventID,
                event.EventType))
                i += 1
                #print i
                if i == 1000:
                    break_loop = True
                    break
            if break_loop == True:
                break
    df = pd.DataFrame(tmp_array, columns=['EventCategory', 'TimeGenerated', 'SourceName', 'EventID', 'EventType'])
    df.to_pickle('df.pkl')
    print df.head(5)


def get_saved_eventlog():
    return pd.read_pickle('df.pkl')
