echo "Enter n:"
read n
echo "Enter p:"
read p
echo "Enter q:"
read q
paul="PAUL"
opp="OPPONENT"
val=`expr $(((($p + $q) / $n) % 2))`
case "$val" in
	0) player="$paul" ;;
	*) player="$opp" ;;
esac
echo $player
