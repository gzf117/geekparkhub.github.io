package com.geekparkhub.hadoop.wordcount;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * Map 阶段
 * <p>
 * KEYIN 输入数据的key
 * VALUEIN 输入数据的value
 * KEYOUT 输出数据的key
 * VALUEOUT 输出数据的value
 * @author system
 */

public class WordcountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

    Text k = new Text();
    IntWritable v = new IntWritable(1);

    /**
     * Rewrite the map() method
     * 重写map()方法
     *
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        /**
         * 1. Get the first row of data, assuming the data is: geek geek
         * 1. 获取第一行数据,假设数据是:geek geek
         */
        String line = value.toString();

        /**
         * 2. Cutting data
         * 2. 切割空格数据
         */
        String[] words = line.split(" ");

        /**
         * 3. Loop through the data
         * 3. 循环遍历数据
         */
        for (String word : words) {
            k.set(word);
            context.write(k, v);
        }
    }
}
