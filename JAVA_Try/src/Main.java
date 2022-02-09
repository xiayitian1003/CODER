class Main {
    public static void main(String[] args) {
        WeekDaysTry weekDaysTry = new WeekDaysTry(0x03);
        WeekDaysTry weekDaysTry2 = new WeekDaysTry(0x07);
        WeekDaysTry weekDaysTry3= new WeekDaysTry(0x09);
        System.out.println(weekDaysTry.toNewString(WeekDaysTry.Order.MON_TO_SUN));
        System.out.println(weekDaysTry.toNewString(WeekDaysTry.Order.SUN_TO_SAT));
        System.out.println(weekDaysTry.toNewString(WeekDaysTry.Order.SAT_TO_FRI));
    }
}