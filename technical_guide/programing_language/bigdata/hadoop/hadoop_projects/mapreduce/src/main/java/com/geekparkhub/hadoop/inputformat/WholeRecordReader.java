package com.geekparkhub.hadoop.inputformat;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.InputSplit;
import org.apache.hadoop.mapreduce.RecordReader;
import org.apache.hadoop.mapreduce.TaskAttemptContext;
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
 * WholeRecordReader
 * <p>
 */

public class WholeRecordReader extends RecordReader<Text, BytesWritable> {

    /**
     * Declaration file slice
     * 声明文件切片
     */
    FileSplit split;
    Configuration conf;
    Text k = new Text();
    BytesWritable v = new BytesWritable();

    /**
     * Marker bit
     * 标记位
     */
    boolean isProgress = true;

    @Override
    public void initialize(InputSplit split, TaskAttemptContext context) throws IOException, InterruptedException {
        /**
         * Initialization operation
         * 初始化操作
         */
        this.split = (FileSplit) split;

        /**
         * Get configuration information
         * 获取配置信息
         */
        conf = context.getConfiguration();
    }

    @Override
    public boolean nextKeyValue() throws IOException, InterruptedException {

        if (isProgress) {

            /**
             * Handling core business logic
             * 处理核心业务逻辑
             */
            byte[] buf = new byte[(int) split.getLength()];

            /**
             * Get fs object
             * 1.获取fs对象
             */
            Path path = split.getPath();
            FileSystem fs = path.getFileSystem(conf);

            /**
             * Get the input stream
             * 2.获取输入流
             */
            FSDataInputStream fis = fs.open(path);

            /**
             * File copy buffer
             * 3.将文件拷贝缓冲区
             */
            IOUtils.readFully(fis, buf, 0, buf.length);

            /**
             * Package V
             * 4.封装 V
             */
            v.set(buf, 0, buf.length);

            /**
             * Package K
             * 5.封装 K
             */
            k.set(path.toString());

            /**
             * Close resource
             * 6.关闭资源
             */
            IOUtils.closeStream(fis);

            /**
             * Clear flag
             * 清空标记位
             */
            isProgress = false;
            return true;
        }
        return false;
    }

    @Override
    public Text getCurrentKey() throws IOException, InterruptedException {

        return k;
    }

    @Override
    public BytesWritable getCurrentValue() throws IOException, InterruptedException {

        return v;
    }

    @Override
    public float getProgress() throws IOException, InterruptedException {
        return 0;
    }

    @Override
    public void close() throws IOException {

    }
}
