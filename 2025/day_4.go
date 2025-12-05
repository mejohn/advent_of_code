package main

import (
	"fmt"
	"os"
	s "strings"
	"slices"
)

func main() {
	dat, _ := os.ReadFile("./input_4.txt")
	var input string = string(dat)

	splits := s.Split(input, "\n")

	grid := [][]string{}
	accessible := [][2]int{}
	empty := [][2]int{}
	edges := [][2]int{}
	values := [][2]int{}

	maxI := len(splits) - 1
	maxJ := len(splits[0]) - 1
	for i := 0; i < len(splits); i++ {
		row := []string{}
		for j := 0; j < len(splits[i]); j++ {
			val := string(splits[i][j])
			coords := [2]int{i,j}
			if val == "@" {
				values = append(values, coords)
				if (j == 0 || i == 0 || j == maxJ || i == maxI) {
					edges = append(edges, coords)
				}
			} else if val == "." {
				empty = append(empty, coords)
			}
			row = append(row, val)
		}
		grid = append(grid, row)
	}

	for k := 0; k < len(edges); k++ {
		if !slices.Contains(accessible, edges[k]) && checkNeighbors(edges[k][0], edges[k][1], grid) {
			accessible = append(accessible, edges[k])
		}
	}

	for k := 0; k < len(empty); k++ {
		i,j := empty[k][0], empty[k][1]
		neighbors := getNeighbors(i,j,maxI,maxJ)
		for n := 0; n < len(neighbors); n++ {
			if slices.Contains(accessible, neighbors[n]) {
				continue
			}
			if grid[neighbors[n][0]][neighbors[n][1]] == "@" && checkNeighbors(neighbors[n][0], neighbors[n][1], grid) {
				accessible = append(accessible, neighbors[n])
			}
		}
	}
	fmt.Println("Part 1:", len(accessible))

	removed := len(accessible)
	for {
		// set all accessible to empty
		for c := 0; c < len(accessible); c++ {
			grid[accessible[c][0]][accessible[c][1]] = "."
		}
		accessible = [][2]int{}
		for v := 0; v < len(values); v++ {
			if grid[values[v][0]][values[v][1]] == "@" {
				if !slices.Contains(accessible, values[v]) && checkNeighbors(values[v][0], values[v][1], grid) {
					accessible = append(accessible, values[v])
				}
			}
		}
		removed += len(accessible)
		if len(accessible) == 0 {
			fmt.Println("Part 2:", removed)
			break
		}
	}
}

func checkNeighbors(i int, j int, grid [][]string) bool {
	wrappingNeighbors := getNeighbors(i, j, len(grid)-1, len(grid[0])-1)
	countEmpty := 8 - len(wrappingNeighbors)
	for w := 0; w < len(wrappingNeighbors); w++ {
		if grid[wrappingNeighbors[w][0]][wrappingNeighbors[w][1]] == "." {
			countEmpty += 1
		}
		if countEmpty >= 5 {
			return true
		}
	}
	return false
}

func getNeighbors(i int, j int, maxI int, maxJ int) [][2]int {
	potentials := [][2]int{
		[2]int{i+1,j},
		[2]int{i+1,j+1},
		[2]int{i,j+1},
		[2]int{i-1,j},
		[2]int{i-1,j-1},
		[2]int{i,j-1},
		[2]int{i+1,j-1},
		[2]int{i-1,j+1},
	}
	neighbors := [][2]int{}
	for k := 0; k < len(potentials); k++ {
		newI, newJ := potentials[k][0], potentials[k][1]
		if newI >= 0 && newI <= maxI && newJ >= 0 && newJ <= maxJ {
			neighbors = append(neighbors, potentials[k])
		}
	}
	return neighbors
}