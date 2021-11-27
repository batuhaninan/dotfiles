import random


_colors = {
    'bg':           '#282828',
    'bg-inactive':  '#525252',
    'fg':           '#88C0D0',
    
    # Widget colors
    'turquoise':    '#45B8AC',
    'coral':        '#FF6F61',
    'ultra-violet': '#6B5B95',
    'serenity':     '#92A8D1',
    'pepper':       '#9B2335',
    'white':        '#ffffff',
    'sand-dollar':  '#DFCFBE',

    'yellow':       '#ef9d10',
    'green':        '#a9b665',
    'red':          '#ea6962',
    'blue':         '#7daea3',
    'magenta':      '#d3869b',
    'cyan':         '#88C0D0',
    'gray':         '#928374',


    'dark-red':     '#800000',
    'dark-green':   '#a9b665',
    'dark-yellow':  '#e78a4e',
    'dark-blue':    '#7daea3',
    'dark-magenta': '#d3869b',
    'dark-cyan':    '#89b482',
    'dark-gray':    '#665c54',

    'black':        '#000000',
    'fg4':          '#766f64',
    'fg3':          '#665c54',
    'fg2':          '#504945',
    'fg1':          '#3c3836',
    'bg0':          '#32302f',
    'fg0':          '#1d2021',
    'fg9':          '#ebdbb2'
}


colors = {}

_light_colors = ["white", "yellow", "sand-dollar"]
_dark_colors = ["bg", "black"]


for color, v in _colors.items():
    colors[color] = [v, v]


light_colors = [colors[_color] for _color in _light_colors]
dark_colors = [colors[_color] for _color in _dark_colors]

colors_list = list(colors)

START_COLOR_INDEX = 3
COLOR_INDEX_INC_VALUE = 1


def get_next_color():
    
    if get_next_color.i >= len(colors_list):
        get_next_color.i = START_COLOR_INDEX
    
    _color = colors_list[get_next_color.i]
    get_next_color.i += COLOR_INDEX_INC_VALUE
    
    return colors[_color]
        
setattr(get_next_color, "i", START_COLOR_INDEX)



def get_matching_foreground(bg):
    
    if bg in light_colors:
        return colors["black"]
    
    if bg in dark_colors:
        return colors["white"] 
    
    return colors["white"]
    
