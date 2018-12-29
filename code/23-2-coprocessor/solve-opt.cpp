// c++ -O2 solve.cpp -o solve
// Generated with Duet https://github.com/paiv/aoc2017
#include <stdint.h>
#include <stdio.h>

typedef uint32_t u32;
typedef int64_t s64;


int main(int argc, char const *argv[]) {
    s64 ra = 1, rb = 0, rc = 0, rd = 0, re = 0, rf = 0, rg = 0, rh = 0;
    rb = 65;
    rc = rb;
    if (!ra) {
        goto ln8;
    }

    rb *= 100;
    rb += 100000;
    rc = rb;
    rc += 17000;
ln8:
    rf = 1;
    rd = 2;
    do {
        // re = 2;
        re = rb / rd;
        do {
            if (rd * re == rb) {
                rf = 0;
            }
            // re += 1;
            re = rb;
        } while (re != rb);
        rd += 1;
    } while (rd != rb);

    if (!rf) {
        rh += 1;
    }
    rg = rb;
    rg -= rc;
    if (rb == rc) {
        goto ln32;
    }
    rb += 17;
    goto ln8;
ln32:

    printf("%lld\n", rh);

    return 0;
}
