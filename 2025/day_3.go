package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	s "strings"
)

func main() {
	dat, _ := os.ReadFile("./input_3.txt")
	var input string = string(dat)

	splits := s.Split(input, "\n")
	banks := [][]int{}

	answer1 := 0
	for i := 0; i < len(splits); i++ {
		bank := []int{}
		tens := 0
		index := 0
		for j:=0; j<len(splits[i])-1; j++ {
			val,_ := strconv.Atoi(string(splits[i][j]))
			bank = append(bank, val)
			if val > tens {
				tens = val
				index = j
			}
		}
		val,_ := strconv.Atoi(string(splits[i][len(splits[i])-1]))
		bank = append(bank, val)
		banks = append(banks, bank)
		ones := 0
		for j:=index+1; j < len(bank); j++ {
			if bank[j] > ones {
				ones = bank[j]
			}
		}
		answer1 += (tens*10)+ones
	}
	fmt.Println("Part 1", answer1)

	answer2 := 0
	for i := 0; i < len(banks); i++ {
		total := 0
		min := 0
		for j := 12; j > 0; j-- {
			next := brrr(min, len(banks[i]) - j, banks[i])
			min = next[1] + 1
			total += int(math.Pow(10, float64(j-1)))*next[0]
		}
		answer2 += total
	}
	fmt.Println("Part 2", answer2)

}

func brrr(min int, max int, bank []int) []int {
	out := 0
	index := 0
	for j := min; j <= max; j++ {
		if bank[j] > out {
			out = bank[j]
			index = j
		}
	}
	return []int{out, index}
}