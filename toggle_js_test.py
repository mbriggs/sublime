import sublime
import sublime_plugin
import os
import re


class ProjectFiles(object):
    @staticmethod
    def find(self, file_matcher):
        directories = self.window().folders()
        return [os.path.join(dirname, file)
            for directory in directories
            for dirname, _, files in self.walk(directory)
            for file in filter(file_matcher, files)]

    @staticmethod
    def walk(self, directory, ignored_directories=[]):
        ignore = lambda dirname: dirname not in ['.git', 'vendor']
        for dir, dirnames, files in os.walk(directory):
            dirnames[:] = [dirname for dirname in filter(ignore, dirnames)]
            yield dir, dirnames, files


class CurrentFile(object):
    def matcher(self):
        m = self.implementation() if self.is_spec() else self.spec()
        return lambda file: file == m

    def implementation(self):
        re.sub('_spec.js$', '.js', self.file_name())

    def spec(self):
        re.sub('.js$', '_spec.js', self.file_name())

    def file_name(self):
        return sublime.active_window().active_view().file_name()

    def is_spec(self):
        re.match('_spec.js$', self.file_name())


class ToggleJavascriptTest(sublime_plugin.WindowCommand):
    def run(self):
        matcher = CurrentFile().matcher()

        ProjectFiles.find(matcher)
