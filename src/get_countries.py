import re


countries_file = 'countries_table.txt'


def get_countries():
    with open(countries_file, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
    
    data = [row.split('│') for row in data ]
    data = [[el for el in row if el] for row in data]

    i = 0
    result = list()
    while i < len(data):
        if len(data[i]) < 4:
            i += 1
            continue
        
        j = i
        country = str()
        while j < len(data) - 1 and data[j+1][0].isspace():
            country += re.sub('\s+', ' ', data[j+1][1].strip()) + ' '
            j += 1
        
        country = country.strip() if country else re.sub('\s+', ' ', data[i][1].strip()).title()
        result.append(country)
        i = j + 1
    
    with open('countries.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))
    