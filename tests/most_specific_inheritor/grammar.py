import os

from PRAGMAR.core_aspects.pragmar import ap

from PRAGMAR.tree import AllParentNode

# set core generation directory
AllParentNode.GEN_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "gen")

# define grammar
def gen_grammar():
    with ap.define_grammar():
        grammar_def = ap.create_grammar()
        (grammar_def.Head("A")
         .Field(field_name="under_A_1", field_type="B")
         .Field(field_name="under_A_2", field_type="B"))
        (grammar_def.Head("B")
         .Field(field_name="under_B_1", field_type="C")
         .Field(field_name="under_B_2", field_type="C"))
        (grammar_def.Head("C")
         .Field(field_name="under_C_1", field_type="D"))
        (grammar_def.Head("D")
         .Field(field_name="my_attribute", field_type=float))

if __name__ == "__main__":
    gen_grammar()