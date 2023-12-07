package main

import (
    "fmt"
    "strings"
    "strconv"
    "os"
)

func main() {
    file, err := os.ReadFile("1s.txt")
    if err != nil {
	fmt.Println(err.Error())
    }
    var dataString []string = strings.Split(string(file), "\n")
    var count int = 0
    for i := 0; i < len(dataString); i++ {
	last := len(dataString[i]) - 1
	first := 0
	for j := 0; j < len(dataString[i]); j++ {
	    if !isDigit(dataString[i][first]) {
		first++
	    }
	    if !isDigit(dataString[i][last]) {
		last--
	    }
	}
	if first > -1 && last > -1 {
	    curr, err := strconv.Atoi(
		string(dataString[i][first]) + string(dataString[i][last]),
		)
	    if err != nil {
		fmt.Println(err.Error())
	    }
	    count += curr
	}
    }
    fmt.Println(count)
}

func isDigit(char byte) bool {
    if char >= '0' && char <= '9' {
	return true
    }
    return false
}
