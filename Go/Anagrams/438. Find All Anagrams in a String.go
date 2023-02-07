package main

import (
	"fmt"
)

func findAnagrams(s string, p string) []int {

	Ans := []int{}
	if len(s) < len(p) {
		return Ans
	}
	m1 := make([]int, 26)
	m2 := make([]int, 26)
	for i := range p {
		m1[p[i]-'a']++
		m2[s[i]-'a']++
	}
	var matches int
	for i := range m1 {
		if m1[i] == m2[i] {
			matches++
		}
	}
	for i := len(p); i <= len(s); i++ {
		if matches == 26 {
			Ans = append(Ans, i-len(p)+1)
		}
		if i == len(s) {
			break
		}
		l := s[i-len(p)] - 'a'
		r := s[i] - 'a'
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
	return Ans
}
func main() {
	fmt.Println(findAnagrams("baa", "aa"))
	fmt.Println(findAnagrams("abab", "ab"))
}
