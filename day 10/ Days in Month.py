# returns if a given year is a leap year or not.
def is_leap(year):
  return True if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else False

# returns the no. days in a given year and month.
def days_in_month(year,month):
  if month  not in range(1,13):
    return f"{month} is not a correct moth number!."
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  return month_days[month-1] if month != 2 else month_days[month-1]+1 if is_leap(year) else month_days[month-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







