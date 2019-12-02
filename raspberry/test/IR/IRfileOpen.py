IRlist = list(input().split(" "))
# IRlist = ['tvOn', 'utf-8', 'ABC123']
f = open('RemoteController.txt', 'a', encoding="utf8")

for i in IRlist:
    f.write(i+'\t')
f.write('\n')
f.close()
