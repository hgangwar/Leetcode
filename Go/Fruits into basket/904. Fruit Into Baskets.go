package main

import (
	"fmt"
)

func totalFruit(fruits []int) int {
	count := 0
	Maxcount := 0
	lastX := 1
	X := -1
	Y := -1
	for ndx, x := range fruits {
		if X == -1 {
			X = x
		}
		if Y == -1 && x != X {
			Y = x
		}
		if x != X && x != Y && X != -1 && Y != -1 {
			if Maxcount < count {
				Maxcount = count
			}
			count = ndx - lastX
			if fruits[lastX] == X {
				Y = x
			} else {
				X = x
			}
		}

		if ndx > 0 {
			if fruits[ndx] != fruits[ndx-1] {
				lastX = ndx
			}
		}
		count++
	}
	if Maxcount < count {
		Maxcount = count
	}
	return Maxcount
}
func main() {
	fmt.Println(totalFruit([]int{3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4}))
}
