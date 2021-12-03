public class UpThenDown {
    public static void main(String[] args) {
        Object_to_StringNULL a = new Object_to_StringNULL();
        a.name = "xyt_win";
        Object test = a;
        upanddown(test);
    }
    public static void upanddown(Object x){
        Object_to_StringNULL a = (Object_to_StringNULL) x;
        System.out.println(a.name);
    }
}

