from tests.multible_aspect_files.gen.classes import SomeInnerNode
from tests.multible_aspect_files.gen.classes import Def


print("DARK")

my_aspect = Def.create_aspect("my_dark_aspect")

@my_aspect.SomeInnerNode
def run_dark(node: SomeInnerNode) -> str:
    return "RUN IN THE DARK!"

