package cn.edu.fjnu.orcinusprice.test;

import cn.edu.fjnu.orcinusprice.model.Request;
import cn.edu.fjnu.orcinusprice.server.Server;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by frank93 on 6/15/14.
 */
public class TestJSON {
    public static void main(String[] args){
        testToJson();
        testFromJson();
    }

    public  static void testFromJson(){
        /*
        *    "action='" + action + '\'' +
                ", keyword='" + keyword + '\'' +
                ", index=" + index +
                ", size=" + size +
                '}';
        * */
        String json = "{ 'action':\"any\", 'keyword':'Linux', 'index':10, 'size':100}";
        Request request = Server.parserJson(json);
        System.out.println(""+request);
    }

    public  static void testToJson(){
        List<String> list = new ArrayList<String>();
        list.add("1[\"");
        list.add("2");
        list.add("3");
        System.out.println(Server.toJson(list));
    }
}
