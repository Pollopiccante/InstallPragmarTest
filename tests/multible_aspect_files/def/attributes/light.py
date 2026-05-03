from tests.multible_aspect_files.gen.classes import Def
from tests.multible_aspect_files.gen.nodes import SomeInnerNode

@Def.SomeInnerNode
def run_light(node: SomeInnerNode) -> str:
    return "WALK IN THE LIGHT!"