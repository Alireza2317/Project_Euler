# 1 jan 1900 -> mon
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight,And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


def is_leap(year):
	leap = False

	if year%4 ==0:
		leap = True

		if year%100 == 0:
			leap = False

		if year%400 == 0:
			leap = True

	return leap


months = (
	'jan', 'feb', 'mar', 'apr',
	'may', 'jun', 'jul', 'aug',
	'sep', 'oct', 'nov', 'dec'
)

weekdays = (
	'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'
)


count_sundays = 0
w_day = 365

for year in range(1901, 2000+1):
	for month in months:
		days = 31
		if month in ('sep', 'jun', 'apr', 'nov'):
			days = 30

		if month == 'feb':
			days = 28

			if is_leap(year):
				days = 29

		for day in range(1, days+1):
			if weekdays[w_day%7] == 'sun' and day == 1:
				count_sundays += 1

			w_day += 1

print(count_sundays)