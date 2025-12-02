package main

import (
	"fmt"
	"os"
	"slices"
	s "strings"
	"strconv"
)

func main() {
	dat, _ := os.ReadFile("./input_2.txt")
	var input string = string(dat)

	splits := s.Split(input, ",")

	invalid1 := []int{}
	invalid2 := []int{}

	for i := 0; i < len(splits); i++ {
		bounds := s.Split(splits[i], "-")
		left := bounds[0]
		right := bounds[1]

		leftInt,_ := strconv.Atoi(left)
		rightInt,_ := strconv.Atoi(right)

		for j := leftInt; j <= rightInt; j++ {
			jString := strconv.Itoa(j);
			half := len(jString) / 2

			// part 1
			jLeft := jString[0:half]
			jRight := jString[half:]

			if jLeft == jRight {
				invalid1 = append(invalid1, j)
			}

			// part 2
			for k := 1; k <= half; k++ {
				if len(jString) % k != 0 || slices.Contains(invalid2, j) {
					continue
				}
				pattern := jString[0:k]
				repeats := len(jString) / k
				if s.Repeat(pattern, repeats) == jString {
					invalid2 = append(invalid2, j)
				}
			}
		}
		
	}
	
	var part1 int
	for i := range invalid1 {
		part1 += invalid1[i]
	}
	var part2 int
	for i := range invalid2 {
		part2 += invalid2[i]
	}
	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}