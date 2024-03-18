def add_time(start, duration, day=None):
    # Parsing start time and duration
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Adding time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + end_minute // 60
    end_minute %= 60

    # Calculating period changes
    period_change = end_hour // 12
    end_hour %= 12

    if end_hour == 0:
        end_hour = 12

    # Updating period and calculating days later
    if period == 'AM' and period_change % 2 != 0:
        period = 'PM'
    elif period == 'PM' and period_change % 2 != 0:
        period = 'AM'
        period_change += 1  # Additional day passes when PM switches to AM

    days_later = period_change // 2

    # Formatting the new time
    new_time = f"{end_hour}:{end_minute:02d} {period}"

    # Day of the week calculation, if day is provided
    if day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = days_of_week.index(day.capitalize()) + days_later
        new_day = days_of_week[day_index % 7]
        new_time += f', {new_day}'

    # Adding notation for days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

# Testing the corrected function
print(add_time('11:55 AM', '3:12'))  # Should return '3:07 PM'
print(add_time('11:59 PM', '24:05'))  # Should return '12:04 AM (2 days later)'
print(add_time('8:16 PM', '466:02'))  # Should return '6:18 AM (20 days later)'