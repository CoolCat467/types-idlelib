from collections.abc import Container
from tkinter import Event, Listbox, Misc, StringVar, Toplevel
from tkinter.ttk import Button, Checkbutton, Entry, Frame

FUNCTION_KEYS: tuple[str, ...]
ALPHANUM_KEYS: tuple[str, ...]
PUNCTUATION_KEYS: tuple[str, ...]
WHITESPACE_KEYS: tuple[str, str, str]
EDIT_KEYS: tuple[str, str, str]
MOVE_KEYS: tuple[str, ...]
AVAILABLE_KEYS: tuple[str, ...]

def translate_key(key: str, modifiers: Container[str]) -> str: ...

class GetKeysDialog(Toplevel):
    keyerror_title: str
    parent: Misc
    action: str
    current_key_sequences: list[str]
    result: str
    key_string: StringVar
    modifier_vars: list[StringVar]
    advanced: bool
    def __init__(
        self,
        parent: Misc,
        title: str,
        action: str,
        current_key_sequences: list[str],
        *,
        _htest: bool = ...,
        _utest: bool = ...,
    ) -> None: ...
    def showerror(self, *args: Misc, **kwargs: Misc) -> None: ...
    frame: Frame  # type: ignore[assignment]
    button_ok: Button
    button_cancel: Button
    frame_keyseq_basic: Frame
    frame_controls_basic: Frame
    modifier_checkbuttons: dict[str, Checkbutton]
    list_keys_final: Listbox
    button_clear: Button
    frame_keyseq_advanced: Frame
    advanced_keys: Entry
    frame_help_advanced: Frame
    button_level: Button
    def create_widgets(self) -> None: ...
    modifiers: list[str]
    modifier_label: dict[str, str]
    def set_modifiers_for_platform(self) -> None: ...
    def toggle_level(self) -> None: ...
    def final_key_selected(self, event: Event[Misc] | None = ...) -> None: ...
    def build_key_string(self) -> None: ...
    def get_modifiers(self) -> list[str]: ...
    def clear_key_seq(self) -> None: ...
    def ok(self, event: Event[Misc] | None = ...) -> None: ...
    def cancel(self, event: Event[Misc] | None = ...) -> None: ...
    def keys_ok(self, keys: str) -> bool: ...
    def bind_ok(self, keys: str) -> bool: ...
