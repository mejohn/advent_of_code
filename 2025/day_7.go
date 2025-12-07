package main

import (
	"fmt"
	"os"
	s "strings"
)

func main() {
	dat, _ := os.ReadFile("./input_7.txt")
	var input string = string(dat)

	splits := s.Split(input, "\n")

	splittersHit := 0
	beamCounters := map[[2]int]int{}
	paths := 0

	for i := 0; i < len(splits); i++ {
		for j := 0; j < len(splits[i]); j++ {
			lastBeam := [2]int{i-1,j}
			
			switch val := string(splits[i][j]); val {
			case "S":
				beamCounters[[2]int{i,j}] = 1
			case "^":
				if beamCount,ok := beamCounters[lastBeam]; ok {
					beamCounters[[2]int{i,j+1}] += beamCount
					beamCounters[[2]int{i,j-1}] += beamCount
					splittersHit++
				}
			case ".":
				if beamCount,ok := beamCounters[lastBeam]; ok {
					beamCounters[[2]int{i,j}] += beamCount
				}
			}
		}
		
		if i == len(splits)-1 {
			for b := range beamCounters {
				if b[0] == i {
					paths += beamCounters[b]
				}
			}
		}
	}
	fmt.Println("Part 1", splittersHit)
	fmt.Println("Part 2", paths)
}
