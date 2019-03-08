package com.geekparkhub.hadoop.mapreduce;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * GeekDeveloper : JEEP-711
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * <p>
 * Reducer 阶段
 * <p>
 * KEYIN 既是map阶段输出的key
 * VALUEIN 既是map阶段输出的value
 * @author system
 */

public class WordcountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

    /**
     * Rewrite the reduce() method
     * 重写reduce()方法
     *
     * @param key
     * @param values
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        IntWritable v = new IntWritable();
        /**
         * 1. Accumulate summation
         * 1. 累加求和
         */
        int sum = 0;
        for (IntWritable value : values) {
            sum += value.get();
        }
        v.set(sum);

        /**
         * 2. Output data
         * 2. 输出数据
         */
        context.write(key, v);
    }
}
