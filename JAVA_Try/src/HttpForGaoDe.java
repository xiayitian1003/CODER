import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class HttpForGaoDe {
    private static final Object KEY = "86959160eb68570d15ae3236db7aa989";
    private static final String BASE_PATH = "https://restapi.amap.com/v3";

    public static void main(String[] args) {
        try {
            syncGet();
        } catch (InterruptedException | IOException e) {
            e.printStackTrace();
        }
    }
    public static void syncGet() throws InterruptedException, IOException {
        String address = "阿比让";
//        address = URLEncoder.encode(address, "utf-8");

        String jsonUrl = BASE_PATH + "/geocode/geo?address=" + address + "&output=json&key="+ KEY;
        String xmlUrl = BASE_PATH + "/geocode/geo?address=" + address + "&output=XML&key="+ KEY;
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                            .GET()
                            .uri(URI.create(jsonUrl))
//                            .uri(URI.create("/geocode/geo?address=北京&city&output=XML&key=<>"))
                            .build();
        HttpResponse<String> response =
                client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println(response.body());
    }
}
