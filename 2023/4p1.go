package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
)

func main() {
    file, _ := os.ReadFile("4i.txt")
    games := strings.Split(string(file), "\n")
    games = games[:len(games) - 1]
    total := 0
    repeats := make(map[int]int)
    for _, game := range games {
	_, winning, cards := parse(game)
	total += calculatePoints(winning, cards)
    }
    scratchCards := len(games)
    for _, game := range games {
	gameN, winning, cards := parse(game)
	j := repeats[gameN]
	for j > -1 {
	    matches := calculateMatches(winning, cards)
	    scratchCards += matches
	    for k := 1; k <= matches; k++ {
		repeats[gameN + k]++
	    }
	    j--
	}
    }
    fmt.Println(scratchCards)
    fmt.Println(total)
}

func calculatePoints(winning map[int]int, cards []int) int {
    points := 0
    for _, card := range cards {
	_, present := winning[card]
	if present {
	    if points == 0 {
		points = 1
	    } else {
		points *= 2
	    }
	}
    }
    return points 
}

func calculateMatches(winning map[int]int, cards []int) int {
    points := 0
    for _, card := range cards {
	_, present := winning[card]
	if present {
	    points++
	}
    }
    return points 
}



func parse(line string) (int, map[int]int, []int) {
    line = line[5:]
    game := strings.Split(line, ":")
    gameN, _ := strconv.Atoi(strings.TrimSpace(game[0]))
    cardsInfo := strings.Split(game[1], "|")
    return gameN, genMap(cardsInfo[0]), genArray(cardsInfo[1])
}

func genArray(input string) []int {
    inputN := strings.Split(input, " ")
    var numbers []int
    for _, numS := range inputN {
	number, err := strconv.Atoi(numS) 
	if err == nil {
	    numbers = append(numbers, number)
	}
    }
    return numbers
}

func genMap(input string) map[int]int {
    inputN := strings.Split(input, " ")
    numbers := make(map[int]int)
    for _, numS := range inputN {
	number, err := strconv.Atoi(numS) 
	if err == nil {
	    numbers[number] = 0
	}
    }
    return numbers
}
