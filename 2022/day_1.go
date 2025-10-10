package main

import (
    "fmt"
    "os"
    "sort"
    s "strings"
    "strconv"
)

func main() {
    dat, _ := os.ReadFile("./input_1.txt")

    var input string = string(dat)

    splits := s.Split(input, "\n")
    fmt.Println(splits)

    var elf int
    var elves = make(map[int]int)

    for i := 0; i < len(splits); i++ {
        if splits[i] == "" {
            elf++
        } else {
            cals,_ := strconv.Atoi(splits[i])
            elves[elf] += cals            
        }
    }

    fmt.Println(elves)

    var mostCals int
    for _, value := range elves {
        if value > mostCals {
            mostCals = value
        }
    }

    fmt.Println(mostCals)

    type kv struct {
        Key int
        Value int
    }

    var slices []kv
    for k, v := range elves {
        slices = append(slices, kv{k, v})
    }

    sort.Slice(slices, func(y, z int) bool {
        return slices[y].Value > slices[z].Value
    })

    var topThree int
    for _,kv := range slices[0:3] {
        fmt.Println(kv.Key, kv.Value)
        topThree += kv.Value
    }
    fmt.Println(topThree)
}
