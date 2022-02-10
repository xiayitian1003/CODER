class Main {
    public static void main(String[] args) {
//        WeekDaysTry weekDaysTry = new WeekDaysTry(0x03);
//        WeekDaysTry weekDaysTry2 = new WeekDaysTry(0x07);
//        WeekDaysTry weekDaysTry3= new WeekDaysTry(0x0E);
        for (int i = 0; i <= 128; i++) {
            WeekDaysTry weekDaysTry = new WeekDaysTry(i);
            System.out.println(i + "----------" + Integer.toBinaryString(i) + "----------");
            System.out.println(weekDaysTry.toNewString(WeekDaysTry.Order.MON_TO_SUN));
            System.out.println(weekDaysTry.toNewString(WeekDaysTry.Order.SUN_TO_SAT));
            System.out.println(weekDaysTry.toNewString(WeekDaysTry.Order.SAT_TO_FRI));
            System.out.println("-----------end-----------");
        }
    }
}