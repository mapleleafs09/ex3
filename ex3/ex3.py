import os

def files(path):
    content = os.listdir(path)
    files_txt = []
    for file in os.listdir(path):
        if file.endswith('.txt'):
            files_txt.append(file)
    return files_txt

data_dict = {}
for file in files(os.getcwd()):
    with open(f'{file}') as f:
        _n = 0
        data = []
        for line in f:
            _n += 1
            data.append(line.strip())
        data_dict[f'{file}'] = (_n, data)
print(data_dict)

sorted_tuple = sorted(data_dict.items(), key=lambda x: x[1])

print(dict(sorted_tuple))

with open('result.txt', 'wt') as f:
    for key, value in dict(sorted_tuple).items():
        f.write(f'{key}\n')
        f.write(f'{value[0]}\n')
        for line in value[1]:
            f.write(f'{line}\n')