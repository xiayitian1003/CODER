import java.text.DateFormatSymbols;
import java.util.*;

import static java.lang.Integer.parseInt;
import static java.util.Calendar.*;


public class WeekDaysTry {
    private static final int ALL_DAYS = 0x7F;
    private int mBits;
    private static final Map<Integer, Integer> sCalendarDayToBit;

    static {
        sCalendarDayToBit = Map.of(MONDAY, 0x01, TUESDAY, 0x02, WEDNESDAY, 0x04, THURSDAY,
                0x08, FRIDAY, 0x10, SATURDAY, 0x20, SUNDAY, 0x40);
    }

    public enum Order {
        SAT_TO_FRI(SATURDAY, SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY),
        SUN_TO_SAT(SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY),
        MON_TO_SUN(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY);

        private final List<Integer> mCalendarDays;

        Order(Integer... calendarDays) {
            mCalendarDays = Arrays.asList(calendarDays);
        }

        public List<Integer> getCalendarDays() {
            return mCalendarDays;
        }
    }

    public WeekDaysTry(int bits) {
        // Mask off the unused bits.
        mBits = ALL_DAYS & bits;
    }

    public boolean isBitOn(int calendarDay) {
        final Integer bit = sCalendarDayToBit.get(calendarDay);
        if (bit == null) {
            throw new IllegalArgumentException(calendarDay + " is not a valid weekday");
        }
        return (mBits & bit) > 0;
    }

    public boolean isRepeating() {
        return mBits != 0;
    }

    public String toNewString(Order order) {
        if (!isRepeating()) {
            return "仅响一次";
        }

        if (mBits == ALL_DAYS) {
            return "每天";
        }

        int length = 0;
        List<Integer> orderWeekdays = order.getCalendarDays();

        final DateFormatSymbols dfs = new DateFormatSymbols();
        final String[] weekdays = dfs.getShortWeekdays();
        final StringBuilder builder = new StringBuilder(40);

        for (int i = 0; i < orderWeekdays.size(); i++) {
            int calendarDay = orderWeekdays.get(i);
            if (isBitOn(calendarDay)) {
                if (builder.length() > 0) {
                    builder.append(",");
                }
                int j = i;
                while (j < orderWeekdays.size() && isBitOn(orderWeekdays.get(j))) {
                    length++;
                    j++;
                }
                if (length == 1) {
                    builder.append(weekdays[calendarDay]);
                } else if (length == 2) {
                    builder.append(weekdays[calendarDay] + "," + weekdays[orderWeekdays.get(i + 1)]);
                } else if (length > 2) {
                    builder.append(weekdays[calendarDay] + "to" + weekdays[orderWeekdays.get(j - 1)]);
                }
                i = j - 1;
                length = 0;
            }
        }

        return builder.toString();
    }
//    public void toNewString(int Bits, Order order){
//        int length = 0;
//        List<Integer> orderWeekdays = order.getCalendarDays();
//        System.out.println("-----------for-each-----------");
//        for (int calendarDay : orderWeekdays) {
//            System.out.println(calendarDay);
////            if(isBitOn(calendarDay)){
////                length ++;
////            }else {
////                if(length > 2)
////
////                length = 0;
////            }
//        }
//        System.out.println("-----------array-index-----------");
//        for(int i = 0;i < orderWeekdays.size();i ++){
//            System.out.println(orderWeekdays.get(i));
//        }
//        System.out.println("-----------------next------------------");
//    }
}
