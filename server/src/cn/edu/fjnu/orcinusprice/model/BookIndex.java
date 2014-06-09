package cn.edu.fjnu.orcinusprice.model;

/**
 * Created by frank93 on 6/9/14.
 */
public class BookIndex {
    private String isbn;
    private String title;
    private String author;

    public BookIndex() {
    }
    public BookIndex(String isbn, String title, String author) {
        this.isbn = isbn;
        this.title = title;
        this.author = author;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
}
