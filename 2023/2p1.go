package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
)

func main() {
    file, err := os.ReadFile("2i.txt")
    if err != nil {
	fmt.Println(err.Error())
    }
    var data []string = strings.Split(string(file), "\n")
    idSum := 0
    for i := 0; i < len(data); i++ {
	if len(data[i]) > 0 {
	    id := ""
	    j := 5
	    for string(data[i][j]) != ":" {
		id += string(data[i][j])
		j++
	    }
	    intId, _ := strconv.Atoi(id)
	    isValid := true
	    rounds := strings.Split(data[i][j+1:], ";")
	    for _, round := range rounds {
		entries := strings.Split(round, ",")
		for _, entry := range entries {
		    numberColor := strings.Split(entry, " ")
		    count, _ := strconv.Atoi(numberColor[1])
		    switch {
		    case numberColor[2][0] == 'r' && count > 12:
			isValid = false
			break
		    case numberColor[2][0] == 'g' && count > 13:
			isValid = false
			break
		    case numberColor[2][0] == 'b' && count > 14:
			isValid = false
			break
		    }
		}
		if !isValid {
		    break
		}
	    }
	    if isValid {
		idSum += intId
	    }
	}
    }
    fmt.Println(idSum)
}
