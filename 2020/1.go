package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
	"time"
)

func main() {
	file, err := os.ReadFile("1i.txt")
	if err != nil {
		fmt.Println(err.Error())
	}
	var	dataString []string = strings.Split(string(file), "\n")
	data := make([]int, 0, len(dataString))
	dataCount := len(dataString)
	for i := 0; i < dataCount; i++ {
		number, err := strconv.Atoi(dataString[i])
		if err != nil {
			fmt.Println(err.Error())
		}
		data = append(data, number)
	}
	fmt.Println("PART ONE\n")
	t0 := time.Now()
	var twosum [2] int = partOne(data, dataCount)
	fmt.Printf("Using two for loops: %v\n", time.Since(t0))	
	fmt.Printf("Numbers: %v %v \n", twosum[0], twosum[1])
	fmt.Printf("Answer: %v \n\n", twosum[0]*twosum[1])
	
	t0 = time.Now()	
	var twosumtoo [2] int = partOneFaster(data)	
	fmt.Printf("Using hash maps: %v\n", time.Since(t0))	
	fmt.Printf("Numbers: %v %v\n", twosumtoo[0], twosumtoo[1])
	fmt.Printf("Answer: %v\n\n", twosumtoo[0]*twosumtoo[1])
	
	fmt.Println("PART TWO\n")
	t0 = time.Now()
	var threesum [3] int = partTwo(data, dataCount)	
	fmt.Printf("Using three for loops: %v\n", time.Since(t0))	
	fmt.Printf("Numbers: %v %v %v \n", threesum[0], threesum[1], threesum[2])
	fmt.Printf("Answer: %v \n\n", threesum[0]*threesum[1]*threesum[2])
	
	t0 = time.Now()
	var threesumtoo[3] int = partTwoFaster(data)
	fmt.Printf("Using Hash Maps: %v\n", time.Since(t0))	
	fmt.Printf("Numbers: %v %v %v \n", threesumtoo[0], threesumtoo[1], threesumtoo[2])
	fmt.Printf("Answer: %v \n", threesumtoo[0]*threesumtoo[1]*threesumtoo[2])
}

func partOne(data []int, dataCount int) [2]int {
	var answer [2]int 
	for i := 0; i < dataCount; i++ {
		for j := 0; j < dataCount; j++ {
			if i != j && data[i] + data[j] == 2020 {
				answer[0] = data[i]	
				answer[1] = data[j]
				return answer	
			}
		}
	}
	return answer
}

func partTwo(data []int, dataCount int) [3] int {
	var answer [3]int 
	for i := 0; i < dataCount; i++ {
		for j := 0; j < dataCount; j++ {
			for k := 0; k < dataCount; k++ {
				if i != j && j != k && k != i && data[i] + data[j] + data[k] == 2020 {
					answer[0] = data[i]	
					answer[1] = data[j]
					answer[2] = data[k]
					return answer	
				}
			}
		}
	}
	return answer
}

// Using hashing or Maps
func partOneFaster(data []int) [2] int {
	dataCount := len(data)	
	var answer [2]int
	numbers := make(map[int]int)
	target := 2020	
	for i := 0; i < dataCount; i++ {	
		toFind := target - data[i]
		_, ok := numbers[toFind]
		if ok {
			answer[0] = data[i]
			answer[1] = toFind
			return answer
		} else {
			numbers[data[i]] = i
		}
	}	
	return answer
}

// Using hashing or Maps
func partTwoFaster(data []int) [3] int {
	dataCount := len(data)
	target := 2020
	var answer [3] int
	numbers := make(map[int]int)
	for i := 0; i < dataCount; i++ {
		remaining := target - data[i]
		for j := 0; j < dataCount; j++ {
			if i != j {
				toFind := remaining - data[j]
				_, ok := numbers[toFind]
				if ok {
					answer[0] = data[i]
					answer[1] = data[j]
					answer[2] = toFind
					return answer
				} else {
					numbers[data[j]] = j
				}
			}
		}
	}
	return answer
}