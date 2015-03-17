#Youssouf H. Cherif
#09 - Oct - 2013
#dayzzy.py


days = ("Sunday (Dim.)","Monday (Lun.)","Tuesday (Mar.)",
	"Wednesday (Mer.)","Thursday (Jeu.)",
	"Friday (Ven.)","Saturday (Sam.)")


def computesDay(month,day,year,century):
	'''
		Returns the day of the week (eg: Monday)
	'''
	w= (13*month - 1) / 5
	x = year / 4 
	y = century / 4
	z = w + x + y + day + year - 2*century
	return z%7

def regulateMonth(month,year):
	'''
		the month of the year, with March having the value 1, April the
		value 2, . . ., December the value 10, and January and February being
		counted as months 11 and 12 of the preceding year (in which
		case,subtract 1 from C)
	'''
	if month - 2 ==0:
		month = 12
		year -=1
	elif month - 2 == -1:
		month = 11
		year -= 1
	else:
		month -=2
	return month,year

def main():
	day = input("Enter the day of the month (1-31): ")
	month = input("Enter the month of the year (1-12): ")
	temp = input("Enter the year (e.g: 2013): ")
	temp = str(temp) # convert to string the year
	century = int(temp[0:2]) # take the 2 first number of temp and cast to int
	year = int(temp[2:]) # take the 2 last number of temp and cast to int
	month,year = regulateMonth(month,year)
	result = computesDay(month,day,year,century) # call the function computeDay
	print "The of the week of the given date is: ",days[result] # print the result


if __name__ == '__main__':
	main()