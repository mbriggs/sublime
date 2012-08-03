import sublime_plugin


class ToggleLastViewListener(sublime_plugin.EventListener):
    def on_deactivated(self, view):
        if view.file_name():
            ToggleLastViewCommand.previous_file = view.file_name()


class ToggleLastViewCommand(sublime_plugin.WindowCommand):
    previous_file = None

    def run(self):
        prev = self.previous_file
        if prev:
            self.window.open_file(prev)
