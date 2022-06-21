import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SplitRegexTry {
    private static final Pattern NUMERIC_INDEX_REGEX = Pattern.compile("\\d+");
    public static void main(String[] args) {
//        String str = "a|b||c|d";
//        String[] parts = str.split("[|]");
//        for (String part : parts) {
//            System.out.println(part);
//        }
        String indexString = "A";
        final Matcher matcher = NUMERIC_INDEX_REGEX.matcher(indexString);
        final int index = matcher.find() ? Integer.parseInt(matcher.group()) : -1;
//        Boolean b1 = null;
//        if(!b1) System.out.println("null equal false");
//        String[] nums = {"1.234", "1.23", "1.20", "-1", "1.0"};
//        float ans =0;
//        for (String num : nums) {
//            System.out.println(String.format("%f", Float.parseFloat(num)));
//            System.out.println(Float.parseFloat(num));
//            System.out.println(num);
//            ans += Float.parseFloat(num);
//        }
//
//        System.out.println(ans);
//        System.out.println();
    }
}
