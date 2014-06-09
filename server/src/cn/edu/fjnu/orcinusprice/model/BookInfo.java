package cn.edu.fjnu.orcinusprice.model;

import java.util.List;
import java.util.Objects;

/**
 * Created by frank93 on 5/16/14.
 */
public class BookInfo {
    private String isbn;
    private double price;
    private String title;
    private String author;
    private String press;
    private String description;
    private String cover;
    private List<BookGoodsInfo> goodsList;

    public BookInfo() {
    }

}
