// c++ -O2 solve.cpp -o solve
// Generated with Duet https://github.com/paiv/aoc2017
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint32_t u32;
typedef int64_t s64;


static s64 _snd;

void SND(s64 x) {
    _snd = x;
}

void RCV(s64& x) {
    if (x > 0) {
        x = _snd;

        // part1:
        printf("%lld\n", _snd);
        exit(0);
    }
}

int main(int argc, char const *argv[]) {
    s64 ra = 0, rb = 0, rf = 0, ri = 0, rp = 0;
    ri = 31;
    ra = 1;
    rp *= 17;
    // if (rp > 0) {
    //     goto_r rp;
    // }
    do {
        ra *= 2;
        ri += -1;
    } while (ri > 0);
    ra += -1;
    ri = 127;
    rp = 622;
    do {
        rp *= 8505;
        rp %= ra;
        rp *= 129749;
        rp += 12345;
        rp %= ra;
        rb = rp;
        rb %= 10000;
        SND(rb);
        ri += -1;
    } while (ri > 0);
    if (ra > 0) {
        goto ln23;
    }
    ln21:
    do {
        RCV(rb);
    } while (rb > 0);
    ln23:
    rf = 0;
    ri = 126;
    RCV(ra);
    do {
        RCV(rb);
        rp = ra;
        rp *= -1;
        rp += rb;
        if (rp > 0) {
            goto ln34;
        }
        SND(ra);
        ra = rb;
        if (1 > 0) {
            goto ln36;
        }
    ln34:
        SND(rb);
        rf = 1;
    ln36:
        ri += -1;
    } while (ri > 0);
    SND(ra);
    if (rf > 0) {
        goto ln23;
    }
    if (ra > 0) {
        goto ln21;
    }

    puts("poop\n");

    return 0;
}
