package main

import (
	"fmt"
)

func checkInclusion(s1 string, s2 string) bool {
	if len(s2) < len(s1) {
		return false
	}
	m1 := make([]int, 26)
	m2 := make([]int, 26)
	for i := range s1 {
		m1[s1[i]-'a']++
		m2[s2[i]-'a']++
	}
	var matches int
	for i := range m1 {
		if m1[i] == m2[i] {
			matches++
		}
	}
	for i := len(s1); i < len(s2); i++ {
		if matches == 26 {
			return true
		}
		l := s2[i-len(s1)] - 'a'
		r := s2[i] - 'a'
		m2[r]++
		if m2[r] == m1[r] {
			matches++
		} else if m2[r] == m1[r]+1 {
			matches--
		}
		m2[l]--
		if m2[l] == m1[l] {
			matches++
		} else if m2[l] == m1[l]-1 {
			matches--

		}
	}
	return matches == 26
}
func main() {
	fmt.Println(checkInclusion("adc", "dcda"))
	fmt.Println(checkInclusion("ab", "eidboaoo"))
}
