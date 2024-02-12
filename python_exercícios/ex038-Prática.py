n1 = int(input('Priemiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[1;1;31mPRIMEIRO\033[0;m valor é maior')
elif n2 > n1:
    print('O \033[1;1;36mSEGUNDO\033[0;m valor é maior')
else:
    print('Os dois valores são\033[4;1;35mIGUAIS\033[0;m')




