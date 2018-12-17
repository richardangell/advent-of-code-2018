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

    minutes_alseep = f.loc[f.action == 'wakes up', ['guard', 'diff_minutes']].groupby(['guard']).sum().reset_index()

    selected_guard = minutes_alseep.loc[minutes_alseep.diff_minutes == minutes_alseep.diff_minutes.max(), 'guard'].item()

    selected_guard_actions = f.loc[f.guard == selected_guard]

    minutes = []

    for start, stop in zip(selected_guard_actions.loc[selected_guard_actions.action == 'falls asleep', 'minute'].tolist(),
                           selected_guard_actions.loc[selected_guard_actions.action == 'wakes up', 'minute'].tolist()):

        minutes = minutes + [i for i in range(start, stop)]

    minutes_count = pd.Series(minutes).value_counts().reset_index()

    max_minutes_count = minutes_count.loc[minutes_count[0] == minutes_count[0].max(), 'index'].item()

    print(int(max_minutes_count) * int(selected_guard))
    
    return(int(max_minutes_count) * int(selected_guard))





if __name__ == '__main__':

    most_minutes_asleep(sys.argv[1])

