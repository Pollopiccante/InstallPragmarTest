from tests.multible_aspect_files.gen.classes import Def
from tests.multible_aspect_files.gen.nodes import SomeInnerNode


@Def.SomeInnerNode
def run_cyan(node: SomeInnerNode) -> str:
    return "RUN CYAN?!?!?!"