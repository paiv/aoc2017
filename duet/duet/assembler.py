import io
import re
from . import vm


class Assembler:

    class Input:
        _ids = 0

        def __init__(self, fp):
            self.fp = fp
            self.name = None
            if hasattr(fp, 'name'):
                self.name = fp.name
            if not self.name:
                self.name = '<{}>'.format(self._next_id())

        def _next_id(self):
            Assembler.Input._ids += 1
            return Assembler.Input._ids

        def __iter__(self):
            for line in self.fp:
                yield line

    def __init__(self):
        self.inputs = list()

    def load(self, fp):
        if isinstance(fp, str):
            fp = io.StringIO(fp)
        fin = Assembler.Input(fp)
        self.inputs.append(fin)

    def compile(self):
        instrs = 'add|jgz|jnz|mod|mul|rcv|set|snd|sub'
        rx = r'^ (?P<op>{instrs})\s+ (?: (?P<xi>-?\d+) | (?P<xr>[a-z])) (?:\s+ (?: (?P<yi>-?\d+) | (?P<yr>[a-z]) ))? $'.replace('{instrs}', instrs)
        rx = re.compile(rx, re.X)

        def opopt(op, x, y):
            if op in 'add mod mul set sub'.split():
                return op + 'ir'[isinstance(y, str)]
            elif op in 'snd'.split():
                return op + 'ir'[isinstance(x, str)]
            elif op in ('jgz', 'jnz'):
                return op[:2] + 'ir'[isinstance(x, str)] + 'ir'[isinstance(y, str)]
            elif op == 'rcv':
                return op
            else:
                raise NotImplementedError((op, x, y))

        program = list()
        regs = set()

        for src in self.inputs:
            for lineno, line in enumerate(src, 1):
                line = line.strip()
                if not line: continue

                m = rx.search(line)
                if not m:
                    error = '{}:{}  Invalid input {}'.format(src.name, lineno, repr(line))
                    return None, error

                elif m.group('op') is not None:
                    op = m.group('op')
                    x = int(m.group('xi')) if m.group('xi') else m.group('xr') or 0
                    y = int(m.group('yi')) if m.group('yi') else m.group('yr') or 0

                    op = opopt(op, x, y)
                    program.append((op, x, y))

                    if isinstance(x, str): regs.add(x)
                    if isinstance(y, str): regs.add(y)

        regs.discard('ip')
        regs.discard('snd')

        rnames = ['ip', 'snd'] + sorted(regs)
        regs = [0 for _ in rnames]

        def rid(x):
            if isinstance(x, str):
                return rnames.index(x)
            return x

        program = [(op, rid(x), rid(y)) for op, x, y in program]

        image = vm.Image(program, regs=regs, register_names=rnames)

        return image, None
