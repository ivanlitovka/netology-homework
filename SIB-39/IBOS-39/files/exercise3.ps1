if  ((Test-Path -Path $args[0] -PathType Container) -eq $true)
{"This is direcory"}
elseif ((Test-Path -Path $args[0] -PathType Leaf) -eq $true)
{"This is file"}
else
{"Object not exist"}

