//public class InteruptThread {
//    public static void main(String[] args) throws InterruptedException {
//        Thread t = new MyThread();
//        t.start();
//        Thread.sleep(1); // 暂停1毫秒
//        t.interrupt(); // 中断t线程
//        t.join(); // 等待t线程结束
//        System.out.println("end");
//    }
//}
//
//class MyThread extends Thread {
//    public void run() {
//        int n = 0;
//        while (! isInterrupted()) {
//            n ++;
//            System.out.println(n + " hello!");
//        }
//    }
//}
    public class InteruptThread {
        public static void main(String[] args) throws InterruptedException {
            Thread t = new MyThread();
            t.start();
            System.out.println("good");
            Thread.sleep(1000);
            t.interrupt(); // 中断t线程
            t.join(); // 等待t线程结束
            System.out.println("end");
        }
    }

    class MyThread extends Thread {
        public void run() {
            Thread hello = new HelloThread();
            hello.start(); // 启动hello线程
            try {
                hello.join(); // 等待hello线程结束
            } catch (InterruptedException e) {
                System.out.println("MyThread interrupted!");
            }
            hello.interrupt();
        }
    }

    class HelloThread extends Thread {
        public void run() {
            int n = 0;
            while (!isInterrupted()) {
                n++;
                System.out.println(n + " hello!");
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    System.out.println("HelloThread interrupted!");
                    break;
                }
            }
        }
    }
//public class InteruptThread {
//    public static void main(String[] args)  throws InterruptedException {
//        HelloThread t = new HelloThread();
//        t.start();
//        Thread.sleep(1);
//        t.running = false; // 标志位置为false
//    }
//}
//
//class HelloThread extends Thread {
//    public volatile boolean running = true;
//    public void run() {
//        int n = 0;
//        while (running) {
//            n ++;
//            System.out.println(n + " hello!");
//        }
//        System.out.println("end!");
//    }
//}