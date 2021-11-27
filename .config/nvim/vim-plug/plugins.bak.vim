" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    Plug 'sheerun/vim-polyglot'
    Plug 'scrooloose/NERDTree'
    Plug 'jiangmiao/auto-pairs'
    Plug 'preservim/nerdtree'
    Plug 'onsails/lspkind-nvim'
    Plug 'hrsh7th/nvim-cmp'
    Plug 'hrsh7th/cmp-nvim-lsp'
    Plug 'neovim/nvim-lspconfig'
    Plug 'hrsh7th/cmp-path'
    Plug 'hrsh7th/cmp-buffer'
    Plug 'quangnguyen30192/cmp-nvim-ultisnips'
    Plug 'Vimjas/vim-python-pep8-indent'
    Plug 'jeetsukumaran/vim-pythonsense'
    Plug 'machakann/vim-swap'
    Plug 'phaazon/hop.nvim'
    Plug 'romainl/vim-cool'
    Plug 'PeterRincker/vim-searchlight'
    Plug 'kevinhwang91/nvim-hlslens'
    Plug 'haya14busa/vim-asterisk'
    Plug 'nvim-telescope/telescope-symbols.nvim'
    Plug 'navarasu/onedark.nvim'
    Plug 'mhinz/vim-signify'
    Plug 'vim-airline/vim-airline-themes'
    Plug 'vim-airline/vim-airline'
    Plug 'akinsho/bufferline.nvim'
    Plug 'goolord/alpha-nvim'
    Plug 'lukas-reineke/indent-blankline.nvim'
    Plug 'itchyny/vim-highlighturl'
    Plug 'rcarriga/nvim-notify'
    Plug 'ludovicchabant/vim-gutentags'
    Plug 'liuchengxu/vista.vim'
    Plug 'SirVer/ultisnips'
    Plug 'honza/vim-snippets'
    Plug 'Raimondi/delimitMate'
    Plug 'tpope/vim-commentary'
    Plug 'mg979/vim-visual-multi'
    Plug 'Pocco81/AutoSave.nvim'
    Plug 'simnalamburt/vim-mundo'
    Plug 'tpope/vim-eunuch'
    Plug 'tpope/vim-repeat'
    Plug 'jdhao/better-escape.vim'
    Plug 'sbdchd/neoformat'
    Plug 'tpope/vim-fugitive'
    Plug 'rbong/vim-flog'
    Plug 'kevinhwang91/nvim-bqf'
    Plug 'rhysd/committia.vim'
    Plug 'plasticboy/vim-markdown'
    Plug 'vim-pandoc/vim-markdownfootnotes'
    Plug 'godlygeek/tabular'
    Plug 'elzr/vim-json'
    Plug 'folke/zen-mode.nvim'
    Plug 'chrisbra/unicode.vim'
    Plug 'wellle/targets.vim'
    Plug 'machakann/vim-sandwich'
    Plug 'michaeljsmith/vim-indent-object'
    Plug 'tmux-plugins/vim-tmux'
    Plug 'andymass/vim-matchup'
    Plug 'karb94/neoscroll.nvim'
    Plug 'tpope/vim-scriptease'
    Plug 'skywind3000/asyncrun.vim'
    Plug 'cespare/vim-toml'
    Plug 'sakhnik/nvim-gdb'
    Plug 'tpope/vim-obsession'
    Plug 'ojroques/vim-oscyank'
    Plug 'gelguy/wilder.nvim'
    Plug 'folke/which-key.nvim'
    Plug 'jdhao/whitespace.nvim'
call plug#end()


autocmd VimEnter * NERDTree
