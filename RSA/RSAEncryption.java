public class RSAEncryption {
    public static void main(String[] args) {
        String message = "тотзптктоложитсянадвастулазптпадаетнаребратчк";
        String russian_alp = "qабвгдежзийклмнопрстуфхцчшщъыьэюя";
        int E = 3;
        int N = 33;
        int D = 7;
        String[] arr = new String[message.length()];

        for (int i = 0; i < message.length(); i++) {
            char ch = message.charAt(i);
            int n = russian_alp.indexOf(ch);
            System.out.print(n + " ");
            String string = String.format("%02d", (int) (Math.pow(n, E) % N));
            arr[i] = string;
        }

        System.out.println();
        for (String str : arr) {
            int decrypted = (int) (Math.pow(Integer.parseInt(str), D) % N);
            System.out.print(russian_alp.charAt(decrypted));
        }
    }
}
