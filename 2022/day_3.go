package main

import (
    "fmt"
    "os"
    s "strings"
)

func main () {
    priorities := "OabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    dat, _ := os.ReadFile("./input_3.txt")

    var input string = string(dat)

    splits := s.Split(input, "\n")
    fmt.Println(splits)

    var total int
    for i := 0; i < len(splits); i++ {
        compartmentLength := len(splits[i]) / 2
        s1 := splits[i][0:compartmentLength]
        s2 := splits[i][compartmentLength:]
        var item string
        for _,k := range s1 {
            if s.Contains(s2, string(k)) {
                item = string(k)
                break
            }
        }
        total += s.Index(priorities, item)
    }
    fmt.Println("Part 1:", total)

    var badgeTotal int
    for i := 0; i < (len(splits)/3); i++ {
        offset := i*3
        s1 := splits[offset+0]
        s2 := splits[offset+1]
        s3 := splits[offset+2]
	fmt.Println(s1, s2, s3)
        var badge string
        for _,k := range s1 {
            if s.Contains(s2, string(k)) && s.Contains(s3, string(k)) {
                badge = string(k)
                break
            }
        }
        fmt.Println(badge, badgeTotal, s.Index(priorities, badge))
        badgeTotal += s.Index(priorities, badge)
    }
    fmt.Println("Part 2:", badgeTotal)
}
