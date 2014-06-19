package cn.edu.fjnu.orcinusprice.test;

import cn.edu.fjnu.orcinusprice.lucene.LuceneHelper;
import cn.edu.fjnu.orcinusprice.utils.MysqlHelper;

import java.util.List;

/**
 * Created by frank93 on 6/10/14.
 */
public class LuceneTest {
    public static void main(String[] args) {
        test2();
    }
    public static void test1() {
        LuceneHelper lh = new LuceneHelper();
        lh.UpdateIndex();
    }
    public static void test2() {
        LuceneHelper lh = new LuceneHelper();
        List<String> rs = lh.search("title", "");
        MysqlHelper mh = new MysqlHelper();
        mh.getConnection();
        for (String s : rs) {
            mh.queryByIsbn(s);
        }
        System.out.println("pass");
    }
    public static void test3() {
        LuceneHelper lh = new LuceneHelper();
        List<String> rs = lh.search("title", "实战lucene");
        MysqlHelper mh = new MysqlHelper();
        mh.getConnection();
        for (String s : rs) {
            mh.queryByIsbn(s);
        }
        System.out.println("pass");
    }
}
