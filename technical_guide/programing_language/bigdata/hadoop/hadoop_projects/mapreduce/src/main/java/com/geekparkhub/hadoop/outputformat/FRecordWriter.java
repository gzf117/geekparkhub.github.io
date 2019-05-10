package com.geekparkhub.hadoop.outputformat;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.RecordWriter;
import org.apache.hadoop.mapreduce.TaskAttemptContext;

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
 * FRecordWriter
 * <p>
 */

public class FRecordWriter extends RecordWriter<Text, NullWritable> {

    /**
     * Extract FS Data Output Stream
     * 提取FSDataOutputStream
     */
    FSDataOutputStream geekparkhubOut;
    FSDataOutputStream otherOut;

    /**
     * FRecordWriter 写数据核心构造器
     *
     * @param job
     */

    public FRecordWriter(TaskAttemptContext job) {

        try {

            /**
             * Get the file system and pass the current job object to the file system
             *获取文件系统,将当前job对象传递给文件系统
             */
            FileSystem fs = FileSystem.get(job.getConfiguration());

            /**
             * Create an output stream geekparkhub.log
             * 创建输出流 geekparkhub.log
             */
            geekparkhubOut = fs.create(new Path("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_format_001/geekparkhub.log"));

            /**
             * Create an output stream other.log
             * 创建输出流 other.log
             */
            otherOut = fs.create(new Path("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_format_001/other.log"));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Override write() method
     * 复写 write()方法
     *
     * @param key
     * @param value
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    public void write(Text key, NullWritable value) throws IOException, InterruptedException {

        /**
         * Determine if the key contains geekparkhub
         * If yes, write to geekparkhub.log
         * If not, write to other.log
         *
         * 判断key中是否含有geekparkhub
         * 如果有则写入到geekparkhub.log
         * 如法没有则写入到other.log
         */

        if (key.toString().contains("geekparkhub")) {
            geekparkhubOut.write(key.toString().getBytes());
        } else {
            otherOut.write(key.toString().getBytes());
        }

    }

    /**
     * Override the close() method
     * 复写 close()方法
     *
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    public void close(TaskAttemptContext context) throws IOException, InterruptedException {
        if (geekparkhubOut != null) {
            geekparkhubOut.close();
        }
        if (otherOut != null) {
            otherOut.close();
        }
    }
}
