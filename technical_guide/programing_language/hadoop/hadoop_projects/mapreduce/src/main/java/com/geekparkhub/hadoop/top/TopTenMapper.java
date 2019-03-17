package com.geekparkhub.hadoop.top;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

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
 * TopTenMapper
 * <p>
 */

public class TopTenMapper extends Mapper<LongWritable, Text, NullWritable, Text> {

    /**
     * Define a Tree Map as a container for storing data, sorted by key
     * 定义一个TreeMap作为存储数据的容器,按key排序
     */
    private TreeMap<TopFlowBean, Text> flowMap = new TreeMap<TopFlowBean, Text>();

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        TopFlowBean bean = new TopFlowBean();

        /**
         * Get a row of data
         * 获取一行数据
         */
        String line = value.toString();

        /**
         * Cutting data
         * 切割数据
         */
        String[] split = line.split(" ");

        /**
         * Get total traffic
         * 获取总流量
         */
        long sumFlow = Long.parseLong(split[3]);

        /**
         * Package object
         * 封装对象
         */
        bean.setSumFlow(sumFlow);
        bean.setPhoneNum(split[0]);

        /**
         * Add data to the Tree Map
         * 向TreeMap中添加数据
         */
        flowMap.put(bean, new Text(value));

        /**
         * Limit the amount of data in the Tree Map. If there are more than 10 data, delete the data with the smallest traffic.
         * 限制TreeMap的数据量,超过10条就删除掉流量最小的一条数据
         */
        if (flowMap.size() > 10) {
            flowMap.remove(flowMap.firstKey());
        }
    }

    @Override
    protected void cleanup(Context context) throws IOException, InterruptedException {
        for (Text v : flowMap.values()) {
            context.write(NullWritable.get(), v);
        }
    }
}
