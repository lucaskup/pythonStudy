import datetime
import glob2

newFileContent = ''
arquivos = glob2.glob('Teste/Sample-Files/*')
for fil in arquivos:
    with open(fil,'r') as file:
        newFileContent += file.read() + '\n'
f = open('Teste/'+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+'.txt','w')
f.write(newFileContent)
f.close()
