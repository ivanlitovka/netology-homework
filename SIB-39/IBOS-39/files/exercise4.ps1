if  ($args[0] -eq "encrypt")
{[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($args[1]))}
elseif ($args[0] -eq "decrypt")
{[Text.Encoding]::Utf8.GetString([Convert]::FromBase64String($args[1]))}
else
{"Use next sintax: exercise4.ps1 encrypt|decrypt text"}