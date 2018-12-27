from . import assembler as asm
from . import generators
from . import vm


class DuetError(Exception):
    pass


class BaseDuet:
    def __init__(self):
        self.asm = self._assembler()
        self.image = None

    def load(self, fp):
        self.asm.load(fp)

    def compile(self):
        self.image, errors = self.asm.compile()
        if errors:
            raise DuetError(errors)

    def emit(self, output=None):
        if not self.image:
            self.compile()

        gen = self._generator()
        return gen.emit(self.image, output=output)

    def run(self):
        if not self.image:
            self.compile()

        vm = self._virtual_machine(self.image)
        vm.run()
        return vm

    def _assembler(self):
        return asm.Assembler()

    def _virtual_machine(self, image):
        return vm.DuetVM(image)

    def _generator(self):
        raise NotImplementedError()


class Duet(BaseDuet):
    def _generator(self):
        return generators.GeneratorPy()


class DuetAsm(BaseDuet):
    def _generator(self):
        return generators.GeneratorCppDispatch()


class DuetC(BaseDuet):
    def _generator(self):
        return generators.GeneratorDisasm()


def assemble_files(files, outfile, generator=None, verbose=False):
    tds = DuetC()

    if generator:
        generator = generator.lower()
        if generator == 'c-asm':
            tds = DuetAsm()
        elif generator == 'py':
            tds = Duet()

    for fp in files:
        tds.load(fp)

    tds.emit(output=outfile)
