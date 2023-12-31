import java.math.BigInteger;
import java.security.SecureRandom;

public class ElGamalEncryption {

    public static void main(String[] args) {
        BigInteger p = generateRandomNumberInRange(1, 31);
        BigInteger g = generateRandomNumberInRange(1, 31);
        BigInteger x = generateRandomNumberInRange(1, 31);

        BigInteger y = g.modPow(x, p);

        System.out.println("Открытый ключ (g, p, y): (" + g + ", " + p + ", " + y + ")");

        //шифр текст
        String originalMessage = "тот, кто ложится на два стула, падает на ребра.";

        BigInteger k = generateRandomNumberInRange(1, 31);

        //Шифрование
        String encryptedMessage = encrypt(originalMessage, k, g, y, p);

        System.out.println("Зашифрованное сообщение: " + encryptedMessage);

        //Расшифрование
        String decryptedMessage = decrypt(encryptedMessage, x, p);

        //Вывод расшифрованного сообщения
        System.out.println("Расшифрованное сообщение: " + decryptedMessage);
    }

    //Генерация случайного числа
    public static BigInteger generateRandomNumberInRange(int min, int max) {
        SecureRandom random = new SecureRandom();
        int range = max - min + 1;
        int randomNumber = random.nextInt(range) + min;
        return BigInteger.valueOf(randomNumber);
    }

    public static String encrypt(String message, BigInteger k, BigInteger g, BigInteger y, BigInteger p) {
        StringBuilder encryptedMessage = new StringBuilder();
        for (char c : message.toCharArray()) {
            BigInteger M = BigInteger.valueOf(c);
            BigInteger a = g.modPow(k, p);
            BigInteger b = y.modPow(k, p).multiply(M).mod(p);
            encryptedMessage.append(a).append(" ").append(b).append(" ");
        }
        return encryptedMessage.toString();
    }

    public static String decrypt(String encryptedMessage, BigInteger x, BigInteger p) {
        String[] tokens = encryptedMessage.split(" ");
        StringBuilder decryptedMessage = new StringBuilder();
        for (int i = 0; i < tokens.length; i += 2) {
            BigInteger a = new BigInteger(tokens[i]);
            BigInteger b = new BigInteger(tokens[i + 1]);
            BigInteger aInverse = a.modPow(x, p).modInverse(p);
            BigInteger M = b.multiply(aInverse).mod(p);
            decryptedMessage.append((char) M.intValue());
        }
        return decryptedMessage.toString();
    }
}
