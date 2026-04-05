from PRAGMAR.tree import *
import types
import typing


class Node(InnerNode):
    def __init__(self, ):
        super().__init__()
        self.type = "Node"
        # fields
    # attributes
    def meta_checker_fits_grammar_rule(self, rule: 'RuleNode') -> None:
        return self.attribute("fits_grammar_rule")(rule)
    def print_ast_depth(self) -> int:
        return self.attribute("depth")()
    def print_ast_print_tree(self, show_grammar_structure: 'None', show_attributes: 'None') -> str:
        return self.attribute("print_tree")(show_grammar_structure, show_attributes)
    def meta_checker_get_super_type(self, type: 'None') -> None:
        return self.attribute("get_super_type")(type)
    def meta_checker_get_rule_for_type(self, type: 'None') -> None:
        return self.attribute("get_rule_for_type")(type)
    def meta_checker_is_subtype_of(self, type: 'None', potential_super_type: 'None') -> None:
        return self.attribute("is_subtype_of")(type, potential_super_type)
    def meta_checker_get_all_subtypes_of_type(self, type: 'None') -> None:
        return self.attribute("get_all_subtypes_of_type")(type)
    def meta_checker_get_all_reachable_types_of_type(self, type: 'None') -> None:
        return self.attribute("get_all_reachable_types_of_type")(type)
    def gen_iterate_ancestors_of_type(self, type: 'str') -> List:
        return self.attribute("iterate_ancestors_of_type")(type)


class ASTNode(Node):
    def __init__(self, ):
        super().__init__()
        self.type = "ASTNode"
        # fields


class AllParent(Node):
    def __init__(self, Grammar: 'Grammar', Attributes: 'ListNode[Aspect]', ASTs: 'ListNode[ASTNode]'):
        super().__init__()
        self.type = "AllParent"
        # fields
        self.add_child("Grammar", Grammar)
        self.Grammar: 'Grammar' = Grammar
        self.add_child("Attributes", Attributes)
        self.Attributes: 'ListNode[Aspect]' = Attributes
        self.add_child("ASTs", ASTs)
        self.ASTs: 'ListNode[ASTNode]' = ASTs
    # attributes
    def meta_checker_get_super_type(self, type: 'None') -> None:
        return self.attribute("get_super_type")(type)
    def meta_checker_get_rule_for_type(self, type: 'None') -> None:
        return self.attribute("get_rule_for_type")(type)
    def meta_checker_is_subtype_of(self, type: 'None', potential_super_type: 'None') -> None:
        return self.attribute("is_subtype_of")(type, potential_super_type)
    def meta_checker_check_grammar(self) -> None:
        return self.attribute("check_grammar")()
    def gen_generate_class_helpers(self) -> None:
        return self.attribute("generate_class_helpers")()
    def gen_iterate_ancestors_of_type(self, type: 'str') -> List:
        return self.attribute("iterate_ancestors_of_type")(type)
    def gen_generate_node_helpers(self) -> None:
        return self.attribute("generate_node_helpers")()
# helper class, as the all parent is not created by the user
class APWrapper(AllParent):
    def __init__(self, ap):
        self.wrapped_ap = ap
        super().__init__(ap.children["Grammar"], ap.children["Attributes"], ap.children["ASTs"])


class Grammar(Node):
    def __init__(self, ClassNode: 'ClassNode', Rules: 'ListNode[Rule]'):
        super().__init__()
        self.type = "Grammar"
        # fields
        self.add_child("ClassNode", ClassNode)
        self.ClassNode: 'ClassNode' = ClassNode
        self.add_child("Rules", Rules)
        self.Rules: 'ListNode[Rule]' = Rules
    # attributes
    def meta_checker_check_grammar(self, tree_to_check: 'TreeNode') -> None:
        return self.attribute("check_grammar")(tree_to_check)
    def gen_generate_class_helpers(self) -> None:
        return self.attribute("generate_class_helpers")()


class Rule(Node):
    def __init__(self, head_type: 'str', head_super_type: 'str', Fields: 'ListNode[Field]'):
        super().__init__()
        self.type = "Rule"
        # fields
        self.head_type: 'str' = head_type
        self.head_super_type: 'str' = head_super_type
        self.add_child("Fields", Fields)
        self.Fields: 'ListNode[Field]' = Fields
    # attributes
    def meta_checker_get_all_fields(self) -> None:
        return self.attribute("get_all_fields")()


