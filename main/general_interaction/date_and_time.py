import datetime
import sys

def get_date(date_format='long'):
    # Get the current date in a short or long format by filling the type parameter
    today = datetime.date.today()

    if date_format == 'short':
        return today.strftime('%d/%m/%Y')

    elif date_format == 'long':
        return today.strftime('%A %d %B')

    elif date_format == 'day':
        return today.strftime('%A')

    elif date_format == 'year':
        return today.strftime('%Y')

    elif date_format == 'month':
        return today.strftime('%b')
        
    else:
        return 'Provide a valid format for the date (short or long)'


def get_time(time_format='12'):
    time = datetime.datetime.today()

    if time_format == '12':
        time_12hr = time.strftime('%I %M%p')
        return time_12hr

    elif time_format == '24':
        time_24hr = time.strftime('%H %M%p')
        return time_24hr
    
    else:
        return 'Provide valid format (12 or 24)'



if __name__ == '__main__':
    print(get_date('short'))
    print(get_date('long'))
    print(get_date('day'))
    print(get_date('year'))

    print(get_time('12'))
    print(get_time('24'))
