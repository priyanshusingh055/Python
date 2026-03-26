word ="Donkey"

with open("PS/donkey.txt","r") as f:
    contant=f.read()


contantNew = contant.replace(word,"#######")   


with open("PS/donkey.txt","w") as f:
    f.write(contantNew)