from PRAGMAR.new_tree import GrammarBuilder
from PRAGMAR.decorators import def_grammar


@def_grammar
def gen_grammar(grammar: GrammarBuilder):

    # everything is a frame
    (grammar.Head("Frame"))

    # modifications are frames and target frames
    (grammar.Head("Modification", head_super_type="Frame"))

    # single target modification types
    (grammar.Head("SingleTargetModification", head_super_type="Modification")
     .Field(field_type="Frame", field_name="target"))
    (grammar.Head("Position", head_super_type="SingleTargetModification")
     .Field(field_type=float, field_name="x")
     .Field(field_type=float, field_name="y"))
    (grammar.Head("Rotate", head_super_type="SingleTargetModification")
     .Field(field_type=float, field_name="roll")
     .Field(field_type=float, field_name="pitch")
     .Field(field_type=float, field_name="yaw"))
    (grammar.Head("Scale", head_super_type="SingleTargetModification")
     .Field(field_type=float, field_name="width")
     .Field(field_type=float, field_name="height"))
    (grammar.Head("Crop", head_super_type="SingleTargetModification")
     .Field(field_type=float, field_name="top")
     .Field(field_type=float, field_name="left")
     .Field(field_type=float, field_name="width")
     .Field(field_type=float, field_name="height"))
    (grammar.Head("Duration", head_super_type="SingleTargetModification")
     .Field(field_type=float, field_name="duration"))
    (grammar.Head("MoveTime", head_super_type="SingleTargetModification")
     .Field(field_type=int, field_name="offset"))

    # multi target modifications
    (grammar.Head("MultiTargetModification", head_super_type="Modification")
     .Field(field_type="Frame", field_name="targets", is_list=True))
    (grammar.Head("Stack", head_super_type="MultiTargetModification"))
    (grammar.Head("Sequence", head_super_type="MultiTargetModification"))
    (grammar.Head("Panel", head_super_type="MultiTargetModification")
     .Field(field_type=str, field_name="mode")) # wrap, horizontal, vertical
    (grammar.Head("Interpolation", head_super_type="MultiTargetModification")
     .Field(field_type="KeyFrame", field_name="keyframes", is_list=True))
    (grammar.Head("KeyFrame")
     .Field(field_type=int, field_name="time")
     .Field(field_type=str, field_name="attributes")) # attributes seperated by comma

    # resource input types
    (grammar.Head("ResourceInput", head_super_type="Frame")
     .Field(field_type=str, field_name="path"))
    (grammar.Head("Image", head_super_type="ResourceInput"))
    (grammar.Head("TextResource", head_super_type="ResourceInput"))
    (grammar.Head("Video", head_super_type="ResourceInput"))

    # direct input types
    (grammar.Head("DirectInput", head_super_type="Frame"))
    (grammar.Head("Text", head_super_type="DirectInput")
     .Field(field_type=str, field_name="input"))

    # templating system
    (grammar.Head("TemplateDef")
     .Field(field_type=str, field_name="id")
     .Field(field_type="Frame", field_name="root"))
    (grammar.Head("Template")
     .Field(field_type=str, field_name="id")
     .Field(field_type="Filling", field_name="fillings", is_list=True))
    (grammar.Head("Filling")
     .Field(field_type=str, field_name="id")
     .Field(field_type="Frame", field_name="input"))


    # example usage (no templating)

    """
    Stack(
        Duration<10, 5000>(    
            Video<evangelion.mp4>,
        )
        MoveTime<140>(
            Sequence(
                Duration<24>(
                    Image("myface.png")
                ),
                Duration<24>(
                    Image("myface_weird.png")
                )
            )
        ),
        Move<Transform<0,0,0,90,0,0>>(
            MoveTime<450>(
                Duration<24>(
                    Image("someFace.png")
                )
            )
        )
    )
    """

    # template definition, and usage as a frame
    """
    TemplateDef<id: "EvangelionIntro">
    (
        Stack(
            Duration<10, 5000>(    
                Video<evangelion.mp4>,
            )
            MoveTime<140>(
                Sequence(
                    Duration<24>(
                        Hole<id: "first_face">
                    ),
                    Duration<24>(
                        Image("myface_weird.png")
                    )
                )
            ),
            Move<Transform<0,0,0,90,0,0>>(
                MoveTime<450>(
                    Duration<24>(
                        Hole<id: "final_face">
                    )
                )
            )
        )
    )
    
    Panel(
        <Template id="EvangelionIntro">(
            <Filling id="first_face">(
                <Image path="tiger.png">
            ),
            <Filling id="final_face">(
                <Image path="lukeSkywalker.png">            
            )       
        )
        <Text input="What is This???">
    )
    
    
    """

# duration bracht modi: (cut_loop, cut_blank, stretch)
# cut_OPTION: take a part of the source video, the length depends on the duration,
#   cut_loop: if the source is shorter either loop the video to fill the gaps
#   cut_blank: or insert a blank frame

# stretch: slow down or speed up the source video to match the specified duration


# Rotation modes: Center / LeftTop / Custom = (Width, Height as parameters, formula allowed)