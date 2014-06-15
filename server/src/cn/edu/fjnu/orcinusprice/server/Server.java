package cn.edu.fjnu.orcinusprice.server;

import cn.edu.fjnu.orcinusprice.lucene.LuceneHelper;
import cn.edu.fjnu.orcinusprice.model.Request;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.sun.org.apache.xpath.internal.SourceTree;

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
            if (server == null) {
                server = new ServerSocket(port);
                System.out.println("Server is running!");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        while (true) {
            try {
                final Socket socket = server.accept();
                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        System.out.println(socket.getInetAddress());
                        handle(socket);
                        try {
                            System.out.println(socket.getInetAddress() + " close!");
                            socket.close();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
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
                System.out.println("recv: " + line);
                if (line.equals("end"))
                    break;
                sb.append(line);
            }

            //FIXME
            System.out.println("===" + sb.toString());
            Request request = parserJson(sb.toString());
            System.out.println("request: " + request);

            LuceneHelper lh = new LuceneHelper();
            System.out.println("search begin!");
            List<String> result = lh.search(request.getAction(), request.getKeyword());
            System.out.println("search end!");
            List<String> subResult = null;
            int start = request.getIndex();
            int end = request.getIndex() + request.getSize();
            end = end < result.size() ? end : result.size();
            if (start < end) {
                subResult = result.subList(start, end);
            } else {
                subResult = new ArrayList<String>();
            }
            System.out.println("start: " + start + " end: " + end);
            System.out.println("subResult: " + subResult);
            subResult.add(Integer.toString(result.size()));

            String resultJson = toJson(subResult);
            System.out.println("hehe");
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            System.out.println("haha");
            bw.write(resultJson);
            System.out.println("result json: " + resultJson);

            //br.close();
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

    public static Request parserJson(String json) {
        Gson gson = new Gson();
        Request request = gson.fromJson(json,Request.class);
        return request;
    }

    public static String toJson(List<String> l){
        Gson gson = new Gson();
        System.out.println("isbn list=   "+l);
        String json = gson.toJson(l);
        return json;
    }
}
