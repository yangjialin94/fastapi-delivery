import re

def parse_sap_date(date: str):
    regex = re.compile("/Date[(]([0-9]+)[)]/$")
    match = regex.match(date)

    if match is None:
        raise Exception(f"Bad date: {date}")

    try:
        date = int(match.groups()[0])
    except TypeError:
        raise Exception(f"Bad date: {date}")
        
    return date
