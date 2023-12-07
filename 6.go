package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
)

func main() {
    file, _ := os.ReadFile("6i.txt")
    lines := strings.Split(string(file), "\n")
    timings, _ := strings.CutPrefix(lines[0], "Time:")
    distances, _ := strings.CutPrefix(lines[1], "Distance:")
    fmt.Println(partOne(timings, distances))
    fmt.Println(partTwo(timings, distances))
}

func partOne(timings string, distances string) int {
    timeStr := strings.Split(timings, " ")
    distStr := strings.Split(distances, " ")
    var times []int
    var dists []int
    for _, t := range timeStr {
	time, err := strconv.Atoi(t)
	if err == nil {
	    times = append(times, time)
	}
    }
    for _, d := range distStr {
	distance, err := strconv.Atoi(d)
	if err == nil {
	    dists = append(dists, distance)
	}
    }
    answer := 1
    for i, t := range times {
	answer *= calculateWins(t, dists[i])
    }
    return answer
}

func calculateWins(time int, record int) int {
    count := 0
    for t := 0; t < time + 1; t++ {
	if (time - t) * t > record {
	    count++
	} 
    }
    return count
}

func partTwo(time string, record string) int {
    timeStr := ""
    recordStr := ""
    time = strings.TrimSpace(time) 
    record = strings.TrimSpace(record)
    for _, t := range time {
	if t != ' ' {
	    timeStr += string(t)
	}
    }
    for _, r := range record {
	if r != ' ' {
	    recordStr += string(r)
	}
    }
    timeInt, _ := strconv.Atoi(timeStr)
    recordInt, _ := strconv.Atoi(recordStr)
    return calculateWins(timeInt, recordInt)
}
