from libqtile import layout
from libqtile.config import Match



floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])



layouts = [
    layout.MonadTall(
        border_focus=["#88c0d0", "#88c0d0"],
        border_normal=["#282828", "#282828"],
        grow_amount=20,
        margin=10
    ),
    layout.Max(),
]

