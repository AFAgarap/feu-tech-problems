total=0
j=0
i=1
printf "Enter number of seconds: "
read -r seconds
while [ $j -lt $seconds ]
do	
	result=`expr $(($j % 2))`
	if [[ "$result" -ne "0" ]]; then
		i=`expr $(($i + 1))`
	fi
	total=`expr $(($total + $i))`
	j=`expr $(($j + 1))`
done
printf $total
printf "\n"