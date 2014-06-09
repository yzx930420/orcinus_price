package cn.edu.fjnu.orcinusprice.model;

/**
 * Created by frank93 on 6/9/14.
 */
public class Request {
    private String action; // author, title
    private String keyword;
    private int index; //开始下标
    private int size; // 个数

    public Request() {
    }

    public Request(String action, String keyword, int index, int size) {
        this.action = action;
        this.keyword = keyword;
        this.index = index;
        this.size = size;
    }

    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
}
