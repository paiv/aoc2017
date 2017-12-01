; synacor vm
in a
push a

input:
in b
eq e b 10
jf e :compare
pop b

compare:
eq c a b
jf c :skip
add a a -0x30
add d d a

skip:
set a b
jf e :input

push 0

div10:
mod a d 10
add a a 0x30
push a
set b 0
jmp :remainder

sub10:
add d d -10
add b b 1

remainder:
gt c 10 d
jf c :sub10

set d b
jt d :div10

output:
pop a
out a
jt a :output
