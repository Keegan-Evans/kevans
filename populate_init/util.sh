function get_function_names() {
    file=$1
    raw_names=$(awk '
      BEGIN { raw = "" };
      /^def\ [^_][a-zA-z_0-9]*\(/ { raw=raw $2 " " };
      END { print raw }' $file)

      IFS=", " read -ra raw_array <<< "$raw_names"

      for i in "${raw_array[@]}"
      do
          IFS="(" read -ra cleaned_name <<< "$i"
          printf "$cleaned_name\n"
      done
}

function parse_init(){
    current_init=$1
}

if [ $1 ]
then
    provided=$1
    get_function_names $provided
fi

