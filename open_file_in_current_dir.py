import sublime
import sublime_plugin
import os


class OpenFileInCurrentDirectoryCommand(sublime_plugin.WindowCommand):
    current_files = None

    def run(self):
        current = self.window.active_view().file_name()

        if current:
            self.select_file(current)

        else:
            message = "You must save the file before it has a directory"
            sublime.status_message(message)

    def select_file(self, target):
        self.current_files = self.files(target)
        self.window.show_quick_panel(self.current_files, self.switch_to)

    def switch_to(self, index):
        if index < 0:
            return

        selected = self.current_files[index][1]

        if os.path.isdir(selected):
            self.select_file(selected)
        else:
            self.window.open_file(selected)

    def files(self, current):
        base_dir = current if os.path.isdir(current) else os.path.dirname(current)
        paths = os.listdir(base_dir)

        full = lambda p: "%s/%s" % (base_dir, p)

        files = [[path, full(path)] for path in paths]
        files.insert(0, ["..", os.path.dirname(base_dir)])
        return files
