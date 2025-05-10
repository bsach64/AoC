local function main()
	local ans_one, ans_two = 0, 0
	for line in io.lines("2.txt") do
		local cur_number, numbers = "", {}
		for i = 1, #line do
			local char = line:sub(i, i)
			if char ~= "x" then
				cur_number = cur_number .. char
			else
				numbers[#numbers+1] = tonumber(cur_number)
				cur_number = ""
			end
		end
		if cur_number ~= "" then
			numbers[#numbers+1] = tonumber(cur_number)
		end
		table.sort(numbers)
		ans_one = ans_one + (3 * numbers[1] * numbers[2]) + (2 * numbers[2] * numbers[3]) + (2 * numbers[3] * numbers[1])
		ans_two = ans_two + (2 * numbers[1]) + (2 * numbers[2]) + (numbers[1] * numbers[2] * numbers[3])
	end
	print("Part1", ans_one)
	print("Part2", ans_two)
end

main()
