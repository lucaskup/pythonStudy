#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:23:30 2017

@author: lucas
"""
idGeral = 0
dicInd = {}


def traduzId(id):
    if isinstance(id, str):    

        #legal = False
        #if id == '1o0h-63ce4c49d336ff87e0b334542dd0f64b' or id == '2iaj-63ce4c49d336ff87e0b334542dd0f64b' or id == '2g8c-63ce4c49d336ff87e0b334542dd0f64b':
        #    legal = True
        #    print('achou')
        global dicInd
        if id in dicInd:
            id = dicInd[id]
        else:
            global idGeral
            idGeral += 1
            dicInd[id] = idGeral
            id = idGeral
        #if legal:
        #    print(str(id))
    return id
class Vertice():
    def __init__(self,id, nome,rotulo):
        id = traduzId(id)
        self.id = id
        self.nome = nome
        self.rotulo = rotulo
    def __str__(self):
        return "nodo('" + str(self.id)+"','"+self.nome+"','"+self.rotulo+"')"
    def __repr__(self):
        return self.__str__()
    def csv_tulip(self):
        return str(self.id) + ';'+self.nome+';'+self.rotulo
    

    

class Aresta():
    def __init__(self,id, idInicio, idFim, rotulo):
        id = traduzId(id)
        idInicio = traduzId(idInicio)
        idFim = traduzId(idFim)
        self.id = id
        self.idInicio = idInicio
        self.idFim = idFim
        self.rotulo = rotulo
        
    def __str__(self):
        return "arco('" + str(self.idInicio)+"','"+str(self.idFim)+"','"+self.rotulo+"')"
    def __repr__(self):
        return self.__str__()
    def csv_tulip(self):
        return str(self.idInicio) + ';'+str(self.idFim)+';'+self.rotulo


import xml.etree.ElementTree as etree
tree = etree.parse("diagramaOpenOMR.xml")
root = tree.getroot()
content = root[1]
#Remove as tags JUDE pois elas tem referencia para as 
#classes e acaba lendo as classes em dobro
content.remove(content[4])
classes = tree.findall('.//{org.omg.xmi.namespace.UML}Class')
listaClasses = []
listaAtributos = []
listaMetodos = []
listaArestasAttMet = []
idInternoAresta = 0
for c in classes:
    if len(c)> 0:
        verticeClasse = Vertice(c.attrib['xmi.id'],c.attrib['name'],'classe')
        listaClasses.append(verticeClasse)
        features = c.find('{org.omg.xmi.namespace.UML}Classifier.feature')
        if features is not None:
            for f in features:
                isAttr = f.tag == '{org.omg.xmi.namespace.UML}Attribute'
                v = Vertice(f.attrib['xmi.id'],f.attrib['name'],'atributo' if isAttr else 'metodo')
                idInternoAresta += 1
                listaArestasAttMet.append(Aresta(idInternoAresta,verticeClasse.id,v.id,'atributo' if isAttr else 'metodo'))
                if isAttr:
                    listaAtributos.append(v)
                else:
                    listaMetodos.append(v)
    
herancas = tree.findall('.//{org.omg.xmi.namespace.UML}Generalization')
listaHerancas = []
for h in herancas:
    if len(h) > 0: 
        try:
            id = h.attrib['xmi.id']
            idfilho = h.find('{org.omg.xmi.namespace.UML}Generalization.child')[0].attrib['xmi.idref']
            idPai = h.find('{org.omg.xmi.namespace.UML}Generalization.parent')[0].attrib['xmi.idref']
            listaHerancas.append(Aresta(id,idfilho,idPai,'heranca'))
        except:
            print("Exception Heranças")
            pass

usos = tree.findall('.//{org.omg.xmi.namespace.UML}Usage')
listaUsos = []
for u in usos:
    if len(u) > 0: 
        try:
            id = u.attrib['xmi.id']
            idfilho = u.find('{org.omg.xmi.namespace.UML}Dependency.client')[0].attrib['xmi.idref']
            idPai = u.find('{org.omg.xmi.namespace.UML}Dependency.supplier')[0].attrib['xmi.idref']
            listaUsos.append(Aresta(id,idfilho,idPai,'uso'))
        except:
            print("Exception Heranças")
            pass

#for c in listaClasses:
#    print(c)
#for h in listaHerancas:
#    print(h)
#for h in listaUsos:
#    print(h)
#for a in listaAtributos:
#    print(a)
#for m in listaMetodos:
#    print(m)
#for a in listaArestasAttMet:
#    print(a)

print('Classes: ',str(len(listaClasses)))
print('Atributos: ',str(len(listaAtributos)))
print('Métodos: ',str(len(listaMetodos)))
print('Heranças: ',str(len(listaHerancas)))
print('Usos: ',str(len(listaUsos)))
print('AtribOuMetodo: ',str(len(listaArestasAttMet)))


with open('tulipNodes.csv','w') as file:
    for c in listaClasses:
        file.write(c.csv_tulip()+'\n')
    for a in listaAtributos:
        file.write(a.csv_tulip()+'\n')
    for m in listaMetodos:
        file.write(m.csv_tulip()+'\n')
with open('tulipEdges.csv','w') as file:
    for h in listaHerancas:
        file.write(h.csv_tulip()+'\n')
    for u in listaUsos:
        file.write(u.csv_tulip()+'\n')
    for a in listaArestasAttMet:
        file.write(a.csv_tulip()+'\n')

def outroMetodo():
    with open('basefatosprolog.pl','w') as file:
        for c in listaClasses:
            file.write(str(c)+'.\n')
        for a in listaAtributos:
            file.write(str(a)+'.\n')
        for m in listaMetodos:
            file.write(str(m)+'.\n')
        for h in listaHerancas:
            file.write(str(h)+'.\n')
        for u in listaUsos:
            file.write(str(u)+'.\n')
        for a in listaArestasAttMet:
            file.write(str(a)+'.\n')
    
