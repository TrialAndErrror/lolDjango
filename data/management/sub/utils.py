import re


def map_to_assignment(data):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    for key in data:
        print(f"{pattern.sub('_', key).lower()}=participant[\"{key}\"],")
