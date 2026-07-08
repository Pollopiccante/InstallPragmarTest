import types

from PRAGMAR.new_tree import GrammarBuilder
from PRAGMAR.decorators import def_grammar


@def_grammar
def gen_grammar(grammar: GrammarBuilder):

    (grammar.Head("Video")
     .Field(field_name="frames", field_type="Image", is_list=True)
     .Field(field_name="filters", field_type="Filter", is_list=True)
     .Field(field_name="save_file_path", field_type=str)
     .Field(field_name="video_name", field_type=str))

    (grammar.Head("Image")
     .Field(field_name="width", field_type=int)
     .Field(field_name="height", field_type=int)
     .Field(field_name="image_file_path", field_type=str))

    (grammar.Head("Filter")
     .Field(field_name="range", field_type="ApplicableRange")
     .Field(field_name="mod", field_type="Modificator"))

    (grammar.Head("ApplicableRange")
     .Field(field_name="windows", field_type="Window", is_list=True))

    (grammar.Head("Window")
     .Field(field_name="start_frame", field_type=int)
     .Field(field_name="end_frame", field_type=int))

    (grammar.Head("Modificator")
     .Field(field_name="mod_name", field_type=str)
     .Field(field_name="mod_id", field_type=int))