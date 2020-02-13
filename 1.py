import string
msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
msgNova = ""
alfList = []

# Minha resolução
for letra in string.ascii_lowercase:
    alfList.append(letra)

for x in range(3):
    alfList.append(alfList[x])


for letra in msg:
    if letra in alfList:
        msgNova += alfList[alfList.index(letra)+2]
    else:
        msgNova += letra
print(msgNova)

#Resolução com maketrans

entrada = string.ascii_lowercase
saida = "cdefghijklmnopqrstuvwxyzab"
tradutor = str.maketrans(entrada,saida)

msgNova = msg.translate(tradutor)

print(msgNova)