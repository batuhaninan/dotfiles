import os
from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.config import Screen

from functions import PWA
from libqtile import qtile
from libqtile.log_utils import logger


_colors = {
    'bg':           '#282828',
    'bg-inactive':  '#525252',
    'fg':           '#88C0D0',
    'dark-red':     '#800000',
    'red':          '#ea6962',
    'dark-green':   '#a9b665',
    'green':        '#a9b665',
    'dark-yellow':  '#e78a4e',
    'yellow':       '#d8a657',
    'dark-blue':    '#7daea3',
    'blue':         '#7daea3',
    'dark-magenta': '#d3869b',
    'magenta':      '#d3869b',
    'dark-cyan':    '#89b482',
    'cyan':         '#88C0D0',
    'dark-gray':    '#665c54',
    'gray':         '#928374',
    'white':        '#ffffff',

    'fg4':          '#766f64',
    'fg3':          '#665c54',
    'fg2':          '#504945',
    'fg1':          '#3c3836',
    'bg0':          '#32302f',
    'fg0':          '#1d2021',
    'fg9':          '#ebdbb2'
}

colors = {}

for color, v in _colors.items():
    colors[color] = [v, v]


widget_defaults = {
    "font": "Caskaydia Cove Nerd Font",
    "fontsize": 16,
    "padding": 7,
    "background": colors["bg"],
    "foreground": colors["fg"]
}

extension_defaults = widget_defaults.copy()
font = widget_defaults["font"]


def check_update_command(updates):
    return updates - 1


class MyWidgets:
    def __init__(self):

        self.terminal = "terminator"

    def init_widgets_list(self):
        '''
        Function that returns the desired widgets in form of list
        '''
        widgets_list = [
            widget.Sep(
                linewidth=0,
                padding=6,
                foreground=colors["fg"],
                background=colors["bg"]
            ),
            widget.Image(
                background=colors["bg"],
                foreground=colors["fg"],
                filename="~/.config/qtile/icons/terminal-iconx14.png",
                mouse_callbacks={
                    'Button1': lambda : qtile.cmd_spawn('dmenu_run -p "Run: "')}
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=colors["fg"],
                background=colors["bg"]
            ),
            widget.GroupBox(
                margin_y=4,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=colors["fg"],
                inactive=colors["bg-inactive"],
                rounded=False,
                highlight_color=colors["fg"],
                highlight_method="block",
                this_current_screen_border=colors["dark-gray"],
                this_screen_border=colors["bg"],
                foreground=colors["white"],
                background=colors["bg"],
                fontsize=16,
                disable_drag=True
            ),
            widget.Prompt(prompt=">>> ", background=colors["bg"], foreground=colors["fg"], font=font),
            widget.WindowName(background=colors["bg"], foreground=colors["fg"], font=font),
            widget.Chord(
                chords_colors = {
                    "launch": ("#5e81ac", "#ffffff"),
                },
                name_transform = lambda name: name.upper(),
            ),
            widget.Sep(linewidth=0, padding=5, foreground=colors["fg"], background=colors["bg"]),
            widget.Systray(
                background=colors["bg"],
                foreground=colors["fg"],
                padding=5,
            ),
            widget.TextBox(
                text='\uE0B2',
                background=colors["bg"],
                foreground=colors["yellow"],
                padding=0,
                margin=0,
                fontsize=40
            ),
            widget.TextBox(
                text=" 🖬",
                foreground=colors["bg"],
                background=colors["yellow"],
                padding=0,
                margin=0,
                fontsize=14
            ),
            widget.Memory(
                foreground=colors["bg"],
                background=colors["yellow"],
                mouse_callbacks={'Button1': lambda : qtile.cmd_spawn(
                    self.terminal + ' -e htop')},
                padding=5
            ),
            widget.TextBox(
                text='\uE0B2',
                background=colors["yellow"],
                foreground=colors["magenta"],
                padding=0,
                fontsize=37
            ),
            widget.TextBox(
                text=" ⟳",
                padding=2,
                fontsize=14,
                foreground=colors["bg"],
                background=colors["magenta"]
            ),
            widget.CheckUpdates(
                custom_command="apt list --upgradable",
                custom_command_modify=check_update_command,
                no_update_string="No Updates",
                display_format="{updates} Updates",
                mouse_callbacks={'Button1': lambda : qtile.cmd_spawn(f"{self.terminal} -x sudo apt update && sudo apt upgrade")},
                background=colors["magenta"],
                foreground=colors["bg"],
                update_interval=60,
                padding=10
            ),
            widget.TextBox(
                text="\uE0B2",
                background=colors["magenta"],
                foreground=colors["red"],
                padding=0,
                fontsize=37,
            ),
            widget.TextBox(
                text=" Vol:",
                foreground=colors["bg"],
                background=colors["red"],
                padding=0
            ),
            widget.Volume(
                foreground=colors["bg"],
                background=colors["red"],
                padding=5,
                step=5
            ),
            widget.TextBox(
                text='\uE0B2',
                background=colors["red"],
                foreground=colors["dark-red"],
                padding=0,
                fontsize=37
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser(
                    "~/.config/qtile/icons")],
                foreground=colors["bg"],
                background=colors["dark-red"],
                padding=0,
                scale=0.7
            ),
            widget.CurrentLayout(
                foreground=colors["bg"],
                background=colors["dark-red"],
                padding=5
            ),
            widget.TextBox(
                text='\uE0B2',
                foreground=colors["cyan"],
                background=colors["dark-red"],
                padding=0,
                fontsize=37
            ),
            widget.Clock(
                foreground=colors["bg"],
                background=colors["cyan"],
                format="%d/%m/%Y  |   %H:%M:%S"
            ),
            widget.TextBox(
                text='\uE0B2',
                background=colors["cyan"],
                foreground=colors["white"],
                padding=0,
                fontsize=37
            ),
            widget.QuickExit(
                countdown_start=5,
                countdown_format="{} s",
                default_text="Logout",
                background=colors["white"],
                foreground=colors["bg"],
                padding=25
            ),
            widget.Sep(
                linewidth=0,
                padding=0,
                foreground=colors["white"],
                background=colors["white"]
            ),
        ]

        return widgets_list


    def init_widgets_screen(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen = self.init_widgets_list()
        return widgets_screen

    def init_widgets_screen2(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen2 = self.init_widgets_screen()
        return widgets_screen2

    def init_screen(self):
        '''
        Init the widgets in the screen
        '''
        return [Screen(top=bar.Bar(widgets=self.init_widgets_screen(), opacity=1.0, size=20)),
                Screen(top=bar.Bar(
                    widgets=self.init_widgets_screen2(), opacity=1.0, size=20))
                ]
