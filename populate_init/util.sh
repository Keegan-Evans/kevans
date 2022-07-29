function discover_python_function_definitions() {
    FILE=$1
    defs=${awk '/^def\ [^_][a-zA-z_0-9]*\(/' $FILE}
}


if [ $1 ]
then
    provided=$1
    printf "${provided}\n"
    discover_python_function_definitions provided
fi
