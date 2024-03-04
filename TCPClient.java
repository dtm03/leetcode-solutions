import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Calendar;

public class TCPClient {

    private void connect(String serverName, int port) {
        // Try-catch to make sure everything is closed
        try (Socket s = new Socket(serverName, port);
             // InputStreamReader to convert bytes to characters that are then read line by line by BufferedReader
             BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
             BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
        ) {

            // Send a GET request to the server (write part)
            bw.write("GET / HTTP/1.1\r\n");
            bw.write("Host: " + serverName + "\r\n\r\n");
            bw.flush();

            // Could also be implemented using a for loop
            while (br.readLine() != null) {
                System.out.println(br.readLine());
            }

        } catch (UnknownHostException ex) {
            System.err.println(ex);
        } catch (IOException ex) {
            System.err.println(ex);
        }
    }

    public static void main(String[] args) {
        // (new TCPClient()).connect("localhost", 4711);
        (new TCPClient()).connect("time.nist.gov", 13);
    }

}
