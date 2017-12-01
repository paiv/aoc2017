#!/usr/bin/env python3
import csv
import re
import sys


streets = (
    'street',
    'drive',
    'road',
    'avenue',
    'park',
    'way',
    'lane',
    'court',
    'loop',
    'rd',
    'dr',
    'St #300',
    'St SW',
)


def parse(problem):
    line_rx = re.compile(r'^(.*?)\s+([A-Z]{2})\s+(\w+)$')
    city_rx = re.compile(r'^(.*?\s+(?:{}))\s+(.*)$'.format('|'.join(re.escape(x) for x in streets)), re.I)
    # print(city_rx.pattern)

    res = []
    for line in problem.splitlines():
        for row in line_rx.findall(line):
            # print(row)
            street,city = city_rx.findall(row[0])[0]
            res.append((street, city, *row[1:]))

    return res


def tocsv(addresses):
    fieldnames = 'street|city|state|zipcode'.split('|')

    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()

    for adr in addresses:
        writer.writerow(dict(zip(fieldnames, adr)))


def solve(problem):
    addresses = parse(problem)
    # print(addresses)
    # print('\n'.join(sorted(x[1] for x in addresses)))
    print(tocsv(addresses))
    return ''

def getinput():
    import fileinput
    with fileinput.input() as f:
        return ''.join(f).strip()


if __name__ == '__main__':
    print(solve(getinput()))
