import sublime
import sublime_plugin
import re


class AddToGlobalsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # word = self.current_word()
        if self.no_global():
            self.add_global_declaration(edit)
        else:
            self.open_global_declaration()

    def add_global_declaration(self, edit):
        self.view.insert(edit, self.start_of_buffer(), "/*global ")
    # def open_global_declaration(self):

    def current_word(self):
        pos = self.view.sel()[0]
        word_pos = self.view.word(pos)
        return self.view.substr(word_pos)

    def no_global(self):
        return not re.match('^/\*global ', self.first_line())

    def first_line(self):
        line = self.view.line(self.start_of_buffer())
        return self.view.substr(line)

    def start_of_buffer(self):
        return sublime.Region(0, 0)
