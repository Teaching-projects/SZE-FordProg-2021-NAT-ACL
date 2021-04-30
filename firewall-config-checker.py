import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'ACCESSLIST',
    'ENTITYNAME',
    'INT',
    'PERMIT',
    'DENY',
    'STANDARD',
    'EXTENDED',
    'TCP',
    'UDP',
    'IP',
    'ANY',
    'HOST',
    'OBJECT',
    'EQ',
    'LT',
    'GT',
    'IPADDR'
]

def t_ACCESSLIST(t):
    r'access\-list'
    return t

def t_PERMIT(t):
    r'permit'
    return t

def t_DENY(t):
    r'deny'
    return t
    
def t_STANDARD(t):
    r'standard'
    return t

def t_EXTENDED(t):
    r'extended'
    return t

def t_TCP(t):
    r'tcp'
    return t

def t_UDP(t):
    r'udp'
    return t

def t_IP(t):
    r'ip'
    return t

def t_ANY(t):
    r'any'
    return t

def t_HOST(t):
    r'host'
    return t

def t_OBJECT(t):
    r'object'
    return t

def t_EQ(t):
    r'eq'
    return t
    
def t_GT(t):
    r'gt'
    return t
    
def t_LT(t):
    r'lt'
    return t

t_ENTITYNAME = r'[a-zA-Z]+[a-zA-Z0-9\_\.\-]*'
t_INT = r'[0-9]+'
t_IPADDR = r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])'
t_ignore = r' \n'

def t_error(t):
    print("Not permitted input!")
    t.lexer.skip(1)

lexer = lex.lex()

data=''
with open('example.txt', 'r') as f:
    data=f.read().split()

print(data)

for i in data:
    lexer.input(i)
    while True:
        tok = lexer.token()
        if not tok: break
        print(tok.type, tok.value)