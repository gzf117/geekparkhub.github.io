package com.geekparkhub.hadoop.index;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

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
 * TwoIndexReducer
 * <p>
 */

public class TwoIndexReducer extends Reducer<Text, Text, Text, Text> {

    Text v = new Text();

    @Override
    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {

        /**
         * Splicing string
         * 拼接字符串
         */
        StringBuffer sb = new StringBuffer();
        for (Text value : values) {
            sb.append(value.toString().replaceAll("\t", " - -> ") + "\t");
        }
        v.set(sb.toString());

        /**
         * 写出数据
         */
        context.write(key, v);

    }
}
