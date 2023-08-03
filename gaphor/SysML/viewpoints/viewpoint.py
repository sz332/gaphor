from gaphor.core.modeling.properties import attribute

from gaphor.diagram.presentation import (
    Classified,
    ElementPresentation
)
from gaphor.diagram.shapes import (
    Box,
    Text,
    draw_border
)

from gaphor.diagram.support import represents
from gaphor.diagram.text import FontStyle, FontWeight
from gaphor.SysML.sysml import Stakeholder, Viewpoint

from gaphor.UML.recipes import stereotypes_str

from gaphor.core.styling.declarations import TextAlign

@represents(Viewpoint)
class ViewpointItem(Classified, ElementPresentation[Viewpoint]):
    def __init__(self, diagram, id=None):
        super().__init__(diagram, id)

        self.watch(
            "subject[NamedElement].name"
        ).watch(
            "subject[NamedElement].namespace.name"
        ) .watch(
            "subject[Classifier].isAbstract", self.update_shapes
        )

    def update_shapes(self, event=None):
        self.shape = Box(
            Box(
                Text(
                    text=lambda: stereotypes_str(
                        self.subject, [self.diagram.gettext("viewpoint")]
                    ),
                    style={
                        "text-align": TextAlign.CENTER
                    }
                ),
                Text(
                    text=lambda: self.subject.name or "",
                    style={
                        "font-weight": FontWeight.BOLD,
                        "text-align": TextAlign.CENTER,
                        "font-style": FontStyle.ITALIC if self.subject and self.subject.isAbstract 
                        else FontStyle.NORMAL,
                    },
                ),
                style={
                    "padding": (4, 4, 4, 4)
                },
            ),
            draw=draw_border
        )