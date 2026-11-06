import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
valid_records = read_valid(lines)

parsed_count = len(valid_records)
non_empty_lines = [line for line in lines if line.strip()]
error_count = len(non_empty_lines) - parsed_count

best_city = warmest_city(valid_records)
if best_city:
    averages = average_by_city(valid_records)
    best_temp = averages[best_city]
    print(f"{parsed_count}")
    print(f"{error_count}")
    print(f"{best_temp:.1f}")
else:
    print(f"{parsed_count}")
    print(f"{error_count}")
    print("0.0")