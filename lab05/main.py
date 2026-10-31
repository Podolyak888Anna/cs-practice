from logstats import parse_event
with open ("events.log", "r", encoding = "utf8") as file:
    for line in file: 
        print(parse_event(line))