public class main {
    public static void main(String[] args) {
        int num1 = 1215;
        int num2 = 2755;

        int gcd = EuclideanAlgorithm.findGCD(num1, num2);

        System.out.println("Наибольший общий делитель чисел " + num1 + " и " + num2 + " равен " + gcd);
    }
}