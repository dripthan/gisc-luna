
ain      = 0b100000000000000000000
bIn      = 0b010000000000000000000
cin      = 0b001000000000000000000
aout     = 0b000100000000000000000
bout     = 0b000010000000000000000
cout     = 0b000001000000000000000
marin    = 0b000000100000000000000
irin     = 0b000000010000000000000
fin      = 0b000000001000000000000
pcin     = 0b000000000100000000000
pcout    = 0b000000000010000000000
pc       = 0b000000000001000000000
endi     = 0b000000000000100000000
op3      = 0b000000000000010000000
op2      = 0b000000000000001000000
op1      = 0b000000000000000100000
op0      = 0b000000000000000010000
aluout   = 0b000000000000000001000
ramin    = 0b000000000000000000100
ramout1  = 0b000000000000000000010
ramout0  = 0b000000000000000000001

insts = [

  # naw
  pcout | marin,
  ramout1 | irin | pc,
  endi,
  0,
  0,
  0,
  0,
  0,

  # ldia
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | ain,
  endi,
  0,
  0,
  0,
  0,

  # ldib
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | bIn,
  endi,
  0,
  0,
  0,
  0,

  # ldic
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | cin,
  endi,
  0,
  0,
  0,
  0,

  # lda
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | marin,
  ramout0 | ain,
  endi,
  0,
  0,
  0,

  # ldb
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | marin,
  ramout0 | bIn,
  endi,
  0,
  0,
  0,

  # ldc
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | marin,
  ramout0 | cin,
  endi,
  0,
  0,
  0,

  # stoa
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | marin,
  aout | ramin,
  endi,
  0,
  0,
  0,

  # stob
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | marin,
  bout | ramin,
  endi,
  0,
  0,
  0,

  # stoc
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | marin,
  cout | ramin,
  endi,
  0,
  0,
  0,

  # swab
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | marin,
  aout | ramin,
  bout | ain,
  ramout0 | bIn,
  endi,
  0,

  # swac
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | marin,
  aout | ramin,
  cout | ain,
  ramout0 | cin,
  endi,
  0,

  # swbc
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | marin,
  bout | ramin,
  cout | bIn,
  ramout0 | cin,
  endi,
  0,

  # add
  pcout | marin,
  ramout1 | irin | pc,
  aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # sub
  pcout | marin,
  ramout1 | irin | pc,
  op0 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # mul
  pcout | marin,
  ramout1 | irin | pc,
  op1 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # div
  pcout | marin,
  ramout1 | irin | pc,
  op1 | op0 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # neg
  pcout | marin,
  ramout1 | irin | pc,
  op2 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # shl
  pcout | marin,
  ramout1 | irin | pc,
  op2 | op0 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # shr
  pcout | marin,
  ramout1 | irin | pc,
  op2 | op1 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # not
  pcout | marin,
  ramout1 | irin | pc,
  op2 | op1 | op0 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # and
  pcout | marin,
  ramout1 | irin | pc,
  op3 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # or
  pcout | marin,
  ramout1 | irin | pc,
  op3 | op0 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # nand
  pcout | marin,
  ramout1 | irin | pc,
  op3 | op1 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # nor
  pcout | marin,
  ramout1 | irin | pc,
  op3 | op1 | op0 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # xor
  pcout | marin,
  ramout1 | irin | pc,
  op3 | op2 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # xnor
  pcout | marin,
  ramout1 | irin | pc,
  op3 | op2 | op0 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # cmp
  pcout | marin,
  ramout1 | irin | pc,
  op3 | op2 | op1 | aluout | ain | fin,
  endi,
  0,
  0,
  0,
  0,

  # j
  pcout | marin,
  ramout1 | irin | pc,
  ramout0 | pcin,
  endi,
  0,
  0,
  0,
  0
]

for i in insts:
  print(hex(i))