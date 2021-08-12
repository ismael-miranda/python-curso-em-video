pessoas = {'nome':'Ismael', 'sexo':'M', 'idade':34}
print('mostrar somente as chaves(keys) do dicionario')
for k in pessoas.keys():
    print(k)

print('\nmostrar somente os valores(values) do dicionario')
for v in pessoas.values():
    print(v)

print('\nmostrar tudo com items do dicionario')
for i in pessoas.items():
    print(i)

print('mostrar os items, do dicionario, formatado')
for k, v in pessoas.items():
    print(f'{k} = {v}')