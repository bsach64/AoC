package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
)

type minBalls struct {
    red int
    green int
    blue int
}

func main() {
    file, err := os.ReadFile("2i.txt")
    if err != nil {
	fmt.Println(err.Error())
    }
    var data []string = strings.Split(string(file), "\n")
    Sum := 0
    for i := 0; i < len(data); i++ {
	if len(data[i]) > 0 {
	    id := ""
	    j := 5
	    for string(data[i][j]) != ":" {
		id += string(data[i][j])
		j++
	    }
	    rounds := strings.Split(data[i][j+1:], ";")
	    var info minBalls
	    for _, round := range rounds {
		entries := strings.Split(round, ",")
		for _, entry := range entries {
		    numberColor := strings.Split(entry, " ")
		    count, _ := strconv.Atoi(numberColor[1])
		    switch {
		    case numberColor[2][0] == 'r':
			if info.red < count {
			    info.red = count
			}
		    case numberColor[2][0] == 'g':
			if info.green < count {
			    info.green = count
			}
		    case numberColor[2][0] == 'b':
			if info.blue < count {
			    info.blue = count
			}
		    }
		}
	    }
	    Sum += (info.red * info.green * info.blue)
	}
    }
    fmt.Println(Sum)
}
