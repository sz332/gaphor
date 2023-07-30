"""The definition for the requirements section of the toolbox."""

from gaphor.core import gettext
from gaphor.diagram.diagramtoolbox import ToolDef, ToolSection, new_item_factory
from gaphor.SysML.viewpoints.stakeholder import StakeholderItem

from gaphor.SysML.sysml import Stakeholder

viewpoints = ToolSection(
    gettext("Viewpoints"),
    (
        ToolDef(
            "toolbox-stakeholder",
            gettext("Stakeholder"),
            "gaphor-requirement-symbolic",
            None,
            new_item_factory(StakeholderItem, Stakeholder)
        ),
        ToolDef(
            "toolbox-viewpoint",
            gettext("Viewpoint"),
            "gaphor-requirement-symbolic",
            None,
            None
        ),
        ToolDef(
            "toolbox-view",
            gettext("View"),
            "gaphor-requirement-symbolic",
            None,
            None
        )
    ),
)
