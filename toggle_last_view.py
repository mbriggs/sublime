import sublime_plugin


class ToggleLastViewListener(sublime_plugin.EventListener):
    deactivated = None

    def on_deactivated(self, view):
        self.deactivated = view

    def on_activated(self, view):
        if (self.deactivated is not None) and (self.deactivated != view):
            ToggleLastViewCommand.last_view = self.deactivated


class ToggleLastViewCommand(sublime_plugin.WindowCommand):
    last_view = None

    def run(self):
        prev = self.last_view
        if prev:
            self.window.focus_view(self.last_view)
