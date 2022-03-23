# Path to your oh-my-zsh installation.
export ZSH="/home/batuhaninan/.oh-my-zsh"

ZSH_THEME="spaceship"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
DISABLE_UNTRACKED_FILES_DIRTY="true"

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git github npm pip pipenv pyenv pylint python sudo ubuntu virtualenv vscode web-search yarn aliases alias-finder autopep8 colorize command-not-found common-aliases colored-man-pages copypath copyfile debian docker docker-compose docker-machine git-prompt gnu-utils man node postgres zsh-autosuggestions)

source $ZSH/oh-my-zsh.sh

# User configuration

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='mvim'
fi

# Compilation flags
export ARCHFLAGS="-arch x86_64"

alias zshconfig="mate ~/.zshrc"
alias ohmyzsh="mate ~/.oh-my-zsh"

source /usr/share/gazebo-11/setup.sh
source /opt/ros/noetic/setup.zsh

#export GAZEBO_MODEL_PATH=~/Documents/Software/ardupilot_gazebo/models
#export GAZEBO_RESOURCE_PATH=~/Documents/Software/ardupilot_gazebo/words:${GAZEBO_RESOURCE_PATH}

export GAZEBO_MODEL_PATH=~/Documents/Software/ardupilot_gazebo/models:${GAZEBO_MODEL_PATH}
export GAZEBO_MODEL_PATH=~/Documents/Software/ardupilot_gazebo/models_gazebo:${GAZEBO_MODEL_PATH}
export GAZEBO_RESOURCE_PATH=~/Documents/Software/ardupilot_gazebo/worlds:${GAZEBO_RESOURCE_PATH}
export GAZEBO_PLUGIN_PATH=~/Documents/Software/ardupilot_gazebo/build:${GAZEBO_PLUGIN_PATH}

export ANDROID_SDK=$HOME/Android/Sdk:$PATH

export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/batuhaninan/Apps/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/batuhaninan/Apps/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/batuhaninan/Apps/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/batuhaninan/Apps/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


alias vim="lvim"
alias ls="exa -l --color=always --group-directories-first"
alias android-studio="/usr/local/android-studio/bin/studio.sh"
alias webstorm="~/Downloads/WebStorm/bin/webstorm.sh"

#export KDEWM=/home/batuhaninan/.local/bin/qtile
#qtile start
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'
#fpath+=${ZDOTDIR:-~}/.zsh_functions

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

export PATH=~/Android/Sdk/tools:$PATH
export PATH=~/Android/Sdk/platform-tools:$PATH

