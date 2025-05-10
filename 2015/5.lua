local function part_one()
	local ans = 0
	local vowels = {
		a = true,
		e = true,
		i = true,
		o = true,
		u = true
	}
	for line in io.lines("5.txt") do
		local vowel_count, is_nice, has_double = 0, true, false
		for i = 1, #line do
			local cur = line:sub(i, i)
			if i >= 2 then
				local prev = line:sub(i - 1, i - 1)
				local substring = prev .. cur
				if substring == "ab" or
					substring == "cd" or
					substring == "pq" or
					substring == "xy"
				then
					is_nice = false
					break
				end
				if prev == cur then
					has_double = true
				end
			end
			if vowels[cur] == true then
				vowel_count = vowel_count + 1
			end
		end
		if is_nice and has_double and vowel_count >= 3 then
			ans = ans + 1
		end
	end
	print(ans)
end

part_one()

local function part_two()
	local ans = 0
	for line in io.lines("5.txt") do
		local doubles, has_triple = {}, false
		for i = 1, #line do
			local cur = line:sub(i, i)
			if i >= 2 then
				local prev = line:sub(i - 1, i - 1)
				local substring = prev .. cur
				if doubles[substring] ~= nil then
					if i >= 3 then
						local prev_prev = line:sub(i - 2, i - 2)
						if cur == prev and cur == prev_prev then
						else
							doubles[substring] = doubles[substring] + 1
						end
					else
						doubles[substring] = doubles[substring] + 1
					end
				else
					doubles[substring] = 1
				end
			end
			if not has_triple and i >= 3 then
				local prev_prev = line:sub(i - 2, i - 2)
				if prev_prev == cur then
					has_triple = true
				end
			end
		end
		local has_double_double = false
		for key, val in pairs(doubles) do
			if val >= 2 then
				has_double_double = true
				break
			end
		end
		if has_double_double and has_triple then
			ans = ans + 1
		end
	end
	print(ans)
end

part_two()

-- generated using gemini, mine was incorrect
local function gem_part_two()
	local ans = 0
	local file = io.open("5.txt", "r")
	if not file then
		io.stderr:write("Error: Could not open file 5.txt\n")
		return
	end

	for line in file:lines() do
		local has_non_overlapping_pair = false
		local has_repeat_with_one_between = false

		-- Check for Rule 2: Contains at least one letter which repeats with exactly one letter between them
		for i = 1, #line - 2 do
			if line:sub(i, i) == line:sub(i + 2, i + 2) then
				has_repeat_with_one_between = true
				break -- Found one, no need to check further for this rule
			end
		end

		-- Check for Rule 1: Contains a pair of any two letters that appears at least twice without overlapping
		-- Iterate through all possible starting positions of the first pair
		for i = 1, #line - 3 do
			local pair = line:sub(i, i + 1)
			-- Search for the same pair starting from 2 positions after the start of the first pair
			for j = i + 2, #line - 1 do
				local second_pair = line:sub(j, j + 1)
				if pair == second_pair then
					has_non_overlapping_pair = true
					goto next_line -- Found a non-overlapping pair, move to the next line
				end
			end
		end
		::next_line:: -- Label for the goto

		-- If both rules are satisfied, increment the answer
		if has_non_overlapping_pair and has_repeat_with_one_between then
			ans = ans + 1
		end
	end

	file:close()
	print(ans)
end

gem_part_two()
