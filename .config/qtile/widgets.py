import os
from libqtile import bar, widget
from libqtile.config import Screen
from libqtile import qtile
from colors import colors, get_next_color, get_matching_foreground


fonts = [
    "Caskaydia Cove Nerd Font",
    "Hack Nerd Font Mono",
]

opacity = 0.75

widget_defaults = {
    "font": fonts[-1],
    "fontsize": 16,
    "padding": 7,
    "background": colors["bg"],
    "foreground": colors["fg"]
}

extension_defaults = widget_defaults.copy()
font = widget_defaults["font"]


class WidgetCreator:
    last_widget_color = colors["bg"]

    @staticmethod
    def create_arrow(wg):
        wg.foreground = get_next_color()
        wg.background = WidgetCreator.last_widget_color
        wg.text = '\uE0B2'
        WidgetCreator.last_widget_color = wg.foreground

        return wg

    @staticmethod
    def create_widget(wg, color=None):
        if color:
            wg.background = color
            return wg

        wg.background = WidgetCreator.last_widget_color
        wg.foreground = get_matching_foreground(wg.background)

        return wg


def check_update_command(updates):
    return updates - 1


class MyWidgets:
    def __init__(self):
        self.terminal = "terminator"

    def init_widgets_list(self):
        widgets_list = [
            WidgetCreator.create_widget(
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    foreground=colors["fg"],
                ), colors["bg"]
            ),
            WidgetCreator.create_widget(
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
                    fontsize=16,
                    disable_drag=True
                ), colors["bg"]
            ),
            WidgetCreator.create_widget(
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    foreground=colors["fg"],
                ), colors["bg"]
            ),
            WidgetCreator.create_widget(
                widget.Prompt(prompt=">>> ", foreground=colors["fg"], font=font), colors["bg"]
            ),
            WidgetCreator.create_widget(
                widget.WindowName(foreground=colors["fg"], font=font), colors["bg"]
            ),
            WidgetCreator.create_widget(
                widget.Chord(
                    chords_colors={
                        "launch": ("#5e81ac", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ), False
            ),
            WidgetCreator.create_widget(
                widget.Sep(linewidth=0, padding=5, foreground=colors["fg"]), colors["bg"]
            ),
            WidgetCreator.create_widget(
                widget.Systray(
                    foreground=colors["fg"],
                    padding=5,
                ), colors["bg"]
            ),
            WidgetCreator.create_arrow(
                widget.TextBox(
                    foreground=colors["yellow"],
                    padding=0,
                    margin=0,
                    fontsize=40
                ),
            ),
            WidgetCreator.create_widget(
                widget.TextBox(
                    text=" 🖬",
                    background=colors["yellow"],
                    padding=0,
                    margin=0,
                    fontsize=14
                ),
            ),
            WidgetCreator.create_widget(
                widget.Memory(
                    foreground=colors["bg"],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                        self.terminal + ' -e htop')},
                    padding=5
                ),
            ),
            WidgetCreator.create_arrow(
                widget.TextBox(
                    foreground=colors["magenta"],
                    padding=0,
                    fontsize=37
                ),
            ),
            WidgetCreator.create_widget(
                widget.TextBox(
                    text=" ⟳",
                    padding=2,
                    fontsize=14,
                    foreground=colors["bg"],
                ),
            ),
            WidgetCreator.create_widget(
                widget.CheckUpdates(
                    custom_command="apt list --upgradable",
                    custom_command_modify=check_update_command,
                    no_update_string="No Updates",
                    display_format="{updates} Updates",
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn(f"{self.terminal} -x sudo apt update && sudo apt upgrade")},
                    foreground=colors["bg"],
                    update_interval=60,
                    padding=10
                ),
            ),
            WidgetCreator.create_arrow(
                widget.TextBox(
                    foreground=colors["red"],
                    padding=0,
                    fontsize=37,
                ),
            ),
            WidgetCreator.create_widget(
                widget.TextBox(
                    text=" Vol:",
                    foreground=colors["bg"],
                    padding=0
                ),
            ),
            WidgetCreator.create_widget(
                widget.Volume(
                    foreground=colors["bg"],
                    padding=5,
                    step=5
                ),
            ),
            WidgetCreator.create_arrow(
                widget.TextBox(
                    foreground=colors["dark-red"],
                    padding=0,
                    fontsize=37
                ),
            ),
            WidgetCreator.create_widget(
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser(
                        "~/.config/qtile/icons")],
                    foreground=colors["bg"],
                    padding=0,
                    scale=0.7
                ),
            ),
            WidgetCreator.create_widget(
                widget.CurrentLayout(
                    foreground=colors["white"],
                    padding=5
                ),
            ),
            WidgetCreator.create_arrow(
                widget.TextBox(
                    foreground=colors["cyan"],
                    padding=0,
                    fontsize=37
                ),
            ),
            WidgetCreator.create_widget(
                widget.Clock(
                    foreground=colors["bg"],
                    format="%d/%m/%Y  |   %H:%M:%S"
                ),
            ),
            WidgetCreator.create_arrow(
                widget.TextBox(
                    foreground=colors["white"],
                    padding=0,
                    fontsize=37
                ),
            ),
            WidgetCreator.create_widget(
                widget.QuickExit(
                    countdown_start=5,
                    countdown_format="{} s",
                    default_text="Logout",
                    foreground=colors["bg"],
                    padding=25
                ),
            ),
            WidgetCreator.create_widget(
                widget.Sep(
                    linewidth=0,
                    padding=0,
                    foreground=colors["white"],
                ),
            ),
        ]

        return widgets_list

    def init_widgets_screen(self):
        return self.init_widgets_list()

    def init_widgets_screen2(self):
        return self.init_widgets_screen()

    def init_screen(self):
        return [
            Screen(top=bar.Bar(widgets=self.init_widgets_screen(), opacity=opacity, size=20, margin=[10, 16, 0, 16])),
            Screen(top=bar.Bar(widgets=self.init_widgets_screen2(), opacity=1.0, size=20, margin=[10, 16, 0, 16]))
        ]
