with open('transcripcion.txt', encoding='utf-8') as f:
    texto = f.read()
    texto = texto.strip()
    texto = texto.replace('tʃ','$')
    texto = texto.replace(' ʝ,',' i,')

for item in '.,!¡¿?“”:':
    texto = texto.replace(item, '')

data = {
    'total': 0,
    'cv': {
    'consonantes': 0, 'vocales': 0
    },
    'apariciones': {}
}

for item in texto:
    if item != " ":
        data['total'] += 1
        if item in 'aeiou':
            data['cv']['vocales'] += 1
        else:
            data['cv']['consonantes'] += 1
        if item not in data['apariciones']:
            data['apariciones'][item] = 1
        else:
            data['apariciones'][item] += 1

data['apariciones'] = {k: v for k, v in sorted(data['apariciones'].items(), key=lambda item: item[1], reverse=True)}

def porcentaje(n):
    return (n*100)/data['total']

with open('data.txt', 'w', encoding='utf-8') as f:
    for item in data:
        if isinstance(data[item], dict):
            for key, value in data[item].items():
                f.write(f'{key}\t{value}\t{porcentaje(value)}\n')
            f.write('\n')
        else:
            f.write(f'{item}\t{data[item]}\n')
