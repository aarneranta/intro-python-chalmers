# a very simple dictionary builder and lookup loop
import sys

def mkDict(lines):
    dict = {}
    for line in lines:
        fields = line.split(';')
        if len(fields) >= 2:
            dict[fields[0].strip()] = fields[1].strip()
    return dict


def readDict(filename):
    with open(filename) as file:
        lines = file.readlines()
    return mkDict(lines)


def main():
    filename = sys.argv[1]
    print('reading', filename)
    dict = readDict(filename)
    print('dictionary size', len(dict))
    prompt = "ange sökord+enter, sluta med enter> "
    query = input(prompt)
    while query:
        print(dict.get(query,"hittar inte"))
        query = input(prompt)

main()



