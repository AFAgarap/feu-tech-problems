read -r number
result=`expr $(($number % 2))`
if [[ "$result" != "0" || "$number" -ge "5" && "$number" -le "20" ]]
then
	echo "Weird"
else
	echo "Not Weird"
fi