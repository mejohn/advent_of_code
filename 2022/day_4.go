package main

import (
    "fmt"
    "os"
    s "strings"
    "strconv"
)

func main () {
    dat, _ := os.ReadFile("./input_4.txt")
    var input string = string(dat)
    splits := s.Split(input, "\n")

    var counter int
    var counter2 int
    for i := range len(splits) - 1 {
        pairs := s.Split(splits[i], ",")
        pair1 := s.Split(pairs[0], "-")
        pair2 := s.Split(pairs[1], "-")
        start1,_ := strconv.Atoi(pair1[0])
        end1,_ := strconv.Atoi(pair1[1])
        start2,_ := strconv.Atoi(pair2[0])
        end2,_ := strconv.Atoi(pair2[1])
        fmt.Println(start1, end1, start2, end2)

        if start2 <= start1 && end2 >= end1 {
            counter += 1
        } else if start1 <= start2 && end1 >= end2 {
            counter += 1
        }

        if (start1 >= start2 && start1 <= end2) || (end1 >= start2 && end1 <= end2) {
            counter2 += 1
        } else if (start2 >= start1 && start2 <= end1) || (end2 >= start1 && end2 <= end1) {
            counter2 += 1
        } 
    }
    fmt.Println("Part 1:", counter)
    fmt.Println("Part 2:", counter2)
}
