import sys
from logstats import count_levels, top_errors, format_report

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    filename = input_data[0].strip()
    try:
        with open(filename, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return
        
    counts = count_levels(lines)
    errors = top_errors(lines, 3) 
    
    total_parsed = sum(counts.values()) - counts["BROKEN"]
    errors_count = counts["ERROR"]
    broken_count = counts["BROKEN"]
    
    print(total_parsed)
    print(errors_count)
    print(broken_count)
    
    report_text = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)

if __name__ == "__main__":
    main()