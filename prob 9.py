import calendar
def display_calendar():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    print("\n", calendar.month(year, month))
display_calendar()
