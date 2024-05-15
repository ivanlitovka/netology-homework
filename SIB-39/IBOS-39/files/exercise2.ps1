$dir=Get-ChildItem -Path $args[0]

foreach ($val in $dir){
    echo $val
    (($counter++))
}
echo "Количество файлов в папке: $counter."