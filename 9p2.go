package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
)

func main() {
    file, _ := os.ReadFile("9i.txt")
    lines := strings.Split(string(file), "\n")
    lines = lines[:len(lines) - 1]
    sum := 0
    for _, line := range lines {
	numbers := parseArray(line)
	sum += numbers[0] - prevDiff(numbers)
    }
    fmt.Println(sum)
}

func parseArray(line string) []int {
    numbers := make([]int, 0)
    for _, entry := range strings.Split(line, " ") {
	number, err := strconv.Atoi(entry)
	if err == nil {
	    numbers = append(numbers, number)
	}
    }
    return numbers
}

func prevDiff(numbers []int) int {
    flag := true
    for _, number := range numbers {
	if number != 0 {
	    flag = false
	}
    }
    if flag {
	return 0
    }
    diffs := make([]int, 0)
    for i := 1; i < len(numbers); i++ {
	diffs = append(diffs, numbers[i] - numbers[i - 1]) 
    }
    return diffs[0] - prevDiff(diffs)
}
