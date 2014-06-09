package cn.edu.fjnu.orcinusprice.lucene;

import cn.edu.fjnu.orcinusprice.model.BookIndex;
import cn.edu.fjnu.orcinusprice.utils.MysqlHelper;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.index.*;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.util.Version;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by frank93 on 5/16/14.
 */
public class LuceneHelper {
    private static IndexReader reader = null;
    private static Directory dir = null;
    private static MysqlHelper mysqlHelper = null;
    private static final int QueryNum = 100;

    public LuceneHelper() {
        try {
            reader = IndexReader.open(dir);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private void getSearcher() {
    }

    private IndexReader getReader() {
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
        IndexWriterConfig iwc = new IndexWriterConfig(Version.LUCENE_35, new StandardAnalyzer(Version.LUCENE_35));
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
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (writer != null)
                try {
                    writer.close();
                } catch (CorruptIndexException e) {
                    e.printStackTrace();
                }
        }

    }

    public List<String> search(String key, String value, int num) {
        IndexSearcher searcher = null;
        searcher = new IndexSearcher(getReader());
        if (searcher == null)
            return null;
        TermQuery query = new TermQuery(new Term(key, value));
        List<String> isbnList = new ArrayList<String>();
        try {
            TopDocs tds = searcher.search(query, num);

            for (ScoreDoc sd : tds.scoreDocs) {
                Document doc = searcher.doc(sd.doc);
                isbnList.add(doc.get("isbn"));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        return isbnList;
    }


}
