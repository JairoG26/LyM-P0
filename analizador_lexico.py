import ply.lex as lex
import re
import codecs
import os
import sys

tokens = [
    'ID', 'NUMBER', 'LSPARENT', 'RSPARENT', 'COMMA', 'SEMICOLON', 'COLON', 'VERTICALBAR'    
]

reservadas = {
    'ROBOT_R':'ROBOT_R', 'VARS':'VARS', 'PROCS':'PROCS', 'assignTo':'ASSIGNTO', 'goto':'GOTO', 'move':'MOVE',
    'turn':'TURN', 'face':'FACE', 'put':'PUT', 'pick':'PICK', 'moveToThe':'MOVETOTHE', 'moveInDir':'MOVEINDIR',
    'jumpToThe':'JUMPTOTHE', 'jumpInDir':'JUMPINDIR', 'nop':'NOP', 'if':'IF', 'while':'WHILE', 'then':'THEN',
    'else':'ELSE', 'do':'DO', 'repeat':'REPEAT', 'facing':'FACING', 'canPut':'CANPUT', 'canPick':'CANPICK',
    'canMoveInDir':'CANMOVEINDIR', 'canJumpInDir':'CANJUMPINDIR', 'canMoveToThe':'CANMOVETOTHE', 'canJumpToThe':'CANJUMPTOTHE',
    'not':'NOT'
}

tokens = tokens + list(reservadas.values())


t_ignore = ' \t'
t_LSPARENT = r'\[r'
t_RSPARENT = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_VERTICALBAR = r'\|'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    #t.type = reservadas.get(t.value, 'ID')
    #t.value = t.value.upper()
    if t.value.upper() in reservadas.keys():
        t.value = t.value.upper()
        t.type = t.value

    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    t.lexer.skip(1)

def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(cont)
        print(str(cont)+ ". " + file)
        cont += 1

    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break
    print("Has escogido \'%s' \n" % files[int(numArchivo) - 1])  

    return files[int(numArchivo) - 1]

directorio = "C:/Users/garav/OneDrive/Escritorio/LYM/test/"


archivo = buscarFicheros(directorio)
test = directorio + archivo
fp =codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

tokens_doc = []

while True:
    tok = analizador.token()
    if not tok: break
    tokens_doc.append(tok)
    
for i in tokens_doc:
    print(i)
    
x = 0
while True:
    if tokens_doc[x].type != 'ROBOT_R':
        print('Programa invalido!! - No inicia el robot')
        break
    else:
        x+=1
        if tokens_doc[x].type != 'VARS':
            print('Programa invalido!! - no declara variables')
            break
        else:
            x +=1
            while tokens_doc[x].type != 'PROCS':
                if tokens_doc[x].type == 'ID' or tokens_doc[x].type == 'COMMA':
                    if x == len(tokens_doc)-1:
                        print('Programa invalido!! - no declara procs')
                        break
                    else:
                        x += 1
                else:
                    if tokens_doc[x].type != 'PROCS':
                        print('Programa invalido!! - no declara procs')
                        break
                    else:
                        print('vamos bien!!')
                break
                        
                    
        



