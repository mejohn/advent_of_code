package main

import (
	"fmt"
	"os"
	s "strings"
	"slices"
)

func main() {
	dat, _ := os.ReadFile("./test_7.txt")
	var input string = string(dat)

	splits := s.Split(input, "\n")

	grid := [][]string{}
	beams := [][2]int{}
	splitters := map[int][][2]int{}
	splittersHit := 0
	endBeams := [][2]int{}
	start := [2]int{}

	for i := 0; i < len(splits); i++ {
		row := []string{}
		for j := 0; j < len(splits[i]); j++ {
			val := string(splits[i][j])
			if val == "S" {
				beams = append(beams, [2]int{i+1,j})
				start[0] = i
				start[1] = j
			} else if val == "^" && slices.Contains(beams, [2]int{i-1,j}) {
				split := false
				if !slices.Contains(beams, [2]int{i,j-1}) {
					beams = append(beams, [2]int{i,j-1})
					split = true
				} 
				if !slices.Contains(beams, [2]int{i,j+1}) {
					beams = append(beams, [2]int{i,j+1})
					split = true
				}
				if split {
					splitters[i] = append(splitters[i], [2]int{i,j})
					splittersHit++
				}
			} else if val == "." && slices.Contains(beams, [2]int{i-1,j}) {
				beams = append(beams, [2]int{i,j})
				if i == len(splits) - 1{
					endBeams = append(endBeams, [2]int{i,j})
				}
			}
			row = append(row, val)
		}
		grid = append(grid, row)
	}
	fmt.Println("Part 1", splittersHit)
}
