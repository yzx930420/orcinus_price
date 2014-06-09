package cn.edu.fjnu.orcinusprice.utils;

import cn.edu.fjnu.orcinusprice.model.BookIndex;

import java.sql.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * Created by frank93 on 5/16/14.
 */
public class MysqlHelper {

    private static final String URL = "jdbc:mysql://127.0.0.1:3306/test";
    private static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
    private static String USER_NAME = "root";
    private static String PASSWORD = "123456";

    static {
        try {
            Class.forName(JDBC_DRIVER);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static Connection getConnection() {
        Connection conn = null;
        try {
            conn = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return conn;
    }

    public static List<BookIndex> queryAll() {
        Connection conn = getConnection();

        try {
            List<BookIndex> bil = new ArrayList<BookIndex>();
            PreparedStatement ps = conn.prepareStatement("select isbn, title, author from book_info");
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                String isbn = rs.getString("isbn");
                String title = rs.getString("title");
                String author = rs.getString("author");
                bil.add(new BookIndex(isbn, title, author));
            }
            free(rs, ps, conn);
            return bil;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;

    }


    public  static void free(ResultSet rs, Statement stat, Connection conn){
        if(rs != null) {
            try {
                rs.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        if (stat != null)
            try {
                stat.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        if (conn != null)
            try {
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
    }

}
