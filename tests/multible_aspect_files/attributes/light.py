from tests.multible_aspect_files.gen.classes import Def
from tests.multible_aspect_files.gen.nodes import SomeInnerNode

print("LIGHT")

my_aspect = Def.create_aspect("my_light_aspect")

@my_aspect.SomeInnerNode
def run_light(node: SomeInnerNode) -> str:
    return "WALK IN THE LIGHT!"