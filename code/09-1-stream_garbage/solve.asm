; synacor vm

    jmp :input

start:
    eq c a '<'
    jt c :garbage

    eq c a '{'
    jf c :grp2
    add b b 1
    add d d b

grp2:
    eq c a '}'
    jf c :input
    add b b -1
    jmp :input

garbage:
    in a
    eq c a '!'
    jf c :garb2
    in a
    jmp :garbage
garb2:
    eq c a '>'
    jf c :garbage

input:
    in a
    eq c a 10
    jf c :start


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
    ; ret

memory:
