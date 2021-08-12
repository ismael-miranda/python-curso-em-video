from time import sleep

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores{num} e são ao todo {tam} números. ')
    for n in num:
        print(f'{n} ', end='', flush=True)
        sleep(0.7)
    print('FIM!')


contador(1, 2, 6, 7)
contador(3, 0, 9)
contador(6, 4, 9, 1, 3, 12)
