package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	file, err := os.ReadFile("3i.txt")
	if err != nil {
		fmt.Println(err.Error())
	}
	var pattern []string = strings.Split(string(file), "\n")
	answer := countTrees(pattern, 1, 1)
	answer *= countTrees(pattern, 1, 3)
	answer *= countTrees(pattern, 1, 5)
	answer *= countTrees(pattern, 1, 7)
	answer *= countTrees(pattern, 2, 1)
	fmt.Println(answer)
}

func countTrees(pattern []string, down int, right int) int {
	trees := 0
	patternSize := len(pattern[0])
	patternLength := len(pattern)
	currentRow := 0
	var position [2]int
	for currentRow < patternLength {
		if pattern[position[0]][position[1]] == '#' {
			trees += 1
		}
		currentRow += down
		position[0] = (position[0] + down) 
		position[1] = (position[1] + right) % patternSize
	}
	return trees
}