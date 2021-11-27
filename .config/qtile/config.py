# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger


from hooks import *
from layouts import *

from widgets import MyWidgets
from groups import CreateGroups

from keybindings import MyKeyBindings, MyMouse
from default_keys import * 



#terminal = guess_terminal()
terminal = "terminator"


if __name__ in ["config", "__main__"]:
    obj_widgets       = MyWidgets()
    obj_groups        = CreateGroups()
    obj_keybindings   = MyKeyBindings(terminal)
    obj_mouse         = MyMouse()

    groups            = obj_groups.init_groups()

    screens           = obj_widgets.init_screen()
    main_widgets_list = obj_widgets.init_widgets_list()
    widgets_screen1   = obj_widgets.init_widgets_screen()

    keys = obj_keybindings.init_keybindings()
    mouse = obj_mouse.init_mouse()

print(groups)
for i, group in enumerate(groups, 1):
    name = group.name
    keys.append(Key([mod], str(i), lazy.group[name].toscreen(), desc=f"Switch to group {name}"))
    keys.append(Key([mod, shift], str(i), lazy.window.togroup(name, switch_group=True), desc=f"Move focused window to group {name}"))
    
    keys.append(Key([mod, ctrl], "n", lazy.group[name].next_window()))
    keys.append(Key([mod, ctrl], "p", lazy.group[name].prev_window()))

