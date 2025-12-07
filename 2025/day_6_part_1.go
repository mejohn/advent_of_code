package main 

import (
	"fmt"
	"os"
	s "strings"
	"strconv"
)

func main() {
	dat, _ := os.ReadFile("./input_6.txt")
	var input string = string(dat)

	splits := s.Split(input, "\n")

	grid := [][]int{}
	operators := []string{}
	for i := 0; i < len(splits); i++ {
		stringRow := s.Split(splits[i], " ")

		row := []int{}
		for j := 0; j < len(stringRow); j++ {
			if stringRow[j] != "" {
				if i == len(splits) - 1 {
					operators = append(operators, stringRow[j])
				} else {
					val,_ := strconv.Atoi(stringRow[j])
					row = append(row, val)
				}
			}
		}
		if i != len(splits) - 1 {
			grid = append(grid, row)
		}
	}
	sum := 0
	for o := 0; o < len(operators); o++ {
		total := 0
		if operators[o] == "+" {
			for i := 0; i < len(grid); i++ {
				total += grid[i][o]
			}
			sum += total
		} else if operators[o] == "*" {
			total := 1
			for i := 0; i < len(grid); i++ {
				total *= grid[i][o]
			}
			sum += total
		}
	}
	fmt.Println("Part 1:", sum)
}