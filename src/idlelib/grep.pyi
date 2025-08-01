from idlelib import searchengine as searchengine
from idlelib.filelist import FileList
from idlelib.iomenu import IOBinding
from idlelib.searchbase import SearchDialogBase as SearchDialogBase
from re import Pattern
from tkinter import BooleanVar, Entry, Event, Misc, StringVar, Text
from typing import Any

def grep(
    text: Text,
    io: IOBinding | None = ...,
    flist: FileList | None = ...,
) -> None: ...
def walk_error(msg: str) -> None: ...
def findfiles(folder: str, pattern: str, recursive: bool) -> None: ...

class GrepDialog(SearchDialogBase):
    title: str
    icon: str
    needwrapbutton: bool
    flist: FileList
    globvar: StringVar
    recvar: BooleanVar
    def __init__(
        self,
        root: Misc,
        engine: searchengine.SearchEngine,
        flist: FileList,
    ) -> None: ...
    def open(  # type: ignore[override]
        self,
        text: Text,
        searchphrase: str | None,
        io: IOBinding | None = ...,
    ) -> None: ...
    globent: Entry
    def create_entries(self) -> None: ...
    def create_other_buttons(self) -> None: ...  # type: ignore[override]
    def create_command_buttons(self) -> None: ...
    def default_command(self, event: Event[Any] | None = ...) -> None: ...
    def grep_it(self, prog: Pattern[str], path: str) -> None: ...
