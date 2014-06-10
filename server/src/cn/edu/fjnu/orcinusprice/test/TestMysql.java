package cn.edu.fjnu.orcinusprice.test;

import cn.edu.fjnu.orcinusprice.utils.MysqlHelper;
import com.sun.swing.internal.plaf.metal.resources.metal_zh_HK;

/**
 * Created by frank93 on 6/9/14.
 */
public class TestMysql {
    public static void main(String[] args) {
        MysqlHelper mh = new MysqlHelper();
        long start = System.currentTimeMillis();
        mh.getConnection();
        mh.queryAll();
        long end = System.currentTimeMillis();
        System.out.println(end - start + "ms");


    }
}
