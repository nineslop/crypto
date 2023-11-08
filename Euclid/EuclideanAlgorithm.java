public class EuclideanAlgorithm {
    public static int findGCD(int a, int b) {
        System.out.println("Начало вычислений:");
        while (b != 0) {
            int quotient = a / b;
            int remainder = a % b;
            System.out.println(a + " / " + b + " = " + quotient + " (остаток " + remainder + ")");
            a = b;
            b = remainder;
        }
        System.out.println("Конец вычислений:");
        return a;
    }
}