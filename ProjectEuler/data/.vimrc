set textwidth=120

command LoadData call LoadData()

function LoadData()
	read template.txt
	normal ggddl
	startinsert 
endfunction
