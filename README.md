# nermolaeva
import re

def open_file():
    f = open('textex.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    return lines

def find_matches(lines):
    regex1 = '[А-Я]\.\s+[А-Я][а-я]+'
    results1 = []
    for line in lines:
        matches1 = re.findall(regex1, line)
        if matches1:
            results1 = results1 + matches1
    results11 = '\n'.join(results1)

    regex2 = '[А-Я]\.\s+[А-Я]\.\s+[А-Я][а-я]+'
    results2 = []
    for line in lines:
        matches2 = re.findall(regex2, line)
        if matches2:
            results2 = results2 + matches2
    results22 = '\n'.join(results2)

    regex3 = r'\b[А-Я][а-я]+ \b[А-Я][а-я]+'
    results3 = []
    for line in lines:
        matches3 = re.findall(regex3, line)
        if matches3:
            results3 = results3 + matches3
    results33 = '\n'.join(results3)

    results = results11 + '\n' + results22 + '\n' + results33
    return results

def main():
    text = open_file()
    results = find_matches(text)
    print(results)

if __name__ == '__main__':
    main()


