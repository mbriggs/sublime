import sublime_plugin


previous_file = "foo"


class ToggleLastViewListener(sublime_plugin.EventListener):
    def on_deactivated(self, view):
        print user.previous_file


class ToggleLastViewCommand(sublime_plugin.WindowCommand):
    def run(self):
        prev = self.window.settings().get("previous_file")
        if prev:
            self.window.open_file(prev)
