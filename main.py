import win_event_logs

df = win_event_logs.get_saved_eventlog()
#print df.head(5)
from datetime import datetime, timedelta

base = datetime.today()
date_list = [base - timedelta(days=x) for x in range(0, 14)]
for date in date_list:
    #print date.year, date.month, date.day
    df1 = df[
        #(df['EventID'] == 4616)
        (df['TimeGenerated'] > datetime(date.year, date.month, date.day))
        & (df['TimeGenerated'] < datetime(date.year, date.month, date.day) + timedelta(days=1))
    ]
    df1.sort('TimeGenerated')
    #print df1.tail(1)
    #print df1.head(1)

    if len(df1) > 0:
        print('# Date: {}'.format(date))
        d = df1.tail(1)['TimeGenerated']
        print('First login: {}'.format(df1.tail(1)['TimeGenerated'].values[0]))
        print('Last login: {}'.format(df1.head(1)['TimeGenerated'].values[0]))
        print('')
# print df[(df['EventID'] == 4616) & (df['TimeGenerated'] == datetime(2015, 03, 22))]['TimeGenerated']