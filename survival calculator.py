def calculate_duration(age, units):
    
    # Calculate duration in seconds
    duration_seconds = age * 365 * 24 * 60 * 60
    
    # Convert duration to selected units
    if units == "months":
        duration = duration_seconds / (30 * 24 * 60 * 60)
    elif units == "weeks":
        duration = duration_seconds / (7 * 24 * 60 * 60)
    elif units == "days":
        duration = duration_seconds / (24 * 60 * 60)
    elif units == "hours":
        duration = duration_seconds / (60 * 60)
    elif units == "minutes":
        duration = duration_seconds / 60
    else:
        # Default to seconds if invalid unit is selected
        units = "seconds"
        duration = duration_seconds
    
    return f"The person has lived for {duration:.2f} {units}."


age = int(input("Enter the age of the person: "))
selected_units = input("Enter the time unit (months/weeks/days/hours/minutes/seconds): ")

result = calculate_duration(age, selected_units)
print(result)
