from random import choice

print('\033[1;36mVamos jogar JOKENPO!!\033[m')
print('Escolha uma das opções para jogar contra o computador:')
print('='*35)
print('\033[1mPEDRA    TESOURA     PAPEL\033[m')
print('='*35)

user = str(input('Digite sua escolha: ')).upper()

pc = ['PEDRA', 'TESOURA', 'PAPEL']
escolha_pc = choice(pc)

if user == escolha_pc:
    print('Deu empate!')
elif user == 'PEDRA' and escolha_pc == 'TESOURA':
    print('Você escolheu {} e o computador escolheu {}'.format(user, escolha_pc))
    print('Você ganhou!!!')
elif user == 'TESOURA' and escolha_pc == 'PAPEL':
    print('Você escolheu {} e o computador escolheu {}'.format(user, escolha_pc))
    print('Você ganhou!!!')
elif user == 'PAPEL' and escolha_pc == 'PEDRA':
    print('Você escolheu {} e o computador escolheu {}'.format(user, escolha_pc))
    print('Você ganhou!!!')
else :
    print('Você escolheu {} e o computador escolheu {}'.format(user, escolha_pc))
    print('O computador ganhou!!!')