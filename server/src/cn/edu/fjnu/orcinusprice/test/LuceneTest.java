package cn.edu.fjnu.orcinusprice.test;

import cn.edu.fjnu.orcinusprice.lucene.LuceneHelper;

/**
 * Created by frank93 on 6/10/14.
 */
public class LuceneTest {
    public static void main(String[] args) {
        LuceneHelper lh = new LuceneHelper();
        lh.UpdateIndex();
    }
}
