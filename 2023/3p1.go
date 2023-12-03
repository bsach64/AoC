package main

import (
    "fmt"
    "strings"
    "strconv"
    "os"
)

type Coordinate struct {
    row int
    start int
    end int
}

func main() {
    file, err := os.ReadFile("3i.txt")
    if err != nil {
	fmt.Println(err.Error())
    }
    engineMap := strings.Split(string(file), "\n")
    engineMap = engineMap[:len(engineMap) - 1]
    sum := 0
    for _, num := range validNumbers(engineMap) {
	sum += num
    }
    fmt.Println(sum)
}

func validNumbers(engineMap []string) []int {
    var numbers []int
    for i := 0; i < len(engineMap); i++ {
	row, j := engineMap[i], 0
	for j < len(engineMap[i]) {
	    if isDigit(row[j]) {
		co := Coordinate{row: i, start: j, end: j}
		for j + 1 < len(engineMap[i]) && isDigit(row[j + 1]) {
		    co.end++
		    j++
		}
		num, valid := isValidNumber(co, engineMap) 
		if valid {
		    numbers = append(numbers, num)
		}
	    } 
	    j++
	}
    }
    return numbers
}

func isDigit(symbol byte) bool {
    if symbol >= '0' && symbol <= '9' {
	return true
    }
    return false
}

func isValidNumber(co Coordinate, engineMap []string) (int, bool) {
    num, _ := strconv.Atoi(engineMap[co.row][co.start: co.end + 1])
    pRow, nRow, pCol, nCol := co.row - 1, co.row + 1, co.start - 1, co.end + 1
    if pRow > -1 && checkRow(pRow, co, engineMap) {
	return num, true
    }
    if nRow < len(engineMap) && checkRow(nRow, co, engineMap) {
	return num, true
    }
    if pCol > -1 && engineMap[co.row][pCol] != '.' {
	return num, true
    }
    if nCol < len(engineMap) && engineMap[co.row][nCol] != '.' {
	return num, true
    }
    return -1, false
}

func checkRow(row int, co Coordinate, engineMap []string) bool {
    if co.start - 1 > -1 && engineMap[row][co.start - 1] != '.' { 
	return true
    }
    for j := co.start; j < co.end + 1; j++ {
	if engineMap[row][j] != '.' {
	    return true
	}
    }
    if co.end + 1 < len(engineMap[row]) && engineMap[row][co.end + 1] != '.' {
	return true
    }
    return false
}
