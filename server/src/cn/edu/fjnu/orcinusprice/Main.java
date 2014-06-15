package cn.edu.fjnu.orcinusprice;

import cn.edu.fjnu.orcinusprice.lucene.LuceneHelper;
import cn.edu.fjnu.orcinusprice.server.Server;

/**
 * Created by frank93 on 6/10/14.
 */
public class Main {
    private static Server server = null;
    private static long sleep_ms = 12 * 3600 * 1000;


    public static void main(String[] args) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    LuceneHelper lh = new LuceneHelper();
                    lh.UpdateIndex();
                    try {
                        Thread.sleep(sleep_ms);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }

        });

        server = new Server();
        server.runServer();
    }
}
