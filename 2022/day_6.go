package main

import (
    "fmt"
    "os"
)

func main() {
    dat, _ := os.ReadFile("./input_6.txt")
    var input string = string(dat)
    
    window := []string{}
    var windowStart int

    for windowEnd := 0; windowEnd < len(input) - 4; windowEnd++ {
        if len(window) != 4 {
            window = append(window, string(input[windowEnd]))
        } else {
            if window[0] != window[1] && window[0] != window[2] && window[0] != window[3] && window[1] != window[2] && window[1] != window[3] && window[2] != window[3] {
                fmt.Println("Part 1", window, windowStart, windowEnd)
                break
            }
            window = window[1:]
            window = append(window, string(input[windowEnd]))
            windowStart++
        }
    }

    window = []string{}
    windowStart = 0
    seen := map[string]int{}
    for windowEnd := 0; windowEnd < len(input) - 14; windowEnd++ {
        newChar := string(input[windowEnd])
        if len(window) != 14 {
            window = append(window, newChar)
            seen[newChar]++
        } else {
            allUnique := true
            for _,val := range seen {
                if val > 1 {
                    allUnique = false
                    break
                }
            }
            if allUnique {
                fmt.Println("Part 2", window, windowStart, windowEnd, newChar)
                break
            }
            window = window[1:]
            window = append(window, newChar)
            seen[string(input[windowStart])]--
            windowStart++
            seen[newChar]++
        }
    }
}
