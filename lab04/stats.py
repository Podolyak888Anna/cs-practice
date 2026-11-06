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

def average_by_city(records):
    total = {}
    count = {}
    for rec in records: 
        city = rec["city"]
        temp = rec["temp"]
        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1
    
    averages = {}
    for city in total:
        averages[city] = round(total[city] / count[city], 1)
    return averages 