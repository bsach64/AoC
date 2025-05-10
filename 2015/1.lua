local file = io.open("1.txt", "r")
local input = nil
if file then
	input = file:read("*all")
	input = input:gsub("\n", "")
	file:close()
end
if input then
	local floor = 0

	for i = 1, #input do
		local char = input:sub(i, i)
		if char == "(" then
			floor = floor + 1
		else
			floor = floor - 1
		end
		if floor == -1 then
			print("pos:", i)
			break
		end
	end
end
