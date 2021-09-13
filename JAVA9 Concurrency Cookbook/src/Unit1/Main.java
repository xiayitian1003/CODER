package Unit1;

public class Main {
    public static void main(String[] args) {
        System.out.println("Min Priority is " + Thread.MIN_PRIORITY);
        System.out.println("Min Priority is " + Thread.NORM_PRIORITY);
        System.out.println("Min Priority is " + Thread.MAX_PRIORITY);

        Thread threads[];
        Thread.State states[];
        threads = new Thread[10];
        for (int i = 0;i < 10; i++){
            threads[i] = new Thread(new Calculator());
            if (i % 2 == 0)

        }

    }
}
