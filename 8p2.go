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
    currents := getStarting(connections) 
    steps := make([]int, 0)
    for _, entry := range currents {
	step, i, current := 0, 0, entry
	for current.name[2] != 'Z' {
	    if instructions[i] == 'L' {
		current = connections[current.left]
	    } else if instructions[i] == 'R' {
		current = connections[current.right]
	    }
	    step++
	    i = (i + 1) % len(instructions)
	}
	steps = append(steps, step)
    }
    fmt.Println(lcm(steps))
}

func parseLine(line string) node {
    var newNode node
    newNode.name = line[0:3]
    newNode.left = line[7:10]
    newNode.right = line[12:15]
    return newNode
}

func getStarting(connections map[string]node) []node {
    starting := make([]node, 0)
    for _, v := range connections {
	if v.name[2] == 'A' {
	    starting = append(starting, v)
	}
    }
    return starting
}

func isEnd(current []node) bool {
    for _, entry := range current {
	if entry.name[2] != 'Z' {
	    return false
	}
    }
    return true
}

func move(current []node, connections map[string]node, direction string) []node {
    if direction == "left" {
	for i, _ := range current {
	    current[i] = connections[current[i].left]
	}	
    } else if direction == "right" {
	for i, _ := range current {
	    current[i] = connections[current[i].right]
	}
    }
    return current
}

func lcm(steps []int) int {
    ans := steps[0]
    for i := 1; i < len(steps); i++ {
	ans = (steps[i] * ans) / gcd(steps[i], ans)
    }
    return ans
}

func gcd(a int, b int) int {
    if b == 0 {
	return a
    }
    return gcd(b, a % b)
}
