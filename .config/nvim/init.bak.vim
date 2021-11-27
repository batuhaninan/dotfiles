source $HOME/.config/nvim/vim-plug/plugins.vim

lua require('plugins')

nnoremap <C-Left> :tabprevious<CR>                                                                            
nnoremap <C-Right> :tabnext<CR>
nnoremap <C-j> :tabprevious<CR>                                                                            
nnoremap <C-k> :tabnext<CR>

set laststatus=2
"augroup packer_user_config
  "autocmd!
  "autocmd BufWritePost plugins.lua source <afile> | PackerCompile
"augroup end
