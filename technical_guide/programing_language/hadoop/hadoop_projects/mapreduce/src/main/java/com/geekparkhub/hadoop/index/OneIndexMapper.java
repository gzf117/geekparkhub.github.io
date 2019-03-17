package com.geekparkhub.hadoop.index;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
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
 * OneIndexMapper
 * <p>
 */

public class OneIndexMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

    String name;

    @Override
    protected void setup(Mapper<LongWritable, Text, Text, IntWritable>.Context context) throws IOException, InterruptedException {

        /**
         * Get the file name
         * 获取文件名称
         */
        FileSplit inputSplit = (FileSplit) context.getInputSplit();
        name = inputSplit.getPath().getName();
    }

    Text k = new Text();
    IntWritable v = new IntWritable(1);

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

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
         * Loop traversal
         * 循环遍历
         */
        for (String word : split) {
            k.set(word + " - - " + name);
            context.write(k, v);
        }
    }
}
