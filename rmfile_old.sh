#!bin/bash

dir="./_trash/"

if [ -d "$dir" ] && [ -s "$dir" ]; then 
	find _trash/ -not -path "_trash/" -mmin +1 -exec rm -rf {} \;
	echo "1"
elif [ ! -d "$dir" ]; then
	mkdir /root/_trash
	echo "2"
else
	echo "외쳐 에코!" 
fi
