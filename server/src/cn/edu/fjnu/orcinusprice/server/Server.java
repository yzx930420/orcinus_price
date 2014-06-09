package cn.edu.fjnu.orcinusprice.server;

import cn.edu.fjnu.orcinusprice.lucene.LuceneHelper;
import cn.edu.fjnu.orcinusprice.model.Request;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by frank93 on 6/9/14.
 */
public class Server {
    private static ServerSocket server = null;
    private static int port = 4700;

    public static void runServer() {
        try {
            server = new ServerSocket(port);
        } catch (IOException e) {
            e.printStackTrace();
        }

        while (true) {
            try {
                final Socket socket = server.accept();
                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        handle(socket);
                    }
                }).start();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private static void handle(final Socket socket) {

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            StringBuilder sb = new StringBuilder();
            String line = null;
            while((line = br.readLine()) != null) {
                sb.append(line);
            }
            br.close();
            //FIXME
            System.out.println(sb.toString());
            Request request = parserJson(sb.toString());

            LuceneHelper lh = new LuceneHelper();
            List<String> result = lh.search(request.getAction(), request.getKeyword(),
                    request.getIndex() + request.getSize());
            List<String> subResult = null;
            int start = request.getIndex();
            int end = request.getIndex() + request.getSize();
            end = end < result.size() ? end : result.size();
            if (start < end) {
                subResult = result.subList(start, end);
            } else {
                subResult = new ArrayList<String>();
            }

            String resultJson = toJson(subResult);
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            bw.write(resultJson);
            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void free() {
        if (server != null)
            try {
                server.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
    }

    private static Request parserJson(String json) {
        return null;
    }

    private static String toJson(List<String> l){
        return null;
    }
}
