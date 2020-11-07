filetype plugin indent on
syntax on
set encoding=utf-8
set number
set wrap linebreak

set textwidth=74

" Set options for formatting prose, for more information see:
" https://alols.github.io/2012/11/07/writing-prose-with-vim/
set formatoptions=t1

augroup PROSE
	autocmd InsertEnter * set formatoptions+=a
	autocmd InsertEnter * set formatoptions-=a
augroup END

" Reflows changes made in normal mode
noremap Q gqap

" takes hardwrapped text and soft wraps it.
command! -range=% SoftWrap
            \ <line2>put _ |
            \ <line1>,<line2>g/.\+/ .;-/^$/ join |normal $x

set backspace=indent,eol,start  " more powerful backspacing
