from idlelib.config import idleConf as idleConf
from idlelib.editor import EditorWindow
from re import Pattern
from tkinter import Event, Frame, Misc, Text

BLOCKOPENERS: set[str]

def get_spaces_firstword(
    codeline: str,
    c: Pattern[str] = ...,
) -> tuple[str, str]: ...
def get_line_info(codeline: str) -> tuple[int, str, str | bool]: ...

class CodeContext:
    UPDATEINTERVAL: int
    editwin: EditorWindow
    text: Text
    context_depth: int
    def __init__(self, editwin: EditorWindow) -> None: ...
    @classmethod
    def reload(cls) -> None: ...
    t1: str | None
    def __del__(self) -> None: ...
    cell00: Frame
    context: Text | None
    def toggle_code_context_event(
        self,
        event: Event[Misc] | None = ...,
    ) -> str: ...
    def get_context(
        self,
        new_topvisible: int,
        stopline: int = ...,
        stopindent: int = ...,
    ) -> tuple[list[tuple[int, int, str, str | bool]], int]: ...
    topvisible: int
    def update_code_context(self) -> None: ...
    def jumptoline(self, event: Event[Misc] | None = ...) -> None: ...
    def timer_event(self) -> None: ...
    def update_font(self) -> None: ...
    def update_highlight_colors(self) -> None: ...
