a=int(input('enter the 1st key\n'))
b=int(input('enter the 2nd key\n'))
message=(input('enter message\n').lower())
encrypted_message=''
for i in message:
    encrypted_message+=chr(((ord(i)-ord('a'))*a+b)%26+ord('A'))
print(f'encrypted message=',encrypted_message)

'''
enter the 1st key
56
enter the 2nd key
2
enter message adadaad
adadaad
encrypted message= COCOCCO
'''
