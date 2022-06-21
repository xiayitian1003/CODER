import java.text.CollationElementIterator;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

class Main {
    public static void main(String[] args) {
        String s1 = "good2" +
                "";
        String s2 = "good";
        System.out.println(s1.hashCode());
        System.out.println(Objects.hash(s1));
        System.out.println(s2.hashCode());
        System.out.println(Objects.hash(s2));
//        CalendarLearn point = new CalendarLearn();
//        System.out.println(point.getClass());
//        ArrayList<Integer> ListA = new ArrayList<Integer>();
//        ListA.add(1);ListA.add(2);ListA.add(3);
//        List<Integer> ListC = (List<Integer>) Collections.unmodifiableList(ListA);
//        ArrayList<Integer> ListB = new ArrayList<Integer>();
//        Collections.copy(ListB,ListC);
    }
    public static void strBuilderTry(){
        StringBuilder str = new StringBuilder();
        System.out.println(str);
    }

    public static void weekDayTry(){
        //        WeekDaysTry weekDaysTry = new WeekDaysTry(0x03);
//        WeekDaysTry weekDaysTry2 = new WeekDaysTry(0x07);
//        WeekDaysTry weekDaysTry3= new WeekDaysTry(0x0E);
//        for (int i = 0; i <= 128; i++) {
//            WeekDaysTry weekDaysTry = new WeekDaysTry(i);
//            System.out.println(i + "----------" + Integer.toBinaryString(i) + "----------");
//            System.out.println(weekDaysTry.toNewString(WeekDaysTry.Order.MON_TO_SUN));
//            System.out.println(weekDaysTry.toNewString(WeekDaysTry.Order.SUN_TO_SAT));
//            System.out.println(weekDaysTry.toNewString(WeekDaysTry.Order.SAT_TO_FRI));
//            System.out.println("-----------end-----------");
//        }
    }
}