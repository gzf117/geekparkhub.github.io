package com.geekparkhub.hadoop.cache;


import org.apache.commons.lang.StringUtils;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.util.HashMap;

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
 * DistributedCacheMapper
 * <p>
 */

public class DistributedCacheMapper extends Mapper<LongWritable, Text,Text, NullWritable> {

    HashMap<String, String> pdMap = new HashMap<>();
    Text k = new Text();

    /**
     * Override initialization method
     * 复写 初始化方法
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void setup(Mapper<LongWritable,Text,Text,NullWritable>.Context context) throws IOException, InterruptedException {

        /**
         * Get the cache path of the file
         * 获取文件缓存路径
         */
        URI[] cacheFiles = context.getCacheFiles();
        String path = cacheFiles[0].getPath().toString();

        /**
         * Cache smaller data tables
         * 缓存较小的数据表
         */
        BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(path), "UTF-8"));

        /**
         * Loop traversal
         * 循环遍历
         */
        String line;
        while (StringUtils.isNotEmpty(line = reader.readLine())){
            /**
             * Cutting data
             * 切割数据
             */
            String[] fileds = line.split(" ");
            pdMap.put(fileds[0],fileds[1]);
        }
        /**
         * Close resource
         * 关闭资源
         */
        IOUtils.closeStream(reader);
    }

    /**
     * Override map method
     * 复写 map方法
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
         * Cutting data
         * 切割数据
         */
        String[] fileds = line.split(" ");

        /**
         * Get pid field attribute
         * 获取pid字段属性
         */
        String pid = fileds[1];

        /**
         * Get pname field attribute
         * 获取pname字段属性
         */
        String pname = pdMap.get(pid);

        /**
         * Data stitching
         * 数据拼接
         */
        line = line +"\t"+ pname;
        k.set(line);

        /**
         * Write data
         * 写出数据
         */
        context.write(k,NullWritable.get());
    }
}
