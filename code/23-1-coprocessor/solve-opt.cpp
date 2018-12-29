// c++ -O2 solve.cpp -o solve
// Generated with Duet https://github.com/paiv/aoc2017
#include <stdint.h>
#include <stdio.h>

typedef uint32_t u32;
typedef int64_t s64;

u32 _mul;
s64 MUL(s64 x, s64 y) {
    _mul++;
    return x * y;
}

int main(int argc, char const *argv[]) {
    s64 ra = 0, rb = 0, rc = 0, rd = 0, re = 0, rf = 0, rg = 0, rh = 0;
    rb = 65;
    rc = rb;
    if (ra) {
        goto ln4;
    }
    if (1) {
        goto ln8;
    }
    ln4:
    // rb *= 100;
    rb = MUL(rb, 100);
    rb += 100000;
    rc = rb;
    rc += 17000;
    ln8:
    rf = 1;
    rd = 2;
    do {
        re = 2;
        do {
            rg = rd;
            // rg *= re;
            rg = MUL(rg, re);
            rg -= rb;
            if (rg) {
                goto ln16;
            }
            rf = 0;
    ln16:
            re += 1;
            rg = re;
            rg -= rb;
        } while (rg);
        rd += 1;
        rg = rd;
        rg -= rb;
    } while (rg);
    if (rf) {
        goto ln26;
    }
    rh += 1;
    ln26:
    rg = rb;
    rg -= rc;
    if (rg) {
        goto ln30;
    }
    if (1) {
        goto ln32;
    }
    ln30:
    rb += 17;
    if (1) {
        goto ln8;
    }
ln32:
    printf("%d\n", _mul);

    return 0;
}
