
iset = [
  'naw',
  'ldia',
  'ldib',
  'ldic',
  'lda',
  'ldb',
  'ldc',
  'stoa',
  'stob',
  'stoc',
  'swab',
  'swac',
  'swbc',
  'add',
  'sub',
  'mul',
  'div',
  'neg',
  'shl',
  'shr',
  'not',
  'and',
  'or',
  'nand',
  'nor',
  'xor',
  'xnor',
  'cmp',
  'j',
  'jz',
  'jnz',
  'jpos',
  'jneg',
  'jl',
  'jg',
  'jequ',
  'jovf',
]

lines = '''

ldia fd
ldib 01
add
jovf 05
j 01

'''

for line in lines.split('\n'):
  if line:
    tokens = line.split(' ')
    if len(tokens) == 1:
      print(f'{hex(iset.index(tokens[0]))}00')
    else:
      print(f'{hex(iset.index(tokens[0]))}{tokens[1]}')