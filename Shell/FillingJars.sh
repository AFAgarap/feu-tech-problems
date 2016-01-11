answer=0
printf "Enter n: "
read -r n
printf "Enter m: "
read -r m
while [ $m -gt 0 ]
do
	printf "Enter a: "
	read -r a
	printf "Enter b: "
	read -r b
	printf "Enter k: "
	read -r k
	answer=`expr $(($answer + ((($b - $a) + 1) * $k)))`
	m=`expr $(($m - 1))`
done
answer=`expr $(($answer / n))`
echo $answer