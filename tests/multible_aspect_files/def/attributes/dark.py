from tests.multible_aspect_files.gen.classes import Def
from tests.multible_aspect_files.gen.nodes import SomeInnerNode

@Def.SomeInnerNode
def run_dark(node: SomeInnerNode) -> str:
    return "RUN IN THE DARK!"

