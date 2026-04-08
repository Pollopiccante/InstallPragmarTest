from PRAGMAR.core_aspects.pragmar import ap
from gen.classes import A, B, C, D
from gen.classes import Def


from grammar import gen_grammar


# define grammar
def gen_attributes():
    gen_grammar()

    # define aspects
    with ap.define_attributes(Def):
        my_aspect = Def.create_aspect("my_aspect")

        @my_aspect.A.B.C.D
        def test(node: A) -> str:
            return "Inherited from A"

        @my_aspect.B.C.D
        def test(node: B) -> str:
            return "Inherited from B"

        @my_aspect.C.D
        def test(node: C) -> str:
            return "Inherited from C"

        @my_aspect.D
        def test(node: D) -> str:
            return "Synthesized in D"

if __name__ == "__main__":
    gen_attributes()