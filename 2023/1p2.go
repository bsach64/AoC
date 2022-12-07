package main

import (
    "fmt"
    "strings"
    "strconv"
    "os"
)

func main() {
    file, err := os.ReadFile("1i.txt")
    if err != nil {
	fmt.Println(err.Error())
    }
    var dataString []string = strings.Split(string(file), "\n")
    count := 0
    for i := 0; i < len(dataString); i++ {
	var digits []string = make([]string, 0)
	j := 0
	for j < len(dataString[i]) {
	    present, digit, index := getDigit(dataString[i][j:])
	    if !present {
		j++
		continue
	    }
	    digits = append(digits, digit)
	    j += index
	}
	if len(digits) > 0 {
	    curr, err := strconv.Atoi(digits[0] + digits[len(digits) - 1])
	    if err != nil {
		fmt.Println(err.Error())
	    }
	    count += curr
	}
    }
    fmt.Println(count)
}

func getDigit(chars string) (bool, string, int) {
    if chars[0] >= '0' && chars[0] <= '9' {
	return true, string(chars[0]), 1
    }
    if len(chars) >= 3 {
	switch {
	case chars[:3] == "one": 
	    return true, "1", 2
	case chars[:3] == "two":
	    return true, "2", 2
	case chars[:3] == "six": 
	    return true, "6", 2
	}
    }
    if len(chars) >= 4 {
	switch {
	case chars[:4] == "zero":
	    return true, "0", 3
	case chars[:4] == "four": 
	    return true, "4", 3
	case chars[:4] == "five": 
	    return true, "5", 3
	case chars[:4] == "nine": 
	    return true, "9", 3
	}
    }
    if len(chars) >= 5 {
	switch {
	case chars[:5] == "three": 
	    return true, "3", 4
	case chars[:5] == "seven": 
	    return true, "7", 4
	case chars[:5] == "eight": 
	    return true, "8", 4
    }
    }
    return false, "", 0
}
