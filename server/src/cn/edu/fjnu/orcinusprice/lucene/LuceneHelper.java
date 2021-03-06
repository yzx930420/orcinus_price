package cn.edu.fjnu.orcinusprice.lucene;

import cn.edu.fjnu.orcinusprice.Setting;
import cn.edu.fjnu.orcinusprice.model.BookIndex;
import cn.edu.fjnu.orcinusprice.utils.MysqlHelper;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.index.*;
import org.apache.lucene.queryParser.ParseException;
import org.apache.lucene.queryParser.QueryParser;
import org.apache.lucene.search.*;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.Version;
import org.wltea.analyzer.lucene.IKAnalyzer;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by frank93 on 5/16/14.
 */
public class LuceneHelper {
    private static IndexReader reader = null;
    private static Directory dir = null;
    private static String path = Setting.INDEX_PATH;
    private static MysqlHelper mysqlHelper = null;
    private static final int QueryNum = 100;

    public LuceneHelper() {
//        try {
//            reader = IndexReader.open(dir);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
        File indexDir = new File(path);
        try {
            dir = FSDirectory.open(indexDir);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private void getSearcher() {
    }

    private IndexReader getReader() {
        if (reader == null) {
            try {
                reader = IndexReader.open(dir);
            } catch (IOException e) {
                e.printStackTrace();
            }
            return reader;
        }

        IndexReader tr = null;
        try {
            tr = IndexReader.openIfChanged(reader);
            if (tr != null) {
                reader.close();
                reader = tr;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        return reader;
    }

    public void UpdateIndex() {
        IndexWriterConfig iwc = new IndexWriterConfig(Version.LUCENE_35, new IKAnalyzer());
        IndexWriter writer = null;
        try {
            writer = new IndexWriter(dir, iwc);
            writer.deleteAll();
            mysqlHelper.getConnection();
            List<BookIndex> bil = mysqlHelper.queryAll();
            for (BookIndex bi : bil) {
                Document doc = new Document();
                doc.add(new Field("isbn", bi.getIsbn(), Field.Store.YES, Field.Index.NOT_ANALYZED_NO_NORMS));
                doc.add(new Field("author", bi.getAuthor(), Field.Store.NO, Field.Index.ANALYZED_NO_NORMS));
                doc.add(new Field("title", bi.getTitle(), Field.Store.NO, Field.Index.ANALYZED_NO_NORMS));
                writer.addDocument(doc);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (writer != null)
                try {
                    writer.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
        }

    }

    public List<String> search(String key, String value) {
        if (key == null) {
            System.out.println("key is null");
            return new ArrayList<String>();
        }
        if (value == null) {
            System.out.println("value is null");
            return new ArrayList<String>();
        }
        if (key.length() == 0) {
            System.out.println("length of key is 0");
            return new ArrayList<String>();
        }
        if (value.length() == 0) {
            System.out.println("length of value is 0");
            return new ArrayList<String>();
        }
        IndexSearcher searcher = null;
        searcher = new IndexSearcher(getReader());
        int num = getReader().maxDoc();
        if (searcher == null) {
            System.out.println("searcher is null!");
            return null;
        }
        QueryParser parser = new QueryParser(Version.LUCENE_35, key, new IKAnalyzer());
        Query query = null;
        try {
            query = parser.parse(value);
            System.out.println("query: " + query.toString());
        } catch (ParseException e) {
            e.printStackTrace();
        }

        List<String> isbnList = new ArrayList<String>();
        if (query == null) {
            System.out.println("query is null");
            return isbnList;
        }
        try {
            TopDocs tds = searcher.search(query, num);

            for (ScoreDoc sd : tds.scoreDocs) {
                Document doc = searcher.doc(sd.doc);
                isbnList.add(doc.get("isbn"));
                System.out.println(doc.get("isbn"));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        return isbnList;
    }


}
