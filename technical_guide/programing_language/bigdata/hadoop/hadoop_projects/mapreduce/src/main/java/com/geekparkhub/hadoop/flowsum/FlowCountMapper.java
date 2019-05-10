package com.geekparkhub.hadoop.flowsum;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

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
 * FlowCountMapper 序列化
 * <p>
 */

public class FlowCountMapper extends Mapper<LongWritable, Text, Text, FlowBean> {

    /**
     * Extract k, v
     * 提取k,v
     */
    Text k = new Text();
    FlowBean v = new FlowBean();

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * Get the first row of data
         * 获取第一行数据
         */
        String line = value.toString();

        /**
         * Cutting data
         * 切割数据
         */
        String[] fields = line.split(" ");

        /**
         * Package object
         * 封装对象
         */

        // 封装手机号 | Package phone number
        k.set(fields[1]);

        long upFlow = Long.parseLong(fields[fields.length - 3]);
        long downFlow = Long.parseLong(fields[fields.length - 2]);

        v.setUpFlow(upFlow);
        v.setDownFlow(downFlow);

        /**
         * data input
         * 写入数据
         */
        context.write(k, v);
    }
}
