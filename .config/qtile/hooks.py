import os
import subprocess

from libqtile import hook
from libqtile.lazy import lazy


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    path = os.path.join(home, ".config/qtile/scripts/autostart.sh")
    
    subprocess.call([path])

@hook.subscribe.restart
def restart():

    lazy.reload_config()

