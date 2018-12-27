import io
import jinja2
from . import disasm
from . import vm


class BaseGenerator:
    templates_dir = 'templates'

    def emit(self, image, output):

        env = jinja2.Environment(
            loader=jinja2.PackageLoader(self.__module__, self.templates_dir)
        )

        tpl = env.get_template(self.template_name)

        model = self._transpile(image)

        if not output:
            output = io.StringIO()

        for text in tpl.generate(model):
            output.write(text)

        if hasattr(output, 'getvalue'):
            return output.getvalue()


class Generator(BaseGenerator):
    def _transpile(self, image):
        instr = sorted(set(line[0] for line in image.program))

        program = [(instr.index(line[0]), *line[1:]) for line in image.program]

        return dict(
            instructions=instr,
            program=program,
            registers=image.regs,
            register_names=image.register_names,
            ip=image.ip,
        )


class GeneratorPy(Generator):
    template_name = 'program.py'


class GeneratorCppDispatch(Generator):
    template_name = 'dispatch.cpp'


class GeneratorDisasm(BaseGenerator):
    template_name = 'program.cpp'

    def _transpile(self, image):
        dasm = disasm.DuetDisasm()
        program, regs = dasm.process(image)
        program = program.splitlines()

        return dict(
            registers=regs,
            program=program,
        )
