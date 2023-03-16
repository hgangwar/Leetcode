package main

import (
	"fmt"
)

func shuffle(nums []int, n int) []int {
	Ans := make([]int, 2*n)
	for i := 0; i < 2*n; i = i + 2 {
		ib2 := i / 2
		Ans[i] = nums[ib2]
		Ans[i+1] = nums[ib2+n]
	}
	return Ans
}
func main() {
	fmt.Println(shuffle([]int{2, 5, 1, 3, 4, 7}, 3))
	fmt.Println(shuffle([]int{1, 2, 3, 4, 4, 3, 2, 1}, 4))
	fmt.Println(shuffle([]int{1, 1, 2, 2}, 2))
}
