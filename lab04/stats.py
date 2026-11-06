def parse_record(line):
    parts = line.strip().split(";")
    
    if len(parts) != 3:
        raise ValueError("Неверное количество полей")
        
    city, temp, date = parts
    
    city = city.strip()
    date = date.strip()
    
    if not city or not date:
        raise ValueError("Пустой город или дата")
        
    try:
        temp_float = float(temp)
    except ValueError:
        raise ValueError("Температура не число")
        
    return {"city": city, "temperature": temp_float, "date": date}


def read_valid(lines):
    valid_records = []
    for line in lines:
        if not line.strip():
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
        temp = rec["temperature"]
        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1
        
    averages = {}
    for city in total:
        averages[city] = round(total[city] / count[city], 1)
    return averages


def warmest_city(records):
    averages = average_by_city(records)
    if not averages:
        return ""
        
    best_city = None
    best_temp = -999.0
    
    for city, avg_temp in averages.items():
        if avg_temp > best_temp or (avg_temp == best_temp and city < best_city):
            best_temp = avg_temp
            best_city = city
            
    return best_city