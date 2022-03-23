from libqtile.config import Click, Drag, Group, Key, Match, Screen

from hooks import *
from layouts import *

from widgets import MyWidgets
from groups import CreateGroups

from keybindings import MyKeyBindings, MyMouse
from default_keys import *

terminal = "terminator"

if __name__ in ["config", "__main__"]:
    obj_widgets = MyWidgets()
    obj_groups = CreateGroups()
    obj_keybindings = MyKeyBindings(terminal)
    obj_mouse = MyMouse()

    groups = obj_groups.init_groups()

    screens = obj_widgets.init_screen()
    main_widgets_list = obj_widgets.init_widgets_list()
    widgets_screen1 = obj_widgets.init_widgets_screen()

    keys = obj_keybindings.init_keybindings()
    mouse = obj_mouse.init_mouse()

for i, group in enumerate(groups, 1):
    name = group.name
    keys.append(Key([mod], str(i), lazy.group[name].toscreen(), desc=f"Switch to group {name}"))
    keys.append(Key([mod, shift], str(i), lazy.window.togroup(name, switch_group=True),
                    desc=f"Move focused window to group {name}"))

    keys.append(Key([mod, ctrl], "n", lazy.group[name].next_window()))
    keys.append(Key([mod, ctrl], "p", lazy.group[name].prev_window()))