let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

" Run PlugInstall if there are missing plugins
autocmd VimEnter * if len(filter(values(g:plugs), '!isdirectory(v:val.dir)'))
  \| PlugInstall --sync | source $MYVIMRC
\| endif

call plug#begin('/home/batuhaninan/.config/nvim/autoload/plugged')

    Plug 'jiangmiao/auto-pairs'
    Plug 'preservim/nerdtree'
    Plug 'Vimjas/vim-python-pep8-indent'
    Plug 'jeetsukumaran/vim-pythonsense'
    Plug 'tbodt/deoplete-tabnine', {'do': './install.sh'}
    Plug 'frazrepo/vim-rainbow'
    Plug 'nvim-lualine/lualine.nvim'
    Plug 'kyazdani42/nvim-web-devicons'
    Plug 'tpope/vim-surround'
    Plug 'tpope/vim-fugitive'
    Plug 'airblade/vim-gitgutter'
    Plug 'nvim-lua/plenary.nvim'
    Plug 'nvim-telescope/telescope.nvim'
    Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
    Plug 'ellisonleao/glow.nvim'
    Plug 'dracula/vim', { 'as': 'dracula' }


call plug#end()



lua << EOF
require'lualine'.setup{
options = {
	theme = 'nord',
	icons_enabled = false
	},
sections = {
	lualine_b = {'mode'},
	lualine_c = {'mode'}
	},
inactive_sections = {
	lualine_b = {'mode'},
	lualine_c = {'mode'}
	},
extensions = {'quickfix'}
}
EOF
