#/bin/zsh
echo $0
# get target module
target_module_directory=$1;
printf "$target_module_directory\n"
target=('egg' 'turkey')
for each [ [in [$target] ;] ] do
    printf("\n%s", $each);
done
# check for/locate or create target module init
echo "file already added to your __init__"
# parse target and locate functions
# append to init

# stretch goals:
# specify list of things not to add to init
