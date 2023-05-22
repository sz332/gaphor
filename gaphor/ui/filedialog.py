"""This module has a generic file dialog functions that are used to open or
save files."""

from __future__ import annotations

import sys
from pathlib import Path

from gi.repository import Gio, Gtk

from gaphor.i18n import gettext

GAPHOR_FILTER = [(gettext("All Gaphor Models"), "*.gaphor", "application/x-gaphor")]


def new_filter(name, pattern, mime_type=None):
    f = Gtk.FileFilter.new()
    f.set_name(name)
    f.add_pattern(pattern)
    if mime_type and sys.platform != "win32":
        f.add_mime_type(mime_type)
    return f


def new_filters(filters):
    store = Gio.ListStore.new(Gtk.FileFilter)
    for name, pattern, mime_type in filters:
        store.append(new_filter(name, pattern, mime_type))
    store.append(new_filter(gettext("All Files"), "*"))
    return store


def open_file_dialog(title, handler, parent=None, dirname=None, filters=None) -> None:
    dialog = Gtk.FileDialog.new()
    dialog.set_title(title)

    if dirname:
        dialog.set_initial_folder(Gio.File.parse_name(dirname))

    if filters:
        dialog.set_filters(new_filters(filters))

    def response(dialog, result):
        files = dialog.open_multiple_finish(result)
        handler([Path(f.get_path()) for f in files])

    dialog.open_multiple(parent=parent, cancellable=None, callback=response)


def save_file_dialog(
    title,
    handler,
    parent=None,
    filename=None,
    extension=None,
    filters=None,
) -> Gtk.FileChooser:
    dialog = Gtk.FileDialog.new()

    if filename:
        dialog.set_initial_file(Gio.File.parse_name(str(filename)))

    if filters:
        dialog.set_filters(new_filters(filters))

    def response(dialog, result):
        filename = Path(dialog.save_finish(result).get_path())
        if extension and filename.suffix != extension:
            filename = filename.with_suffix(extension)
            if filename.exists():
                dialog.set_initial_file(Gio.File.parse_name(str(filename)))
                dialog.save(parent=parent, cancellable=None, callback=response)
                return
        handler(filename)

    dialog.save(parent=parent, cancellable=None, callback=response)
    return dialog
