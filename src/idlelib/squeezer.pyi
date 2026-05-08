from idlelib import macosx as macosx
from idlelib.config import idleConf as idleConf
from idlelib.pyshell import PyShellEditorWindow
from idlelib.textview import view_text as view_text
from idlelib.tooltip import Hovertip as Hovertip
from tkinter import Button, Event, Misc, Text
from typing import Literal

def count_lines_with_wrapping(s: str, linewidth: int = ...) -> int: ...

class ExpandingButton(Button):
    s: str
    tags: str | None
    numoflines: int
    squeezer: Squeezer
    editwin: PyShellEditorWindow
    text: Text
    base_text: Text
    is_dangerous: bool
    def __init__(
        self,
        s: str,
        tags: str | None,
        numoflines: int,
        squeezer: Squeezer,
    ) -> None: ...
    def set_is_dangerous(self) -> None: ...
    def expand(self, event: Event[Misc] | None = ...) -> str | None: ...
    def copy(self, event: Event[Misc] | None = ...) -> None: ...
    def view(self, event: Event[Misc] | None = ...) -> None: ...
    rmenu_specs: tuple[
        tuple[Literal["copy"], Literal["copy"]],
        tuple[Literal["view"], Literal["view"]],
    ]
    def context_menu_event(self, event: Event[Misc] | None) -> str: ...

class Squeezer:
    auto_squeeze_min_lines: int
    @classmethod
    def reload(cls) -> None: ...
    editwin: PyShellEditorWindow
    text: Text
    base_text: Text
    window_width_delta: int
    expandingbuttons: list[ExpandingButton]
    def __init__(self, editwin: PyShellEditorWindow) -> None: ...
    def count_lines(self, s: str) -> int: ...
    def squeeze_current_text(self) -> str: ...
