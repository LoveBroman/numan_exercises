import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

with open('../kwh.dat', 'r') as file:
    data = file.read()

pairs = data.split('\n')


dwm = [i.split()[0] for i in pairs if len(i.split()) != 0]
kwh = [int(i.split()[1]) for i in pairs if len(i.split()) != 0]


dwm.reverse()
kwh.reverse()

kwh_arr = np.array(kwh)
monthly = np.diff(kwh_arr)
d_monthly = np.diff(kwh_arr, 2)

dates = [list(map(lambda x: int(x), i.split('-'))) for i in dwm]
dt_dates = [dt.date(i[0], i[1], i[2]) for i in dates]

dt_y = [dt_dates[i] for i in range(len(dt_dates)) if i%36 == 0 ]
#print(dt_dates)


print(f'Max month {dt_dates[np.where(monthly == monthly.max())[0][0]]}')
print(f'Min month {dt_dates[np.where(monthly == monthly.min())[0][0]]}')
print(f'Max increasing month {dt_dates[np.where(d_monthly == d_monthly.max())[0][0]]}')
print(f'Min increasing month {dt_dates[np.where(d_monthly == d_monthly.min())[0][0]]}')
print(f'mean: {monthly.mean():.5}')


#Plotta
# plt.figure(num=0, dpi=120)
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator())
# plt.plot(dt_dates[1:], monthly)
# plt.xticks(dt_y)
# plt.show()
