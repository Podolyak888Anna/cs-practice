def parse_record(line: str)
    parts = line.split(" ; ")

    if len(parts) != 3:
        raise ValueError("Неверное количество полей")

    city, temp, date = parts 

    if not city or not date:
        raise ValueError("Пустой город или дата")
    
    temp_float = float(temp)
    return {"city": city, "temp": temp_float, "date": date} 

def read_valid(lines): 
    valid_records = []
    for line in lines:
        if not line.strip:
            continue 

        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue 
    return valid_records 