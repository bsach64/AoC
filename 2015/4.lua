local md5 = require("md5")

local function main()
	local input, number = "yzbqklnj", 1
	local data = input .. tostring(number)
	local hash = md5.sumhexa(data)
	print(hash:sub(1, 5))
	while hash:sub(1, 6) ~= "000000" do
		number = number + 1
		data = input .. tostring(number)
		hash = md5.sumhexa(data)
	end
	print(number)
end

main()
