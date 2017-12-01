; synacor vm

set h :memory

in a
push a
wmem h a

input:
in b
add h h 1
wmem h b

eq e b 10
jf e :compare1
pop b

compare1:
eq c a b
jf c :skip
add a a -'0'
add d d a

skip:
set a b
jf e :input

; part 1
call :printdecimal

out ' '

; part 2
set a :memory
not a a
add a a 1
add d h a

; set b 0
div2:
add b b 1
add a b b
eq c a d
jf c :div2

set d 0
set f :memory
add b b f
jmp :bounds2

compare2:
rmem a f
rmem c b

eq c a c
jf c :skip2
add a a -'0'
add d d a

skip2:

add b b 1
eq c b h
jf c :halfbounds
set b :memory
halfbounds:
add f f 1
bounds2:
eq c f h
jf c :compare2


printdecimal:
push 0

print10:
mod a d 10
add a a '0'
push a

div10:
set b 0
jmp :remainder10

sub10:
add d d -10
add b b 1

remainder10:
gt c 10 d
jf c :sub10

set d b
jt d :print10

output:
pop a
out a
jt a :output
ret

memory:
