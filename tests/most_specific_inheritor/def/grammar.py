from PRAGMAR.decorators import def_grammar
from PRAGMAR.tree import GrammarBuilder


@def_grammar
def gen_grammar(grammar: GrammarBuilder):
    (grammar.Head("A")
     .Field(field_name="under_A_1", field_type="B")
     .Field(field_name="under_A_2", field_type="B"))
    (grammar.Head("B")
     .Field(field_name="under_B_1", field_type="C")
     .Field(field_name="under_B_2", field_type="C"))
    (grammar.Head("C")
     .Field(field_name="under_C_1", field_type="D"))
    (grammar.Head("D")
     .Field(field_name="my_attribute", field_type=float))
