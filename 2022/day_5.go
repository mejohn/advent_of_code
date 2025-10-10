package main

import (
    "fmt"
    "os"
    s "strings"
    "regexp"
    "strconv"
)

type Stack struct {
    items []string
}

func NewStack() *Stack {
    return &Stack{}
}

func (s *Stack) Push(item string) {
    s.items = append(s.items, item)
}

func (s *Stack) Pop() (string, bool) {
    if len(s.items) == 0 {
        return "", false
    }
    item := s.items[len(s.items)-1]
    s.items = s.items[:len(s.items)-1]
    return item, true
}

func (s *Stack) Peek() string {
    if len(s.items) == 0 {
        return ""
    }
    item := s.items[len(s.items)-1]
    return item
}

func (s *Stack) Print() []string {
    return s.items
}

func main() {
    dat, _ := os.ReadFile("./input_5.txt")
    var input string = string(dat)
    splits := s.Split(input, "\n\n")
    fmt.Println(splits)

    stackSplits := s.Split(splits[0], "\n")
    instructions := s.Split(splits[1], "\n")
    fmt.Println(instructions)

    stacks := map[string]*Stack{}
    indices := map[string]int{}
    lastLine := stackSplits[len(stackSplits)-1]
    for j := range lastLine {
        if string(lastLine[j]) != " " {
            char := string(lastLine[j])
            indices[char] = j
            stacks[char] = NewStack()
        }
    }    
    fmt.Println(indices)

    for i := len(stackSplits)-2; i >= 0; i-- {
        for key,index := range indices {
            char := string(stackSplits[i][index])
            if char != " " {
                stacks[key].Push(char)
            }
        }
    }

    for i := 0; i < len(instructions)-1; i++ {
        instruction := instructions[i]
        // move /d{int} from /d{index} to /d{index}
        re := regexp.MustCompile("[0-9]+")
        groups := re.FindAllString(instruction, -1)
	fmt.Println(groups)

        num,_ := strconv.Atoi(groups[0])
        tempStack := Stack{}
        for _ = range num {
            item,_ := stacks[groups[1]].Pop()
            tempStack.Push(item)
        }
        for _ = range num {
            item,_ := tempStack.Pop()
            stacks[groups[2]].Push(item)
        }
    }

    for key,stack := range stacks {
        fmt.Println(stack.Print())
        fmt.Println(key, stack.Peek())
    }
}
