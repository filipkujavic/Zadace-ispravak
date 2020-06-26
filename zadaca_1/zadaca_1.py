Igrac1= input ('Unesi skare,papir,stijena,guster ili spock')
Igrac2= input ('Unesi skare,papir,stijena,guster ili spock')

if Igrac1=='skare' and Igrac2=='papir':
    print('Skare režu papir. Igrac1 je pobijedio!')
elif Igrac1=='papir' and Igrac2=='skare':
    print('Skare režu papir. Igrac2 je pobijedio!')
elif Igrac1=='papir' and Igrac2=='stijena':
    print ('Papir prekriva stijenu. Igrac2 je pobijedio!')
elif Igrac1=='stijena' and Igrac2=='papir':
    print ('Papir prekriva stijenu. Igrac1 je pobijedio!')
elif Igrac1=='stijena' and Igrac2=='guster':
    print ('Stijena drobi guštera. Igrac1 je pobijedio!')
elif Igrac1=='guster' and Igrac2=='stijena':
    print ('Stijena drobi guštera. Igrac2 je pobijedio!')
elif Igrac1=='papir' and Igrac2=='stijena':
    print('Papir prekriva stijenu. Igrac1 je pobijedio!')
elif Igrac1=='stijena' and Igrac2=='papir':
    print('Papir prekriva stijenu. Igrac2 je pobijedio!')
elif Igrac1=='guster' and Igrac2=='spock':
    print('Guster truje Spock. Igrac1 je pobijedio!')
elif Igrac1=='spock' and Igrac2=='guster':
    print('Guster truje Spock. Igrac2 je pobijedio!')
elif Igrac1=='spock' and Igrac2=='skare':
    print('Spock razbija skare. Igrac2 je pobijedio!')
elif Igrac1=='skare' and Igrac2=='spock':
    print('Spock razbija skare. Igrac2 je pobijedio!')
elif Igrac1=='skare' and Igrac2=='guster':
    print('Skare obrubljuju guštera. Igrac1 je pobijedio!')
elif Igrac1=='guster' and Igrac2=='skare':
    print('Skare obrubljuju guštera. Igrac2 je pobijedio!')
elif Igrac1=='guster' and Igrac2=='papir':
    print('Guster jede papir. Igrac1 je pobijedio!')
elif Igrac1=='papir' and Igrac2=='guster':
    print('Guster jede papir. Igrac2 je pobijedio!')
elif Igrac1=='papir' and Igrac2=='spock':
    print('Papir opovrgava Spock. Igrac1 je pobijedio!')
elif Igrac1=='spock' and Igrac2=='papir':
    print('Papir opovrgava Spock. Igrac2 je pobijedio!')                                                
elif Igrac1=='spock' and Igrac2=='stijena':
    print('Spock isparava stijenu. Igrac1 je pobijedio!')
elif Igrac1=='stijena' and Igrac2=='spock':
    print ('Spock isparava stijenu. Igrac2 je pobijedio!')
elif Igrac1=='stijena' and Igrac2=='skare':
    print('Stijena drobi škare. Igrac1 je pobijedio!')
elif Igrac1=='skare' and Igrac2=='stijena':
    print('Stijena drobi škare. Igrac2 je pobijedio!')
elif Igrac1=='papir' and Igrac2=='papir':
    print('Neriješeno!')
elif Igrac1=='skare' and Igrac2=='skare':
    print('Neriješeno!')
elif Igrac1=='spock' and Igrac2=='spock':
    print('Neriješeno!')
elif Igrac1=='stijena' and Igrac2=='stijena':
    print('Neriješeno!')
elif Igrac1=='guster' and Igrac2=='guster':
    print('Neriješeno!')
else:
    print('Neispravne vrijednosti')                    
