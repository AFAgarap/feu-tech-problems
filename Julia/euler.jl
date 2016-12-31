function main()
	print("Enter value for x: ")
	x = parse(Float64, readline())
	print("Enter value for f(x): ")
	y = parse(Float64, readline())
	print("Approximate what? [f(x)] : ")
	m = parse(Float64, readline())
	print("Enter increment: ")
	i = parse(Float64, readline())

	delta_y = 0.0
	dy_dx = 0

	while x <= m
		dy_dx = F(x, y)
		delta_y = find_slope(dy_dx, i)
		@printf "x:%f\ty:%f\tdy/dx:%f\tΔy:%f\n" x y dy_dx delta_y
		y = y + delta_y
		x = x + i
	end
end

function F(x, y)
	return 2x + 2y
end

function find_slope(dy_dx, i)
	return dy_dx * i
end

main()