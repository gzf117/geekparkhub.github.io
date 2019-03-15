package com.geekparkhub.hadoop.weblog;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
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
 * LogMappers
 * <p>
 */

public class LogMapper extends Mapper<LongWritable, Text, Text, NullWritable> {

    /**
     * Rewrite the map() method
     * 复写 map()方法
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
         * Get a row of data
         * 获取一行数据
         */
        String line = value.toString();

        /**
         * Analytical data
         * 解析数据
         */
        boolean result = parseLog(line, context);

        /**
         * If the parsing fails, skip the return directly.
         * 如果解析失败,则直接跳过返回
         */
        if (!result) {
            return;
        }
        /**
         * If the parsing is successful, write out the data.
         * 如果解析成功,写出数据
         */
        context.write(value, NullWritable.get());
    }

    /**
     * Parsing log method
     * 解析日志方法
     *
     * @param line
     * @param context
     * @return
     */
    private boolean parseLog(String line, Context context) {

        /**
         * Cutting data
         * 切割数据
         */
        String[] flelds = line.split(" ");

        /**
         * Return true if the log length is greater than 11.
         * 如果日志长度大于11,则返回true
         */
        if (flelds.length > 11) {
            /**
             * Introduce a counter, in the Map phase, the number that is judged to be true.
             * 引入计数器,在Map阶段,判断为true的个数
             */
            context.getCounter("map", "true").increment(1);
            return true;
        } else {
            /**
             * Introduce a counter, in the Map phase, the number that is judged to be false.
             * 引入计数器,在Map阶段,判断为false的个数
             */
            context.getCounter("map", "false").increment(1);
            return false;
        }
    }
}
