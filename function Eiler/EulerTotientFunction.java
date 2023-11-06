public class EulerTotientFunction { //реализацию функции Эйлера
    public static int phi(int n) { //функции Эйлера (функции тотиента) для числа n. Метод возвращает целое число
        int result = n; //для хранения результата функции Эйлера
        
        for (int i = 2; i * i <= n; ++i) { //выполняется от i = 2 до тех пор, пока i * i меньше или равно n. Этот цикл итерируется по потенциальным делителям числа n.
            if (n % i == 0) {
                while (n % i == 0) {
                    n /= i; //убирает все множители i из n.
                }
                result -= result / i;
            }
        }
        
        if (n > 1) {
            result -= result / n;
        }
        
        return result;
    }
}
