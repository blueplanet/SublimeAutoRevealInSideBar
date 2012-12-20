import sublime
import sublime_plugin
 
class AutoRevealInSideBar(sublime_plugin.EventListener):
    def on_activated(self, view):
        if view != None:
            view.window().run_command("reveal_in_side_bar")