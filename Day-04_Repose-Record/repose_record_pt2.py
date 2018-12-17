import pandas as pd
import numpy as np
import sys


def read_input(file):

    with open(file) as f:

        lines = f.readlines()

    times = []
    year = []
    month = []
    day = []
    hour = []
    minute = []
    guard = []
    action = []

    for l in lines:

        timestamp = l[1:17]

        times.append(timestamp)

        year.append(int(timestamp[:4]))

        month.append(int(timestamp[5:7]))

        day.append(int(timestamp[8:10]))

        hour.append(int(timestamp[11:13]))

        minute.append(int(timestamp[14:16]))

        if l[19:24] == 'Guard':

            guard.append(l[26:].split(' ')[0])

            action.append('begins shift')

        else:
            
            guard.append('')

            if l.find('falls asleep') > 0:

                action.append('falls asleep')

            elif l.find('wakes up') > 0:

                action.append('wakes up')

    lines_df = pd.DataFrame({'times': times,
                             'year': year,
                             'month': month,
                             'day': day,
                             'hour': hour,
                             'minute': minute,
                             'guard': guard,
                             'action': action})

    lines_df.loc[lines_df.guard == '', 'guard'] = np.NaN

    lines_df.sort_values(['year', 'month', 'day', 'hour', 'minute'], inplace = True)

    lines_df.ffill(inplace = True)

    return(lines_df)



def most_minutes_asleep(file):

    f = read_input(file)

    f['diff_hours'] = f['hour'].diff(1)

    f['diff_minutes'] = f['minute'].diff(1)

    assert np.all(f.loc[f.action == 'wakes up', 'diff_hours'] == 0), 'time differences go over different hours'

    minutes = []

    guards = []

    for start, stop, g in zip(f.loc[f.action == 'falls asleep', 'minute'].tolist(),
                              f.loc[f.action == 'wakes up', 'minute'].tolist(),
                              f.loc[f.action == 'wakes up', 'guard'].tolist()):

        temp_minutes = [i for i in range(start, stop)]

        minutes = minutes + temp_minutes

        temp_guard = [g] * len(temp_minutes)

        guards = guards + temp_guard

    all_minutes = pd.DataFrame({'minute': minutes, 'guard': guards})

    all_minutes_count = all_minutes.groupby(['minute', 'guard']).size().reset_index()

    selected_guard = all_minutes_count.loc[all_minutes_count[0] == all_minutes_count[0].max(), 'guard'].item()

    selected_minute = all_minutes_count.loc[all_minutes_count[0] == all_minutes_count[0].max(), 'minute'].item()

    print(int(selected_guard) * int(selected_minute))
    
    return(int(selected_guard) * int(selected_minute))





if __name__ == '__main__':

    most_minutes_asleep(sys.argv[1])

