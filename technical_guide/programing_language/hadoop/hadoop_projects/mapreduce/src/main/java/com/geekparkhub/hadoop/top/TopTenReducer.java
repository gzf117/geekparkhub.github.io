package com.geekparkhub.hadoop.top;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;
import java.util.TreeMap;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TopTenReducer
 * <p>
 */

public class TopTenReducer extends Reducer<NullWritable, Text, NullWritable, Text> {

    /**
     * Define a Tree Map as a container for storing data, sorted by key
     * 定义一个TreeMap作为存储数据的容器,按key排序
     */
    private TreeMap<TopFlowBean, Text> flowMap = new TreeMap<TopFlowBean, Text>();

    @Override
    protected void reduce(NullWritable key, Iterable<Text> values, Context context) throws IOException, InterruptedException {

        /**
         * Loop traversal
         * 循环遍历
         */
        for (Text value : values) {
            TopFlowBean bean = new TopFlowBean();
            bean.setPhoneNum(value.toString().split(" ")[0]);
            bean.setSumFlow(Long.valueOf(value.toString().split(" ")[3]));
            flowMap.put(bean, new Text(value));

            /**
             * Limit the amount of data in the Tree Map. If there are more than 10 data, delete the data with the smallest traffic.
             * 限制TreeMap的数据量,超过10条就删除掉流量最小的一条数据
             */
            if (flowMap.size() > 10) {
                flowMap.remove(flowMap.firstKey());
            }
        }

        /**
         * Write data
         * 写出数据
         */
        for (Text value : flowMap.descendingMap().values()) {
            context.write(NullWritable.get(), value);
        }
    }
}
