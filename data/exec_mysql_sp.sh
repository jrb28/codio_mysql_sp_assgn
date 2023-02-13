case $# in
  1)
    mysql -e "CALL w2la.$1();"
    ;;
  2)
    mysql -e "CALL w2la.$1('$2');"
    ;;
  3)
    mysql -e "CALL w2la.$1('$2', '$3');"
    ;;
  4)
    mysql -e "CALL w2la.$1('$2', '$3', '$4');"
    ;;
esac