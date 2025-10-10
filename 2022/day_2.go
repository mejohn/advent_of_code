package main

import (
    "fmt"
    "os"
    "slices"
    s "strings"
)

func main () {
    points := map[string]int{"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3, "win": 6, "draw": 3, "lose": 0}
    wins := []string{"A Y", "B Z", "C X"}
    dat, _ := os.ReadFile("./input_2.txt")

    var input string = string(dat)

    rounds := s.Split(input, "\n")

    fmt.Println(rounds)
    fmt.Println(points)

    var totalScore int
    for i := range len(rounds) - 1 {
        choices := s.Split(rounds[i], " ")
        totalScore += points[choices[1]]
        if points[choices[0]] == points[choices[1]] {
            totalScore += points["draw"]
        } else if slices.Contains(wins, rounds[i]) {
            totalScore += points["win"]
        } else {
            totalScore += points["lose"]
        }
    }

    fmt.Println("Part 1", totalScore)

    newPoints := map[string]int {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    var stratScore int
    for i := range len(rounds) - 1 {
        choices := s.Split(rounds[i], " ")
        stratScore += newPoints[choices[1]]
        if choices[1] == "Y" {
            stratScore += newPoints[choices[0]]
        } else if choices[1] == "Z" {
            switch choices[0] {
            case "A":
                stratScore += newPoints["B"]
            case "B":
                stratScore += newPoints["C"]
            case "C":
                stratScore += newPoints["A"]
            }
        } else {
            switch choices[0] {
            case "A":
                stratScore += newPoints["C"]
            case "B":
                stratScore += newPoints["A"]
            case "C":
                stratScore += newPoints["B"]
            }
        }
    }
    fmt.Println("Part 2", stratScore)
}
