import sublime
import sublime_plugin
import re

"""
    ___       __    __   __           ________      __          __
   /   | ____/ /___/ /  / /_____     / ____/ /___  / /_  ____ _/ /____
  / /| |/ __  / __  /  / __/ __ \   / / __/ / __ \/ __ \/ __ `/ / ___/
 / ___ / /_/ / /_/ /  / /_/ /_/ /  / /_/ / / /_/ / /_/ / /_/ / (__  )
/_/  |_\__,_/\__,_/   \__/\____/   \____/_/\____/_.___/\__,_/_/____/

JSHint and JSLint will look for a magic globals comment at the top of a js file.
This plugin will add the word at the cursor to that comment, as well as the
comment (if its not there yet)

usage
=====

I use vintage, so I went for ,g in normal mode as my key mapping


  {
    "keys": [",", "g"],
    "command": "add_to_globals",
    "context": [{"key": "setting.command_mode"}]
  }


MIT License
"""


class AddToGlobalsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.no_global():
            start = self.first_line().begin()
            self.view.insert(edit, start, "/*global \n")
        else:
            opened = re.sub('\*/', '', self.first_line_text())
            self.view.replace(edit, self.first_line(), opened)

        new_global = '%s */' % self.current_word()
        self.view.insert(edit, self.first_line().end(), new_global)

    def current_word(self):
        pos = self.view.sel()[0]
        word_pos = self.view.word(pos)
        return self.view.substr(word_pos)

    def no_global(self):
        return not re.match('^/\*global ', self.first_line_text())

    def first_line_text(self):
        return self.view.substr(self.first_line())

    def first_line(self):
        return self.view.line(self.start_of_buffer())

    def start_of_buffer(self):
        return sublime.Region(0, 0)
