package main

import (
	"fmt"
	"regexp"
	"strconv"
	"os"
	"errors"
	"strings"
)

func main() {
	re := regexp.MustCompile(`(?P<lowerlimit>[0-9]+)-(?P<upperlimit>[0-9]+) (?P<character>[a-z]): (?P<password>[a-z]+)`)	
	file, err := os.ReadFile("2i.txt")
	if err != nil {
		fmt.Println(err.Error())
	}
	var	dataString []string = strings.Split(string(file), "\n")
	var validCount int = partOne(dataString, re)
	fmt.Println(validCount)
	validCount = partTwo(dataString, re)
	fmt.Println(validCount)
}

func getInfo(matches []string, re *regexp.Regexp) (int, int, string, string, error) {
	var ierr error	
	lowerlimit, err := strconv.Atoi(matches[re.SubexpIndex("lowerlimit")])
	if err != nil {
		ierr = errors.New("Could not parse string")
		return 0, 0, "", "", ierr
	}
	upperlimit, err := strconv.Atoi(matches[re.SubexpIndex("upperlimit")])
	if err != nil {
		ierr = errors.New("Could not parse string")
		return 0, 0, "", "", ierr
	}
	character := matches[re.SubexpIndex("character")]
	password := matches[re.SubexpIndex("password")]
	return lowerlimit, upperlimit, character, password, nil
}

func partOne(dataString []string, re *regexp.Regexp) int {
	validCount := 0
	for _, data := range dataString {
		matches := re.FindStringSubmatch(data)
		lowerLimit, upperLimit, character, password, err := getInfo(matches, re)
		if err != nil {
			fmt.Println(err.Error())
		}
		character = string(character)	
		countLetter := 0
		for i := 0; i < len(password); i++ {
			if password[i] == character[0] {
				countLetter += 1
			}
		}
		if countLetter >= lowerLimit && countLetter <= upperLimit {
			validCount += 1
		}
	}
	return validCount
}

func partTwo(dataString []string, re *regexp.Regexp) int {
	validCount := 0
	for _, data := range dataString {
		matches := re.FindStringSubmatch(data)
		one, two, character, password, err := getInfo(matches, re)
		if err != nil {
			fmt.Println(err.Error())
		}
		character = string(character)	
		countLetter := 0
		if password[one - 1] == character[0] {
			countLetter += 1
		}
		if password[two - 1] == character[0] {
			countLetter += 1
		}
		if countLetter == 1 {
			validCount += 1
		}
	}
	return validCount
}
