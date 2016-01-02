printf "Enter number of test cases: "
read -r testCase
while [ $testCase -gt 0 ]
do
	printf "Enter number of cigarettes: "
	read -r number
	printf "Enter number of butts: "
	read -r butts
	count=$number
		while [ $number -ge $butts ]
		do
			count=`expr $(($count + ($number / $butts)))`
			number=`expr $(($number / $butts))`
		done
	echo $count
	testCase=`expr $(($testCase - 1))`
done
