from PRAGMAR.decorators import def_run
from PRAGMAR.tree import AllParentNode

from tests.xml_parsing_example.gen.nodes import AllParentNode


@def_run
def run(ap: AllParentNode):
    xml_prefix = "/home/richard/Documents/Projects/PRAGMAR/InstallPragmarTest/tests/xml_parsing_example/"
    schema = "note.xsd"
    xml_file = "note.xml"

    ap.attribute("generate_xml_schema")(xml_prefix + schema, "my_namespace")
    tree = ap.attribute("add_xml")(xml_prefix + xml_file)

    res = tree.attribute("test_attribute")()
    assert res == "ABCD"
