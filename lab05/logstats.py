def parse_event(line):
    parts = line.strip().split()
    
    if len(parts) >= 3:
        time = parts[0]
        level = parts[1]
        message = ' '.join(parts[2:])
        
        valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
        if level not in valid_levels:
            raise ValueError("Неизвестный уровень")
            
        return {"time": time, "level": level, "message": message}
    elif len(parts) == 2:
        time = parts[0]
        level = parts[1]
        if level not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
            raise ValueError("Неизвестный уровень")
        return {"time": time, "level": level, "message": ""}
    else:
        raise ValueError("Неверный формат строки")


def count_levels(lines):
    counts = {}
    
    for line in lines:
        if not line.strip():
            continue
            
        try:
            event = parse_event(line)
            level = event["level"]
            
            if level in counts:
                counts[level] += 1
            else:
                counts[level] = 1
                
        except ValueError:
            if "BROKEN" in counts:
                counts["BROKEN"] += 1
            else:
                counts["BROKEN"] = 1
                
    return counts


def top_errors(lines, n):
    error_counts = {}
    
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            pass
            
    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
    return [[msg, count] for msg, count in sorted_errors[:n]]


def format_report(counts, errors):
    lines = []
    lines.append("Отчёт по журналу")
    lines.append("")
    
    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")
        
    lines.append("")
    lines.append("Частые ошибки:")
    
    if not errors:
        lines.append("- Нет ошибок")
    else:
        for err in errors:
            lines.append(f"- {err[0]} — {err[1]}")
            
    return "\n".join(lines) + "\n" 