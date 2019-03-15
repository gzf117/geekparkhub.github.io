package com.geekparkhub.hadoop.compress;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.compress.CompressionCodec;
import org.apache.hadoop.io.compress.CompressionCodecFactory;
import org.apache.hadoop.io.compress.CompressionInputStream;

import java.io.*;

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
 * TestDecompression
 * <p>
 */

public class TestDecompression {

    public static void main(String[] args) throws IOException {

        /**
         * Get compressed file.
         * 获取压缩文件
         */
        decompress("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_combine_textInput_format/b.txt.bz2");
    }

    /**
     * Decompression method
     * 解压方法
     *
     * @param fileName
     */
    private static void decompress(String fileName) throws IOException {

        /**
         * Check compression method
         * 检查压缩方式
         */
        CompressionCodecFactory factory = new CompressionCodecFactory(new Configuration());
        CompressionCodec codec = factory.getCodec(new Path(fileName));

        /**
         * Determine if the compressed file is empty
         * 判断压缩文件是否为空
         */
        if (codec == null) {
            System.out.println("当前格式,不支持解压! & Current format, does not support decompression!");
            return;
        }

        /**
         * Get the input stream
         * 获取输入流
         */
        FileInputStream fis = new FileInputStream(new File(fileName));
        CompressionInputStream cis = codec.createInputStream(fis);


        /**
         * Get the output stream
         * 获取输出流
         */
        FileOutputStream fos = new FileOutputStream(new File(fileName + ".decode"));

        /**
         * Stream copy
         * 流对拷
         */
        IOUtils.copyBytes(cis, fos, 1024 * 1024, false);

        /**
         * Close resource
         * 关闭资源
         */
        IOUtils.closeStream(fos);
        IOUtils.closeStream(cis);
        IOUtils.closeStream(fis);
    }
}
