local function part_one()
	local file = io.open("3.txt", "r")
	local input = nil
	if not file then
		return
	end

	input = file:read("*all")
	input = input:gsub("\n", "")
	file:close()

	if not input then
		return
	end

	local cur_x, cur_y = 0, 0
	local visited, count = {["0,0"] = true}, 0
	for i = 1, #input do
		local direction = input:sub(i, i)
		if direction == "^" then
			cur_y = cur_y + 1
		elseif direction == "v" then
			cur_y = cur_y - 1
		elseif direction == ">" then
			cur_x = cur_x + 1
		else
			cur_x = cur_x - 1
		end
		local location = tostring(cur_x) .. "," .. tostring(cur_y)
		visited[location] = true
	end
	for _, _ in pairs(visited) do
		count = count + 1
	end
	print(count)
end

part_one()


local function part_two()
	local file = io.open("3.txt", "r")
	local input = nil
	if not file then
		return
	end

	input = file:read("*all")
	input = input:gsub("\n", "")
	file:close()

	if not input then
		return
	end

	local santa_x, santa_y = 0, 0
	local robo_x, robo_y = 0, 0
	local visited, count = {["0,0"] = true}, 0
	for i = 1, #input do
		local direction = input:sub(i, i)
		if direction == "^" then
			if i % 2 ~= 0 then
				santa_y = santa_y + 1
			else
				robo_y = robo_y + 1
			end
		elseif direction == "v" then
			if i % 2 ~= 0 then
				santa_y = santa_y - 1
			else
				robo_y = robo_y - 1
			end
		elseif direction == ">" then
			if i % 2 ~= 0 then
				santa_x = santa_x + 1
			else
				robo_x = robo_x + 1
			end
		else
			if i % 2 ~= 0 then
				santa_x = santa_x - 1
			else
				robo_x = robo_x - 1
			end
		end
		local location = nil
		if i % 2 ~= 0 then
			location = tostring(santa_x) .. "," .. tostring(santa_y)
		else
			location = tostring(robo_x) .. "," .. tostring(robo_y)
		end
		visited[location] = true
	end
	for _, _ in pairs(visited) do
		count = count + 1
	end
	print(count)
end

part_two()
