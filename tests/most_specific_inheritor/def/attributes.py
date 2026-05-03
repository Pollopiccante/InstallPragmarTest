from tests.most_specific_inheritor.gen.nodes import A, B, C, D
from tests.most_specific_inheritor.gen.classes import Def

@Def.A.B.C.D
def test(node: A) -> str:
    return "Inherited from A"

@Def.B.C.D
def test(node: B) -> str:
    return "Inherited from B"

@Def.C.D
def test(node: C) -> str:
    return "Inherited from C"

@Def.D
def test(node: D) -> str:
    return "Inherited from D"
