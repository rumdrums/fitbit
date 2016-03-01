from jfitbit import Jfitbit_cli as J
import datetime

session = J()

start = datetime.datetime(year=2015,month=01,day=01)
end = datetime.datetime.today()

steps = session.time_series('activities/tracker/steps',base_date=start,end_date=end)['activities-tracker-steps']

total_days = 0
totals = {}
for i in range(7):
	totals[i] = dict(total_steps=0,num_days=0)

for day in steps: 
	num_steps = int(day['value'])
	if num_steps: 
		total_days+=1	
		year, month, day = day['dateTime'].split('-')
		date = datetime.datetime(year=int(year), month=int(month), day=int(day))
		day_of_week = date.weekday()	
		totals[day_of_week]['total_steps'] += num_steps
		totals[day_of_week]['num_days'] += 1

#### average per day of week:
for i in totals:
	average = totals[i]['total_steps'] / totals[i]['num_days']
	print('Average for %s: %d' % (i, average))

"""
Average for 0: 8336
Average for 1: 7079
Average for 2: 7874
Average for 3: 7585
Average for 4: 6136
Average for 5: 7328
Average for 6: 7059
"""

