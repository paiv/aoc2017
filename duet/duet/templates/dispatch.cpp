// c++ -std=c++11 -O2 solve.cpp -o solve
// Generated with Duet https://github.com/paiv/aoc2017
#include <stdint.h>
#include <stdio.h>


typedef uint32_t u32;
typedef int64_t s64;


typedef enum opcodes {
    {%- for name in instructions %}
    {{name}},
    {%- endfor %}
} opcodes;


typedef enum registers {
    {% for name in register_names %}r{{name}}{% if not loop.last %}, {% endif %}{% endfor %}
} registers;


static inline void
dispatch(const s64* instr, s64* regs) {
    switch (instr[0]) {
        {%- if 'addi' in instructions %}
        case addi:
            regs[instr[1]] += instr[2];
            break;
        {%- endif %}
        {%- if 'addr' in instructions %}
        case addr:
            regs[instr[1]] += regs[instr[2]];
            break;
        {%- endif %}
        {%- if 'jgii' in instructions %}
        case jgii:
            if (instr[1] > 0) {
                regs[rip] += instr[2] - 1;
            }
            break;
        {%- endif %}
        {%- if 'jgir' in instructions %}
        case jgir:
            if (instr[1] > 0) {
                regs[rip] += regs[instr[2]] - 1;
            }
            break;
        {%- endif %}
        {%- if 'jgri' in instructions %}
        case jgri:
            if (regs[instr[1]] > 0) {
                regs[rip] += instr[2] - 1;
            }
            break;
        {%- endif %}
        {%- if 'jgrr' in instructions %}
        case jgrr:
            if (regs[instr[1]] > 0) {
                regs[rip] += regs[instr[2]] - 1;
            }
            break;
        {%- endif %}
        {%- if 'modi' in instructions %}
        case modi:
            regs[instr[1]] %= instr[2];
            break;
        {%- endif %}
        {%- if 'modr' in instructions %}
        case modr:
            regs[instr[1]] %= regs[instr[2]];
            break;
        {%- endif %}
        {%- if 'muli' in instructions %}
        case muli:
            regs[instr[1]] *= instr[2];
            break;
        {%- endif %}
        {%- if 'mulr' in instructions %}
        case mulr:
            regs[instr[1]] *= regs[instr[2]];
            break;
        {%- endif %}
        {%- if 'rcv' in instructions %}
        case rcv:
            if (regs[instr[1]]) {
                regs[instr[1]] = regs[rsnd];
            }
            break;
        {%- endif %}
        {%- if 'seti' in instructions %}
        case seti:
            regs[instr[1]] = instr[2];
            break;
        {%- endif %}
        {%- if 'setr' in instructions %}
        case setr:
            regs[instr[1]] = regs[instr[2]];
            break;
        {%- endif %}
        {%- if 'sndi' in instructions %}
        case sndi:
            regs[rsnd] = instr[1];
            break;
        {%- endif %}
        {%- if 'sndr' in instructions %}
        case sndr:
            regs[rsnd] = regs[instr[1]];
            break;
        {%- endif %}
    }
}


static const s64
program[][3] = {
    {%- for line in program %}
    { {{- instructions[line[0]] }}, {% for x in line[1:] %}{{x}}{% if not loop.last %}, {% endif %}{% endfor -%} },
    {%- endfor %}
};


int main(int argc, char const *argv[]) {
    const u32 progn = sizeof(program) / sizeof(program[0]);
    //          {% for name in register_names %}{{name}}, {% endfor %}
    s64 regs[{{ registers|length }}] = { {%- for x in registers %}{{x}}{% if not loop.last %}, {% endif %}{% endfor -%} };

    for (u32 ip = {{ip}}; ip >= 0 && ip < progn; ip++) {
        regs[rip] = ip;
        dispatch(program[ip], regs);
        ip = regs[rip];
    }

    printf("%lld\n", regs[rsnd]);

    return 0;
}
