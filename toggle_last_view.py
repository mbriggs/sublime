import sublime_plugin


class ToggleLastViewListener(sublime_plugin.EventListener):
    deactivated = None

    def on_deactivated(self, view):
        if view.file_name():
            self.deactivated = view.file_name()

    def on_activated(self, view):
        if (self.deactivated is not None) and (self.deactivated != view.file_name()):
            ToggleLastViewCommand.previous_file = self.deactivated


class ToggleLastViewCommand(sublime_plugin.WindowCommand):
    previous_file = None

    def run(self):
        prev = self.previous_file
        if prev:
            self.window.open_file(prev)
