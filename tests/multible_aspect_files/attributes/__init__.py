from PRAGMAR.core_aspects.pragmar import ap
from PRAGMAR.util import import_all_from_package
from tests.multible_aspect_files.gen.classes import Def
from tests.multible_aspect_files.grammar import gen_grammar


def gen_attributes():
    gen_grammar()
    with ap.define_attributes(Def):
        import_all_from_package(__name__, __path__)