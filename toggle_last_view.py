import sublime
import sublime_plugin


class ViewToggler(object):
  _instance = None

class ToggleLastViewListener(sublime_plugin.EventListener):
  def on_deactivated(self, view):
    view.window().run_command("toggle_last_view", { "view": view })


class ToggleLastViewCommand(sublime_plugin.WindowCommand):
  def __init__(self, window):
    sublime_plugin.WindowCommand.__init__(self, window)
    self.lastView = None

  def run(self, view=None):
    if view:
      sublime.status_message("SETTING")
      self.lastView = view
    else:
      if self.lastView:
        sublime.status_message("FOOOO")
        self.window.focus_view(view)
      else:
        sublime.status_message("ARG")
