package main

import (
    "fmt"
    "os"
    "strings"
)
    
func main() {
    file, _ := os.ReadFile("5s.txt")
    fmt.Println(string(file))
}
