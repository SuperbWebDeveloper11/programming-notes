
" Resources :
" https://www.youtube.com/watch?v=n9k9scbTuvQ&t=56s
" https://github.com/erkrnt/awesome-streamerrc/tree/master/ThePrimeagen
" https://www.youtube.com/watch?v=wzrZPcwh-bE

syntax on " basic highlighting
syntax enable " enable highlighting

set hidden
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab "from tabs to spaces
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set incsearch
set noswapfile
set scrolloff=5 " keep 5 line at the buttom of the file

"--------------- html indentation ------------------
autocmd BufRead,BufNewFile *.htm,*.html setlocal tabstop=2 shiftwidth=2 softtabstop=2

:imap jj <Esc>
   
map <C-a> <esc>ggVGy " yank all file
map <C-f> <esc>gg=G " format all file 
map <C-p> :bp<CR> " go to previous opened file
map <C-n> :bn<CR> " go to next opened file
map <C-o> <esc>:NERDTreeToggle <CR>   

let g:html_indent_script1 = "inc"
let g:html_indent_style1 = "inc"
let g:html_indent_inctags = "html,body,head"


" highlit current line for dark theme
set cursorline
hi cursorline cterm=none term=none
autocmd WinEnter * setlocal cursorline
autocmd WinLeave * setlocal nocursorline
highlight CursorLine guibg=#303000 ctermbg=234

"autoclose and position cursor to write text inside
inoremap ' ''<left>
inoremap ` ``<left>
inoremap " ""<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap % %%<left>
"autoclose with : and position cursor to write text inside
inoremap ': '':<left><left>
inoremap `: ``:<left><left>
inoremap ": "":<left><left>
inoremap (: ():<left><left>
inoremap [: []:<left><left>
inoremap {: {}:<left><left>
"autoclose and position cursor after
inoremap '<tab> ''
inoremap `<tab> ``
inoremap "<tab> ""
inoremap (<tab> ()
inoremap [<tab> []
inoremap {<tab> {}
"autoclose 2 lines below and position cursor in the middle
inoremap '<CR> '<CR>'<ESC>O
inoremap `<CR> `<CR>`<ESC>O
inoremap "<CR> "<CR>"<ESC>O
inoremap (<CR> (<CR>)<ESC>O
inoremap [<CR> [<CR>]<ESC>O
inoremap {<CR> {<CR>}<ESC>O

" to make cursore move one character to the right
let CursorColumnI = 0 "the cursor column position in INSERT
autocmd InsertEnter * let CursorColumnI = col('.')
autocmd CursorMovedI * let CursorColumnI = col('.')
autocmd InsertLeave * if col('.') != CursorColumnI | call cursor(0, col('.')+2) | endif

set colorcolumn=80
highlight ColorColumn ctermbg=0 guibg=lightgrey


call plug#begin('~/.vim/plugged')

Plug 'preservim/nerdtree'
autocmd vimenter * NERDTree "open a NERDTree automatically when vim starts up
let g:NERDTreeQuitOnOpen = 1 "close automatically when I open a file for editing
let NERDTreeShowHidden=1 " to display hidden files 

Plug 'mattn/emmet-vim' 
let g:user_emmet_leader_key=','

Plug 'morhetz/gruvbox' " Designed as a bright theme

Plug 'norcalli/nvim-colorizer.lua' " css coloriser

" create Snippets
Plug 'SirVer/ultisnips'
" Snippets are separated from the engine. Add this if you want them:
Plug 'honza/vim-snippets'

let g:UltiSnipsSnippetDirectories=[$HOME.'/.config/ultisnips']
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"
 
call plug#end()

colorscheme gruvbox
set background=dark
set t_Co=256


let mapleader = " "
" example: nnoremap <leader>o :NERDTreeToggle <CR>
