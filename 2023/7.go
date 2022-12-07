package main

import (
    "fmt"
    "strings"
    "os"
)

/*
    5 : Five of a kind,
    4 : Four of a kind,
    F : Full house,
    3 : Three of kind,
    2 : Two pair,
    1 : One pair,
    H : High card
*/

type handInfo struct {
    hType byte
    cards string
}
    
func main() {
    file, _ := os.ReadFile("7s.txt")
    data := strings.Split(string(file), "\n")
    data = data[:len(data) - 1]
    for _, line := range data {
	entry := strings.Split(line, " ")
	_ = getHand(entry[0])
    }
}

func getHand(cards string) handInfo {
    var hand handInfo
    unique := make(map[string]int)
    count := 0
    for _, card := range cards {
	_, present := unique[string(card)]
	if !present {
	    count++
	    unique[string(card)] = 1
	} else {
	    unique[string(card)]++
	}
    }
    fmt.Println(cards, unique)
    return hand
}

