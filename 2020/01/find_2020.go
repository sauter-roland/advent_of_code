package main

import (
	"io/ioutil"
	"strings"
	"strconv"
	"fmt"
)

func FindTwo2020(numList []int) int {
	var lenList = len(numList)

	for i := 0; i < lenList; i++ {
		fi := numList[i]
		for j := i; j < lenList; j++ {
			fj := numList[j]
			if fi+fj == 2020 {
				return (fi * fj)
			}
		}
	}
	return -1
}

func FindThree2020(numList []int) int {
	var lenList = len(numList)

	for i := 0; i < lenList; i++ {
		fi := numList[i]
		for j := i; j < lenList; j++ {
			fj := numList[j]
			for k := j; k < lenList; k++ {
				fk := numList[k]
				if fi+fj+fk == 2020 {
					return (fi * fj * fk)
				}
			}
		}
	}
	return -1
}

func ReadFile(fname string) (nums []int, err error) {
    b, err := ioutil.ReadFile(fname)
    if err != nil { return nil, err }

    lines := strings.Split(string(b), "\n")
    // Assign cap to avoid resize on every append.
    nums = make([]int, 0, len(lines))

    for _, l := range lines {
        // Empty line occurs at the end of the file when we use Split.
        if len(l) == 0 { continue }
        // Atoi better suits the job when we know exactly what we're dealing
        // with. Scanf is the more general option.
        n, err := strconv.Atoi(l)
        if err != nil { return nil, err }
        nums = append(nums, n)
    }

    return nums, nil
}

func main() {
	//testList := []int{1721, 979, 366, 299, 675, 1456}
	//fmt.Println(find2020(testList))
	numFile := "input_01.txt"
	numList, err := ReadFile(numFile)
	if err != nil {panic(err)}
	fmt.Println(FindThree2020(numList))
}
