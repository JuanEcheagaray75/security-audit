echo "Hello! Fear not, user. I'm just a script that will list all the installed software on this machine"
echo "Please give me an alias for you: "
read alias
echo "Thank you, $alias. I will now list all the installed software on this machine"
dpkg -l > inventory/data/raw/ubuntu-installed-software-$alias-test.txt
echo "I've saved the list of installed software to inventory/data/raw/ubuntu-installed-software-$alias.txt"
