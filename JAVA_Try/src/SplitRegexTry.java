public class SplitRegexTry {

    public static void main(String[] args) {
        String str = "a|b||c|d";
        String[] parts = str.split("[|]");
        for (String part : parts) {
            System.out.println(part);
        }
        String[] nums = {"1.234", "1.23", "1.20", "-1", "1.0"};
        float ans =0;
        for (String num : nums) {
            System.out.println(num);
            ans += Float.parseFloat(num);
        }
        System.out.println(ans);
        System.out.println();
    }
}
