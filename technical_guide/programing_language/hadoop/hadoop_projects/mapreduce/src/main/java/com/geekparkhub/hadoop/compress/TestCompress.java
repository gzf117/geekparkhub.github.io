package com.geekparkhub.hadoop.compress;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.compress.CompressionCodec;
import org.apache.hadoop.io.compress.CompressionOutputStream;
import org.apache.hadoop.util.ReflectionUtils;

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
 * TestCompress
 * <p>
 */

public class TestCompress {
    public static void main(String[] args) throws IOException, ClassNotFoundException {

        /**
         * Get the specified compressed file and set it to compress using B Zip 2 Codec format.
         * 获取指定压缩文件,并设置使用BZip2Codec格式进行压缩
         */
        compress("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_combine_textInput_format/b.txt"
                , "org.apache.hadoop.io.compress.BZip2Codec");
    }

    /**
     * Compression method
     * 压缩方法
     *
     * @param fileName
     * @param method
     */
    private static void compress(String fileName, String method) throws IOException, ClassNotFoundException {

        /**
         * 获取输入流
         */
        FileInputStream fis = new FileInputStream(new File(fileName));

        /**
         * Pass the method parameter to the compression mode tool class through the reflection mechanism,
         * and set the encoding mode to obtain the compression extension.
         * 通过反射机制,将method参数传递给压缩方式工具类,并设置编码方式,获取压缩扩展名
         */
        Class classCodec = Class.forName(method);
        CompressionCodec codec = (CompressionCodec) ReflectionUtils.newInstance(classCodec, new Configuration());

        /**
         * Get the output stream
         * 获取输出流
         */
        FileOutputStream fos = new FileOutputStream(fileName + codec.getDefaultExtension());

        /**
         * Set the obtained normal output stream to the compressed output stream
         * 将获取到的普通输出流,设置为压缩输出流
         */
        CompressionOutputStream cos = codec.createOutputStream(fos);

        /**
         * Copy between streams
         * 流之间对拷
         */
        IOUtils.copyBytes(fis, cos, 1024 * 1024, false);

        /**
         * Close resource
         * 关闭资源
         */
        IOUtils.closeStream(cos);
        IOUtils.closeStream(fos);
        IOUtils.closeStream(fis);
    }
}
