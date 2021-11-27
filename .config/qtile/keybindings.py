from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

from default_keys import *

OTHER = [([mod, alt], "a", "pavucontrol"),

    ([alt], space, "/home/batuhaninan/.config/rofi/launchers/slate/launcher.sh"),
    
    ([alt], "Print", "xfce4-screenshooter"),
    
    ([], "XF86AudioLowerVolume", "pactl set-sink-volume @DEFAULT_SINK@ -10%"),
    ([], "XF86AudioRaiseVolume", "pactl set-sink-volume @DEFAULT_SINK@ +10%"),
    ([], "XF86AudioMute", "pactl set-sink-mute @DEFAULT_SINK@ toggle"),
] 

class MyKeyBindings:

    def __init__(self, terminal):
        self.terminal = terminal
    
    def init_keybindings(self):

        defaults = [
            Key([mod], left, lazy.layout.left(), desc="Move focus to left"),
            Key([mod], right, lazy.layout.right(), desc="Move focus to right"),
            Key([mod], down, lazy.layout.down(), desc="Move focus down"),
            Key([mod], up, lazy.layout.up(), desc="Move focus up"),
            Key([mod], space, lazy.layout.next(), desc="Move window focus to other window"),

            Key([mod, shift], left, lazy.layout.shuffle_left(), desc="Move window to the left"),
            Key([mod, shift], right, lazy.layout.shuffle_right(), desc="Move window to the right"),
            Key([mod, shift], down, lazy.layout.shuffle_down(), desc="Move window down"),
            Key([mod, shift], up, lazy.layout.shuffle_up(), desc="Move window up"),

            Key([mod, ctrl], left, lazy.layout.grow_left(), desc="Grow window to the left"),
            Key([mod, ctrl], right, lazy.layout.grow_right(), desc="Grow window to the right"),
            Key([mod, ctrl], down, lazy.layout.grow_down(), desc="Grow window down"),
            Key([mod, ctrl], up, lazy.layout.grow_up(), desc="Grow window up"),
            Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

            Key([mod, shift], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
            Key([mod], "Return", lazy.spawn(self.terminal), desc="Launch terminal"),

            Key([mod], "z", lazy.spawn("nautilus --browser"), desc="Open window manager"),
            
            Key([mod], tab, lazy.next_layout(), desc="Toggle between layouts"),
            Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

            Key([mod, ctrl], "r", lazy.restart(), desc="Restart Qtile"),
            Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        ]

        for k in OTHER:
            modifier, key, command = k
            defaults.append(Key(modifier, key, lazy.spawn(command)))

        
        return defaults



class MyMouse:
   
    def __init__(self):
        ...

    def init_mouse(self):
        return [
            Drag([mod], "Button1", lazy.window.set_position_floating(),
                 start=lazy.window.get_position()),
            Drag([mod], "Button3", lazy.window.set_size_floating(),
                 start=lazy.window.get_size()),
            Click([mod], "Button2", lazy.window.bring_to_front())
            ]

