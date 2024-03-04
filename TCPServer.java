import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class TCPServer {

    private static final int PORT = 4711;

    private void startServer() {

        try(ServerSocket ss = new ServerSocket(PORT)) {

            try(Socket s = ss.accept();
                BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
                BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));) {

                bw.write("Hi Client, schön dich zu sehen!\n");

                }
            } catch (IOException ex) {
                System.err.println(ex);
            }
    }

    public static void main(String[] args) {
        (new TCPServer()).startServer();
    }
}
