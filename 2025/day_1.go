package main

import (
	"fmt"
	"os"
	s "strings"
	"strconv"
)

func main() {
	dat, _ := os.ReadFile("./day_1.txt")
	var input string = string(dat)

	splits := s.Split(input, "\n")

	var password1 int
	var password2 int
	var current int = 50

	for i := 0; i < len(splits); i++ {
		dir := splits[i][0:1]
		num,_ := strconv.Atoi(splits[i][1:])
		rem := num % 100
		password2 += num / 100

		if dir == "R" {
			current += rem
			if current > 99 {
				password2++
			}
		} else {
			if current - rem <= 0 && current != 0 {
				password2++
			}
			current -= rem
		}

		if current < 0 {
			current += 100
		}
		current %= 100

		if current == 0 {
			password1 += 1
		}
		fmt.Println(splits[i], current, password2)
	}

	fmt.Println("Part 1", password1)
	fmt.Println("Part 2", password2)

	current = 50
	password2 = 0
	for i := 0; i < len(splits); i++ {
		dir := splits[i][0:1]
		num,_ := strconv.Atoi(splits[i][1:])

		if dir == "R" {
			for j := 0; j < num; j++ {
				current++
				if current == 100 {
					password2++
					current = 0
				}
			}
		} else {
			for j := 0; j < num; j++ {
				if current == 1 {
					password2++
				}
				current--
				if current == -1 {
					current = 99
				}
			}
		}
	}
	fmt.Println("Brute Force", password2)
}