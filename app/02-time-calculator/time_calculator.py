def format_time(h, m, suffix=None):

    if (m < 10):
        # 3 should print as 03
        m = f"0{m}"

    # Midnight
    if (h == 0):
        return f'{12}:{m} AM{suffix}'

    # Noon
    if (h == 12):
        return f'{12}:{m} PM{suffix}'
    
    # Afternoon
    if (h > 12):
        return f'{h-12}:{m} PM{suffix}'
    
    # After midnight till Noon
    return f'{h}:{m} AM{suffix}'


def add_time(start, duration, week=None):

    try:
        hour = int(str(start).split(":")[0])
        min = int(str(start).split(":")[1].split()[0])
        ampm = str(start).split(":")[1].split()[1]
        durHr = int(str(duration).split(":")[0])
        durMn = int(str(duration).split(":")[1])
        #print(hour, min, ampm, durHr, durMn)
    except:
        return "failed"

    # convert to 24 hour system
    if (ampm == "PM"):
        hour += 12
    
    newMin = durMn + min
    newHr = durHr + hour

    if newMin > 59:
        newHr += 1
        newMin = newMin - 60

    newDays = newHr // 24
    newHr = newHr %  24

    laterMesg = ""

    WEEK2NUM = {"sunday": 0,
            "monday": 1,
            "tuesday": 2,
            "wednesday": 3,
            "thursday": 4,
            "friday": 5,
            "saturday": 6,
            }
    
    NUM2WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if (week is not None):
        
        newWeek = NUM2WEEK[((WEEK2NUM[week.lower()] + newDays) - 7) % 7]
        print(f'1--{WEEK2NUM[week.lower()]} 2--{NUM2WEEK[(WEEK2NUM[week.lower()])]} 3--{newWeek}')
        laterMesg = f", {newWeek}"

    if newDays > 1:
        laterMesg = laterMesg + f" ({newDays} days later)"
    elif newDays == 1:
        laterMesg = laterMesg + " (next day)"

    new_time = format_time(newHr, newMin, laterMesg)
    
    print(f'Returning new time {new_time}')
    return new_time

if __name__ == "__main__":
    add_time("8:16 PM", "466:02", "tuesday")
    add_time("11:59 PM", "24:05", "Wednesday")


