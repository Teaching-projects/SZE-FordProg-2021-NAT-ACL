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
    'IPADDR',
    'MASK'
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
t_MASK = r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])'
t_ignore = r' \n'

def t_error(t):
    print("Not permitted input!")
    t.lexer.skip(1)

lexer = lex.lex()

def p_acl(p):
    '''
    acl : ACCESSLIST ENTITYNAME type
    '''
    p[0]=(p[1], p[2], p[3])

def p_type(p):
    '''
    type :  STANDARD action place
            | EXTENDED action proto place service
            | EXTENDED action proto place place service
    '''
    if len(p)==4: p[0]=(p[1], p[2], p[3])
    elif len(p)==6: p[0]=(p[1], p[2], p[3], p[4], p[5])
    else: p[0]=(p[1], p[2], p[3], p[4], p[5], p[6])

def p_action(p):
    '''
    action :    PERMIT
                | DENY
    '''
    p[0]=p[1]
    
def p_proto(p):
    '''
    proto :    TCP
               | UDP
               | IP
    '''
    p[0]=p[1]

def p_place(p):
    '''
    place :    ANY
               | IPADDR MASK
               | HOST IPADDR
               | OBJECT ENTITYNAME
    '''
    if len(p)==3: p[0]=(p[1], p[2])
    else: p[0]=p[1]

def p_service(p):
    '''
    service :   EQ INT
                | LT INT
                | GT INT
                | empty
    '''
    if len(p)==3: p[0]=(p[1], p[2])
    else: p[0]=p[1]

def p_empty(p):
    '''
    empty : 
    '''
    p[0]=None
    
def p_error(p):
    print('Syntax error!')

parser=yacc.yacc()



data=''
with open('example.txt', 'r') as f:
    data=f.read().split('\n')

#print(data)

# for i in data:
    # lexer.input(i)
    # while True:
        # tok = lexer.token()
        # if not tok: break
        # print(tok.type, tok.value)

for i in data:
    parser.parse(i)
    