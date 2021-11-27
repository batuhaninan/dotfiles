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
plugins=(git github pip pipenv pyenv pylint python sudo ubuntu virtualenv vscode web-search yarn aliases alias-finder autopep8 colorize command-not-found common-aliases colored-man-pages copydir copyfile debian docker docker-compose docker-machine git-prompt gnu-utils man node npm npx postgres zsh-autosuggestions)

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

#source /opt/ros/noetic/setup.zsh
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

#export KDEWM=/home/batuhaninan/.local/bin/qtile
#qtile start
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'
#fpath+=${ZDOTDIR:-~}/.zsh_functions
