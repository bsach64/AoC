package main

import (
    "fmt"
    "strings"
    "strconv"
    "os"
)

type GearLoc struct {
    row int
    col int
}

func main() {
    file, err := os.ReadFile("3i.txt")
    if err != nil {
	fmt.Println(err.Error())
    }
    engineMap := strings.Split(string(file), "\n")
    engineMap = engineMap[:len(engineMap) - 1]
    fmt.Println(findGearRatio(engineMap))
}

func findGearRatio(engineMap []string) int {
    gearRatio := 0
    for i, row := range engineMap {
	for j, _ := range row {
	    if row[j] == '*' {
		nOne, nTwo, valid := isValidGear(GearLoc{row: i, col:j}, engineMap)
		if valid {
		    gearRatio += nOne * nTwo
		}
	    }
	}
    }
    return gearRatio
}

func isDigit(symbol byte) bool {
    if symbol >= '0' && symbol <= '9' {
	return true
    }
    return false
}

func addNumber(row int, col int, engineMap[]string, numsPtr *[]int) {
    j := col - 1;
    for j < col + 2 {
	if j < -1 {
	    j++
	    continue
	} else if j > len(engineMap[row]) {
	    break
	}
	if isDigit(engineMap[row][j]) {
	    number := 0
	    j, number = getNumber(engineMap[row], j)
	    *numsPtr = append(*numsPtr, number)
	} 
	j++
    }
}

func isValidGear(gear GearLoc, engineMap []string) (int, int, bool) {
    var numbers []int
    pRow, nRow := gear.row - 1, gear.row + 1
    if pRow > -1 {
	addNumber(pRow, gear.col, engineMap, &numbers)
    }
    if gear.col - 1 > -1 && isDigit(engineMap[gear.row][gear.col - 1]) {
	_, number := getNumber(engineMap[gear.row], gear.col - 1)
	numbers = append(numbers, number)
    }
    if gear.col + 1 < len(engineMap[gear.row]) && isDigit(engineMap[gear.row][gear.col + 1]) {
	_, number := getNumber(engineMap[gear.row], gear.col + 1)
	numbers = append(numbers, number)
    }
    if nRow < len(engineMap) {
	addNumber(nRow, gear.col, engineMap, &numbers)
    }
    if len(numbers) == 2 {
	return numbers[0], numbers[1], true
    }
    return 0, 0, false
}

func getNumber(num string, digitI int) (int, int) {
    maxI, numS :=  digitI, ""
    for j := digitI; j < len(num) && isDigit(num[j]); j++ {
	numS += string(num[j])
	maxI = j
    }
    for j := digitI - 1; j > - 1 && isDigit(num[j]); j-- {
	numS = string(num[j]) + numS
    }
    number, _ := strconv.Atoi(numS)
    return maxI, number
}
