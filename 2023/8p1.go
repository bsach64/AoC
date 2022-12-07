package main

import (
    "fmt"
    "os"
    "strings"
)

type node struct {
    name string
    left string
    right string
}


func main() {
    file, _ := os.ReadFile("8i.txt")
    lines := strings.Split(string(file), "\n")
    instructions := lines[0]
    connections := make(map[string]node)
    for _, line := range lines[2:len(lines) - 1] {
	newNode := parseLine(line)
	connections[newNode.name] = newNode
    }
    current := connections["AAA"]
    steps, i := 0, 0
    for current.name != "ZZZ" {
	if instructions[i] == 'L' {
	    current = connections[current.left]
	} else if instructions[i] == 'R' {
	    current = connections[current.right]
	}
	steps++
	i = (i + 1) % len(instructions)
    }
    fmt.Println(steps)
}

func parseLine(line string) node {
    var newNode node
    newNode.name = line[0:3]
    newNode.left = line[7:10]
    newNode.right = line[12:15]
    return newNode
}