class Field(Node):
    def __init__(self, field_name: 'str', field_type: 'str'):
        super().__init__()
        self.type = "Field"
        # fields
        self.field_name: 'str' = field_name
        self.field_type: 'str' = field_type


class ClassNode(Node):
    def __init__(self, class_type: 'str', sub_classes: 'ListNode[ClassNode]'):
        super().__init__()
        self.type = "ClassNode"
        # fields
        self.class_type: 'str' = class_type
        self.add_child("sub_classes", sub_classes)
        self.sub_classes: 'ListNode[ClassNode]' = sub_classes


class Aspect(Node):
    def __init__(self, AttrDefinitionRootParts: 'ListNode[AttrDefinitionRootPart]', aspect_name: 'str'):
        super().__init__()
        self.type = "Aspect"
        # fields
        self.add_child("AttrDefinitionRootParts", AttrDefinitionRootParts)
        self.AttrDefinitionRootParts: 'ListNode[AttrDefinitionRootPart]' = AttrDefinitionRootParts
        self.aspect_name: 'str' = aspect_name


class AttrDefinitionPart(Node):
    def __init__(self, ):
        super().__init__()
        self.type = "AttrDefinitionPart"
        # fields
    # attributes
    def gen_get_aspect_name(self) -> None:
        return self.attribute("get_aspect_name")()


class ASTNode(Node):
    def __init__(self, ):
        super().__init__()
        self.type = "ASTNode"
        # fields


class SomeNode(ASTNode):
    def __init__(self, ):
        super().__init__()
        self.type = "SomeNode"
        # fields


class ASTListNode(ListNode):
    def __init__(self, ):
        super().__init__()
        self.type = "ASTListNode"
        # fields


class AttrDefinitionPartInner(AttrDefinitionPart):
    def __init__(self, sub_defs: 'ListNode[AttrDefinitionPart]'):
        super().__init__()
        self.type = "AttrDefinitionPartInner"
        # fields
        self.add_child("sub_defs", sub_defs)
        self.sub_defs: 'ListNode[AttrDefinitionPart]' = sub_defs


class AttrDefinitionValuePart(AttrDefinitionPart):
    def __init__(self, function: 'types.FunctionType'):
        super().__init__()
        self.type = "AttrDefinitionValuePart"
        # fields
        self.function: 'types.FunctionType' = function


class SomeLeafNode(SomeNode):
    def __init__(self, ):
        super().__init__()
        self.type = "SomeLeafNode"
        # fields
    # attributes
    def my_aspect_level_one_inherit(self) -> str:
        return self.attribute("level_one_inherit")()
    def my_aspect_level_two_inherit(self) -> str:
        return self.attribute("level_two_inherit")()


class SomeInnerNode(SomeNode):
    def __init__(self, child1: 'SomeNode', child2: 'SomeNode', context_value: 'str'):
        super().__init__()
        self.type = "SomeInnerNode"
        # fields
        self.add_child("child1", child1)
        self.child1: 'SomeNode' = child1
        self.add_child("child2", child2)
        self.child2: 'SomeNode' = child2
        self.context_value: 'str' = context_value


class AttrDefinitionRootPart(AttrDefinitionPartInner):
    def __init__(self, sub_defs: 'ListNode[AttrDefinitionPart]', attr_name: 'str'):
        super().__init__(sub_defs)
        self.type = "AttrDefinitionRootPart"
        # fields
        self.attr_name: 'str' = attr_name


class AttrDefinitionTypePart(AttrDefinitionPartInner):
    def __init__(self, sub_defs: 'ListNode[AttrDefinitionPart]', def_type: 'str'):
        super().__init__(sub_defs)
        self.type = "AttrDefinitionTypePart"
        # fields
        self.def_type: 'str' = def_type
    # attributes
    def gen_get_type_accessible_from(self) -> None:
        return self.attribute("get_type_accessible_from")()


class AttrDefinitionNamePart(AttrDefinitionPartInner):
    def __init__(self, sub_defs: 'ListNode[AttrDefinitionPart]', def_name: 'str'):
        super().__init__(sub_defs)
        self.type = "AttrDefinitionNamePart"
        # fields
        self.def_name: 'str' = def_name
    # attributes
    def gen_get_type_accessible_from(self) -> None:
        return self.attribute("get_type_accessible_from")()
