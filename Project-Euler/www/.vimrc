" Shortcut for a new Problem Row in the table
autocmd FileType html inoremap <Leader>c <tr><CR></tr><Esc>O<td>000</td><CR><td><a href="https://projecteuler.net/" target="_blank">NAME</a></td><CR><td class="solved">&cross;</td><CR><td><a href="./code/" target="_blank">View</a></td><Esc>kkk^llllcit

autocmd FileType html inoremap <Leader>d <hr/><CR><CR><div class="prob"><CR></div><Esc>O<h3>TITLE</h3><CR><h4>Problem </h4><CR><div class="desc"><CR></div><CR><p>Answer: <b></b></p><Esc>

autocmd FileType html set textwidth=100
autocmd FileType html set colorcolumn=101

autocmd FileType html set spell
