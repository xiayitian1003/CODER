import java.util.Calendar;

public class CalendarLearn {
    public static void printCalendar(Calendar calendar, String  name){
        printCalendar(calendar.toString(), name);
    }
    public static void printCalendar(String string, String name){
        char[] strarray= string.toCharArray();
        System.out.println("----------------StartPrint " + name + "----------------");
        for(int i = 0;i < string.length();i ++){
            System.out.print(strarray[i]);
            if(strarray[i] == ',') System.out.println(" ");
        }
        System.out.println(" ");
        System.out.println("----------------EndPrint " + name + "----------------");
    }
    public static void main(String[] args) {
        Calendar calendar = Calendar.getInstance();
        System.out.println("print calendar:");
        System.out.println(calendar.getTime());
        System.out.println(calendar.getFirstDayOfWeek());
        System.out.println(calendar.getCalendarType());
        System.out.println(calendar.getTimeZone());
        System.out.println(calendar.getTimeInMillis());
        System.out.println("----------------Calendar.get----------------");
        System.out.println("MONTH = " + calendar.get(Calendar.MONTH));
        System.out.println("DATE = " + calendar.get(Calendar.DATE));
        System.out.println("HOUR = " + calendar.get(Calendar.HOUR));
        System.out.println("SECOND = " + calendar.get(Calendar.SECOND));
        System.out.println("MILLISECOND = " + calendar.get(Calendar.MILLISECOND));
        System.out.println("DAY_OF_MONTH = " + calendar.get(Calendar.DAY_OF_MONTH));
        System.out.println("DAY_OF_WEEK = " + calendar.get(Calendar.DAY_OF_WEEK));
        System.out.println("DAY_OF_YEAR = " + calendar.get(Calendar.DAY_OF_YEAR));
        System.out.println("FirstDayOfWeek = " + Calendar.getInstance().getFirstDayOfWeek());

        System.out.println("----------------Calendar-DAY_OF_YEAR-CHANGE-START----------------");
        printCalendar(calendar, "calendar");
        System.out.println("DAY_OF_YEAR = " + calendar.get(Calendar.DAY_OF_YEAR));
        calendar.add(Calendar.DAY_OF_WEEK, 10);
        System.out.println("----------------Calendar-DAY_OF_YEAR-CHANGE----------------");
        printCalendar(calendar, "calendar");

//        String currenttime = "java.util.GregorianCalendar[time=1641245723930,areFieldsSet=true,areAllFieldsSet=true,lenient=true,zone=libcore.util.ZoneInfo[mDstSavings=0,mUseDst=false,mDelegate=[id=\"Asia/Shanghai\",mRawOffset=28800000,mEarliestRawOffset=29143000,transitions=29]],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2022,MONTH=0,WEEK_OF_YEAR=2,WEEK_OF_MONTH=2,DAY_OF_MONTH=4,DAY_OF_YEAR=4,DAY_OF_WEEK=3,DAY_OF_WEEK_IN_MONTH=1,AM_PM=0,HOUR=5,HOUR_OF_DAY=5,MINUTE=35,SECOND=23,MILLISECOND=930,ZONE_OFFSET=28800000,DST_OFFSET=0]";
//        String nextInstanceTime = "java.util.GregorianCalendar[time=1641332040000,areFieldsSet=true,areAllFieldsSet=true,lenient=true,zone=libcore.util.ZoneInfo[mDstSavings=0,mUseDst=false,mDelegate=[id=\"Asia/Shanghai\",mRawOffset=28800000,mEarliestRawOffset=29143000,transitions=29]],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2022,MONTH=0,WEEK_OF_YEAR=2,WEEK_OF_MONTH=2,DAY_OF_MONTH=5,DAY_OF_YEAR=5,DAY_OF_WEEK=4,DAY_OF_WEEK_IN_MONTH=1,AM_PM=0,HOUR=5,HOUR_OF_DAY=5,MINUTE=34,SECOND=0,MILLISECOND=0,ZONE_OFFSET=28800000,DST_OFFSET=0]";
//        String currentTime = "java.util.GregorianCalendar[time=1641247305501,areFieldsSet=true,areAllFieldsSet=true,lenient=true,zone=libcore.util.ZoneInfo[mDstSavings=0,mUseDst=false,mDelegate=[id=\"Asia/Shanghai\",mRawOffset=28800000,mEarliestRawOffset=29143000,transitions=29]],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2022,MONTH=0,WEEK_OF_YEAR=2,WEEK_OF_MONTH=2,DAY_OF_MONTH=4,DAY_OF_YEAR=4,DAY_OF_WEEK=3,DAY_OF_WEEK_IN_MONTH=1,AM_PM=0,HOUR=6,HOUR_OF_DAY=6,MINUTE=1,SECOND=45,MILLISECOND=501,ZONE_OFFSET=28800000,DST_OFFSET=0]";
//        String nextInstanceTime = "java.util.GregorianCalendar[time=1641333660000,areFieldsSet=true,areAllFieldsSet=true,lenient=true,zone=libcore.util.ZoneInfo[mDstSavings=0,mUseDst=false,mDelegate=[id=\"Asia/Shanghai\",mRawOffset=28800000,mEarliestRawOffset=29143000,transitions=29]],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2022,MONTH=0,WEEK_OF_YEAR=2,WEEK_OF_MONTH=2,DAY_OF_MONTH=5,DAY_OF_YEAR=5,DAY_OF_WEEK=4,DAY_OF_WEEK_IN_MONTH=1,AM_PM=0,HOUR=6,HOUR_OF_DAY=6,MINUTE=1,SECOND=0,MILLISECOND=0,ZONE_OFFSET=28800000,DST_OFFSET=0]";
//        String addDays_getDistanceToNextDay = "java.util.GregorianCalendar[time=1641333660000,areFieldsSet=true,areAllFieldsSet=true,lenient=true,zone=libcore.util.ZoneInfo[mDstSavings=0,mUseDst=false,mDelegate=[id=\"Asia/Shanghai\",mRawOffset=28800000,mEarliestRawOffset=29143000,transitions=29]],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2022,MONTH=0,WEEK_OF_YEAR=2,WEEK_OF_MONTH=2,DAY_OF_MONTH=5,DAY_OF_YEAR=5,DAY_OF_WEEK=4,DAY_OF_WEEK_IN_MONTH=1,AM_PM=0,HOUR=6,HOUR_OF_DAY=6,MINUTE=1,SECOND=0,MILLISECOND=0,ZONE_OFFSET=28800000,DST_OFFSET=0]";
//        String DaylightSavingsTime = "java.util.GregorianCalendar[time=?,areFieldsSet=false,areAllFieldsSet=true,lenient=true,zone=libcore.util.ZoneInfo[mDstSavings=0,mUseDst=false,mDelegate=[id=\"Asia/Shanghai\",mRawOffset=28800000,mEarliestRawOffset=29143000,transitions=29]],firstDayOfWeek=1,minimalDaysInFirstWeek=1,ERA=1,YEAR=2022,MONTH=0,WEEK_OF_YEAR=2,WEEK_OF_MONTH=2,DAY_OF_MONTH=5,DAY_OF_YEAR=5,DAY_OF_WEEK=4,DAY_OF_WEEK_IN_MONTH=1,AM_PM=0,HOUR=6,HOUR_OF_DAY=6,MINUTE=1,SECOND=0,MILLISECOND=0,ZONE_OFFSET=28800000,DST_OFFSET=0]";
//        String alarmInstance = "AlarmInstance{mId=-1, mYear=2022, mMonth=0, mDay=5, mHour=7, mMinute=22, mLabel=闹钟, mVibrate=true, mRingtone=content://settings/system/alarm_alert, mAlarmId=14, mAlarmState=0, mIsMuslimsAlarm=false, snoozeDuration=10}";

//        printCalendar(currentTime, "currenttime");
//        printCalendar(nextInstanceTime, "nextInstanceTime");
//        printCalendar(addDays_getDistanceToNextDay,"addDays_getDistanceToNextDay");
//        printCalendar(DaylightSavingsTime, "DaylightSavingsTime");
//        printCalendar(alarmInstance, "alarmInstance");
    }
}
