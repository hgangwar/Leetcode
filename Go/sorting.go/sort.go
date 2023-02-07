package main

import (
	"fmt"
	"strings"
)

func count[T any](slice []T, f func(T) bool) int {
	count := 0
	for _, s := range slice {
		if f(s) {
			count++
		}
	}
	return count
}
func main() {
	s := []string{"ab", "ac", "de", "at", "gfb", "fr"}
	fmt.Println(
		count(
			s,
			func(x string) bool {
				return strings.Contains(x, "a")
			}),
	)

	s2 := []int{1, 2, 3, 4, 5, 6}
	fmt.Println(
		count(
			s2,
			func(x int) bool {
				return x%3 == 0
			}),
	)
}
