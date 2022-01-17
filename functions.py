def printdata(data):
    for item in data:
        print(f'{item:16}{data[item]}')
    print('-' * 42)


def writefile(filename, data):
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(str(data))
        f.write('\n')
        f.close()
