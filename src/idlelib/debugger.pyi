import bdb
import reprlib
from idlelib import macosx as macosx, rpc as rpc
from idlelib.debugger_r import IdbProxy
from idlelib.filelist import FileList
from idlelib.pyshell import PyShellEditorWindow
from idlelib.scrolledlist import ScrolledList as ScrolledList
from idlelib.window import ListedToplevel as ListedToplevel
from tkinter import (
    BaseWidget,
    BooleanVar,
    Button,
    Canvas,
    Checkbutton,
    Event,
    Frame,
    Label,
    Misc,
    Scrollbar,
    Tk,
)
from types import CodeType, FrameType, TracebackType
from typing import Any

class Idb(bdb.Bdb):
    gui: Debugger
    def __init__(self, gui: Debugger) -> None: ...
    def user_line(self, frame: FrameType) -> None: ...
    def user_exception(
        self,
        frame: FrameType,
        info: tuple[type[BaseException], BaseException, TracebackType],
    ) -> None: ...
    def in_rpc_code(self, frame: FrameType) -> bool: ...

class Debugger:
    vstack: BooleanVar | None
    vsource: BooleanVar | None
    vlocals: BooleanVar | None
    vglobals: BooleanVar | None
    pyshell: PyShellEditorWindow
    idb: IdbProxy | None
    frame: FrameType | None
    interacting: int
    nesting_level: int
    def __init__(
        self,
        pyshell: PyShellEditorWindow,
        idb: IdbProxy | None = ...,
    ) -> None: ...
    def run(
        self,
        *args: str | CodeType | dict[str, object] | None,
    ) -> None: ...
    stackviewer: StackViewer
    def close(self, event: Event[Misc] | None = ...) -> None: ...
    flist: FileList
    root: Tk
    top: ListedToplevel
    bframe: Frame
    buttons: list[Button]
    bcont: Button
    bstep: Button
    bnext: Button
    bret: Button
    cframe: Frame
    bstack: Checkbutton
    bsource: Checkbutton
    blocals: Checkbutton
    bglobals: Checkbutton
    status: Label
    error: Label
    errorbg: str
    fstack: Frame
    flocals: Frame
    fglobals: Frame
    def make_gui(self) -> None: ...
    def interaction(
        self,
        message: str,
        frame: FrameType,
        info: (
            tuple[type[BaseException], BaseException, TracebackType] | None
        ) = ...,
    ) -> None: ...
    def sync_source_line(self) -> None: ...
    def cont(self) -> None: ...
    def step(self) -> None: ...
    def next(self) -> None: ...
    def ret(self) -> None: ...
    def quit(self) -> None: ...
    def abort_loop(self) -> None: ...
    def show_stack(self) -> None: ...
    def show_source(self) -> None: ...
    def show_frame(self, stackitem: tuple[FrameType, int]) -> None: ...
    localsviewer: NamespaceViewer
    globalsviewer: NamespaceViewer
    def show_locals(self) -> None: ...
    def show_globals(self) -> None: ...
    def show_variables(self, force: int = ...) -> None: ...
    def set_breakpoint_here(self, filename: str, lineno: int) -> None: ...
    def clear_breakpoint_here(self, filename: str, lineno: int) -> None: ...
    def clear_file_breaks(self, filename: str) -> None: ...
    def load_breakpoints(self) -> None: ...

class StackViewer(ScrolledList):
    flist: FileList
    gui: Debugger
    stack: list[tuple[FrameType, int]]
    def __init__(
        self,
        master: BaseWidget,
        flist: FileList,
        gui: Debugger,
    ) -> None: ...
    def load_stack(
        self,
        stack: list[tuple[FrameType, int]],
        index: int | None = ...,
    ) -> None: ...
    def popup_event(self, event: Event[Misc] | None) -> str | None: ...
    def fill_menu(self) -> None: ...
    def on_select(self, index: int) -> None: ...
    def on_double(self, index: int) -> None: ...
    def goto_source_line(self) -> None: ...
    def show_stack_frame(self) -> None: ...
    def show_source(self, index: int) -> None: ...

class NamespaceViewer:
    master: BaseWidget
    title: str
    repr: reprlib.Repr
    frame: Frame
    label: Label
    vbar: Scrollbar
    canvas: Canvas
    subframe: Frame
    sfid: str
    def __init__(
        self,
        master: BaseWidget,
        title: str,
        dict: dict[str, Any] | None = ...,
    ) -> None: ...
    def load_dict(
        self,
        dict: dict[str, Any],
        force: int = ...,
        rpc_client: rpc.RPCClient | None = ...,
    ) -> None: ...
    dict: dict[str, Any]
    def close(self) -> None: ...
