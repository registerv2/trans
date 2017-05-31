## -*- coding: utf-8 -*-
import codecs, random, os, sys, clipboard
from transliterate import translit
workdir = os.path.dirname(__file__)
listname = workdir + "\/translite.list"
list = codecs.open(listname, 'r', "utf_8")
trans_table = list.read().split('\n')
list.close()
final_table = []
trans_name = []
for item in trans_table:#[:-1]:
    item = item.strip('\r')
    item = item.split(':')
    final_table.append(item)
final_table = dict(final_table[:-1])
if len(sys.argv) > 1:

    if len(sys.argv) == 3:
        while True:
            rev = str(input("Первым введено имя?(Y/n):"))
            if rev == ('y') or rev == ('Y') or rev == (''):
                name = sys.argv[1]+'.'+sys.argv[2]
                rus_name = sys.argv[1]
                rus_surname =sys.argv[2]
                print(rus_name,rus_surname,sep='\n')
                break
            elif rev == ('n') or rev == ('N'):
                name = sys.argv[2]+'.'+sys.argv[1]
                rus_name = sys.argv[2]
                rus_surname = sys.argv[1]
                print(rus_name,rus_surname,sep='\n')
                break
            else:
                print('Только Y/y или N/n')

    elif len(sys.argv) == 2:
        name = sys.argv[1]
        rus_name = sys.argv[1]
        print(rus_name)
    for i in name.lower():
        trans_name.append(final_table.get(i,'.'))
    name = ''.join(trans_name)
    #print(name+'@ritagent.com')
    print(name)
else:
    print('не введены данные пользователя')
def rnd_word_from_list(tab):
    listname = workdir + '\\' + tab +'.list'
    list = codecs.open(listname,'r','utf_8')
    table = list.read().split('\n')
    list.close()
    rnd_word = table[random.randint(0,len(table))]
    return rnd_word

noun = rnd_word_from_list('noun').capitalize().strip('\r')
verb = rnd_word_from_list('verb').capitalize().strip('\r')
adjective = rnd_word_from_list('adjective').capitalize().strip('\r')
num = str(random.randint(0,9))

pas = translit(verb, 'ru', reversed=True)[:4] + translit(adjective, 'ru', reversed=True)[:4] + translit(noun, 'ru', reversed=True)[:4] + str(random.randint(0,10))
print(pas)
print(verb,adjective,noun,num, sep=' ', end='\n')
google = rus_name.capitalize() + ',' + rus_surname.capitalize() + ',' + name + '@ritagent.com' + ',' + pas + ','  + ',' + ',' + ',' + '89031274444' + ',' + ',' + ',' + ',' + ',' + ',' + ',' + ','
print(google)
clipboard.copy(rus_name + '\n' + rus_surname + '\n' + name + '\n' + pas)
