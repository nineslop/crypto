package main

import (
	"fmt"
)

func findGCD(a, b int) int {
	fmt.Println("Начало вычислений:")
	for b != 0 {
		quotient := a / b
		remainder := a % b
		fmt.Printf("%d / %d = %d (остаток %d)\n", a, b, quotient, remainder)
		a, b = b, remainder
	}
	fmt.Println("Конец вычислений:")
	return a
}

func main() {
	num1 := 1215
	num2 := 2755

	gcd := findGCD(num1, num2)

	fmt.Printf("Наибольший общий делитель чисел %d и %d равен %d\n", num1, num2, gcd)
}
