# dateconvert.py
#   Converts a date in form "mm/dd/yyyy" to "month day, year"

def main():
    # Get the date
    date_str = input("Enter a data (mm/dd/yyyy): ")

    # Split into componets
    month_str, day_str, year_str = date_str.split('/')

    # Convert month_str to month name
    months = ['January', 'February', 'March', 'April',
              'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']
    month_str = months[int(month_str) - 1]

    # Output results in month day, year format
    print("The converted date is {0} {1}, {2}.".format(month_str, day_str, year_str))

if __name__ == '__main__':
    main()
