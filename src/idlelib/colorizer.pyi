from _tkinter import Tcl_Obj
from collections.abc import Generator, Iterable
from idlelib.config import idleConf as idleConf
from idlelib.delegator import Delegator as Delegator
from re import Match, Pattern
from tkinter import Event, Misc, Text

DEBUG: bool

def any(name: str, alternates: Iterable[str]) -> str: ...
def make_pat() -> Pattern[str]: ...

prog: Pattern[str]
idprog: Pattern[str]
prog_group_name_to_tag: dict[str, str]

def matched_named_groups(
    re_match: Match[str],
) -> Generator[tuple[str, str]]: ...
def color_config(text: Text) -> None: ...

class ColorDelegator(Delegator):
    prog: Pattern[str]
    idprog: Pattern[str]
    def __init__(self) -> None: ...
    after_id: None
    allow_colorizing: bool
    stop_colorizing: bool
    colorizing: bool
    def init_state(self) -> None: ...
    def setdelegate(self, delegate: Delegator) -> None: ...  # type: ignore[override]
    def config_colors(self) -> None: ...
    tagdefs: dict[str, dict[str, str | None]]
    def LoadTagDefs(self) -> None: ...
    def insert(
        self,
        index: str,
        chars: str,
        tags: str | None = ...,
    ) -> None: ...
    def delete(self, index1: str, index2: str | None = ...) -> None: ...
    def notify_range(self, index1: str, index2: str | None = ...) -> None: ...
    def close(self) -> None: ...
    def toggle_colorize_event(
        self,
        event: Event[Misc] | None = ...,
    ) -> str: ...
    def recolorize(self) -> None: ...
    def recolorize_main(self) -> None: ...
    def removecolors(self) -> None: ...
    def _add_tags_in_section(self, chars: str, head: str) -> None: ...
    def _add_tag(
        self,
        start: int,
        end: int,
        head: str,
        matched_group_name: str,
    ) -> None: ...

    # tag_add = Text.tag_add
    def tag_add(
        self,
        tagName: str,
        index1: Tcl_Obj | str | float | Misc,
        *args: Tcl_Obj | str | float | Misc,
    ) -> None: ...
