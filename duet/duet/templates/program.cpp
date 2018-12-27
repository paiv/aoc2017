// c++ -O2 solve.cpp -o solve
// Generated with Duet https://github.com/paiv/aoc2017
#include <stdint.h>
#include <stdio.h>

typedef uint32_t u32;
typedef int64_t s64;


int main(int argc, char const *argv[]) {
    s64 {% for name, value in registers.items() %}{{name}} = {{value}}{% if not loop.last %}, {% endif %}{% endfor %};

    {%- for line in program %}
    {{line}}
    {%- endfor %}

    printf("%d\n", r0);

    return 0;
}
