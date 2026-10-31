def parse_event(line): 
    line = line.split(" ")
    
    if len(line) >= 3:
        time, level, *message = line
        message = ' '.join(message).strip()
        return {"time": time, "level": level, "message": message} 
    else:
        raise ValueError("")

def count_levels(lines): 
    count = { } 
    for line in lines: 
    line = line.split("-")  
    if len(line) = 0:
        continue 
        

