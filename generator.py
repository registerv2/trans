import codecs,random,os,sys
from transliterate import translit
workdir = os.path.dirname(__file__)
listname = workdir + '\\adjective.list'
adjective_list = codecs.open(listname,'r','utf_8')
adjective_table = adjective_list.read().split('\n')
adjective_list.close()

listname = workdir + '\\verb.list'
verb_list = codecs.open(listname,'r','utf_8')
verb_table = verb_list.read().split('\n')
verb_list.close()

listname = workdir + '\\noun.list'
noun_list = codecs.open(listname,'r','utf_8')
noun_table = noun_list.read().split('\n')
noun_list.close()

#for item in adjective_table:#[:-1]:
    #print (item)
adj = adjective_table[random.randint(0,len(adjective_table))]
vrb = verb_table[random.randint(0,len(verb_table))]
noun = noun_table[random.randint(0,len(noun_table))]

print (vrb.capitalize())
print (adj.capitalize())
print (noun.capitalize())
num = random.randint(100,999)

adjective_translite = translit(adj[0:4], 'ru', reversed=True)
verb_translite = translit(vrb[0:4], 'ru', reversed=True)
noun_translite = translit(noun[0:4], 'ru', reversed=True)

print (verb_translite[0:4].capitalize()+adjective_translite[0:4].capitalize()+noun_translite[0:4].capitalize()+str(num))
fname = str(num)+'.csv'
csv_name = workdir + '\\' + fname
csv_list = codecs.open(csv_name,'w','cp1251')
csv_list.write(verb_translite[0:4].capitalize()+adjective_translite[0:4].capitalize()+noun_translite[0:4].capitalize()+str(num))
csv_list.write("\n"+vrb+" "+adj+""+noun)
csv_list.close()

