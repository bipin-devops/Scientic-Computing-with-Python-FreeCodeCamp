def add_time(start, duration, start_day = None):
    
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    

    
  
    
    # Parse start time
    time_part, period = start.split()
    start_hours, start_minutes = time_part.split(':')
    
    
    # convert hours into 24 hour format
    if period == 'PM':
        start_hours = int(start_hours) + 12

        
    # Parse duration
    duration_hours, duration_minutes = duration.split(':') 
    
    # Calculate total minutes
    total_minutes = (int(start_hours) * 60 + int(start_minutes)) + (int(duration_hours) *60 + int(duration_minutes))
    # print(total_minutes)
    
    # Calculate new hours and minutes
    new_hours = (total_minutes // 60) % 24
    new_minutes = total_minutes % 60
    
    # Calculate days passed
    days_passed = total_minutes // (24* 60)
    
    # Convert back to 12-hour format
    if new_hours >= 12:
        new_period = "PM"
        if new_hours > 12:
            new_hours -= 12
    else:
        new_period = "AM"
        if new_hours == 0:
            new_hours = 12
            
    new_time = f"{new_hours}:{new_minutes:02d} {new_period}"
    
    
    # Add day of week if provided
    if start_day is not None:
        # start_day = start_day.lower()
        start_index = days_of_week.index(start_day.lower())
        new_day_index = (start_index + days_passed) % 7
        new_time += f', {days_of_week[new_day_index].capitalize()}'
        
        
    # Add days later information
    if days_passed == 1:
        new_time += ' (next day)'
    elif days_passed > 1:
        new_time += f' ({days_passed} days later)'
    
    print("THIS IS NEW: ", new_time)
    


    return new_time

add_time('11:43 PM', '24:20', 'tueSday')