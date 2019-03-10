package com.geekparkhub.hadoop.wordcount;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.log4j.Logger;

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
 * WordcountDriver
 * <p>
 */

public class WordcountDriver {

    /**
     * Statement Logger
     */
    private static org.apache.log4j.Logger log = Logger.getLogger(WordcountDriver.class);

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_combine_textInput_format",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_combine_textInput_format_004"};

        /**
         * 1. Get the Job object
         * 1. 获取Job对象
         */
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);

        /**
         * 2. Set the jar storage location
         * 2. 设置jar存储位置
         */
        job.setJarByClass(WordcountDriver.class);

        /**
         * Set set Combiner Class
         *设置setCombinerClass
         */
        job.setCombinerClass(WordcountCombiner.class);

        /**
         * 3. Associate Map and Reduce classes
         * 3. 关联Map和Reduce类
         */
        job.setMapperClass(WordcountMapper.class);
        job.setReducerClass(WordcountReducer.class);

        /**
         * 4. Set the key and value types of the output data in the Mapper stage.
         * 4. 设置Mapper阶段输出数据的key与value类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);

        /**
         * 5. Set the key and value types for the final data output
         * 5. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

//        job.setNumReduceTasks(2);

        /**
         * Set the Format mode to Combine Text Input Format
         * 设置Format模式为Combine Text Input Format
         * If you do not set the Input Format, it defaults to Text Input Format.class
         * 如果不设置InputFormat，它默认用的是TextInputFormat.class
         */
//        job.setInputFormatClass(CombineTextInputFormat.class);

        /**
         * Set the virtual storage slice maximum to 20M
         * 设置虚拟存储切片最大值为 20M
         */
//        CombineTextInputFormat.setMaxInputSplitSize(job, 20971520);

        /**
         * Set the virtual storage slice maximum to 4M
         * 设置虚拟存储切片最大值为 4M
         */
//         CombineTextInputFormat.setMaxInputSplitSize(job, 4194304);

        /**
         * Set the virtual storage slice minimum to 2M
         * 设置虚拟存储切片最小值为 2M
         */
//         CombineTextInputFormat.setMinInputSplitSize(job, 2097152);



        /**
         * 6. Set the input path and output path
         * 6. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 7. Submit the Job
         * 7. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 8. Log printing
         * 8. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
