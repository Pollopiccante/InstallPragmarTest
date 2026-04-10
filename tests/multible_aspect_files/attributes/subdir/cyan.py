from tests.multible_aspect_files.gen.classes import SomeInnerNode
from tests.multible_aspect_files.gen.classes import Def

print("CYAN")

my_aspect = Def.create_aspect("my_cyan_aspect")

@my_aspect.SomeInnerNode
def run_cyan(node: SomeInnerNode) -> str:
    return "RUN CYAN?!?!?!"