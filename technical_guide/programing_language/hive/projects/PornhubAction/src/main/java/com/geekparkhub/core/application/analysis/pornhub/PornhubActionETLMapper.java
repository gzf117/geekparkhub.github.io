package com.geekparkhub.core.application.analysis.pornhub;

import org.apache.commons.lang.StringUtils;
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
 * PornhubActionETLMapper
 * <p>
 */

public class PornhubActionETLMapper extends Mapper<LongWritable, Text, Text, NullWritable> {

    /**
     * Extract k
     * 提取k
     */
    Text k = new Text();

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
         * 1. Get the first row of data
         * 1. 获取第一行数据
         */
        String line = value.toString();

        /**
         * 2. Cleaning data
         * 2. 清洗数据
         */
        String etlString = PornhubActionETLUtil.getETLString(line);
        // 如果数据为空,则直接返回.
        if (StringUtils.isBlank(etlString)){
            return;
        }

        /**
         * 3.Package object
         * 3.封装对象
         */
        k.set(etlString);

        /**
         * 4.data input
         * 4.写入数据
         */
        context.write(k, NullWritable.get());

    }
}
