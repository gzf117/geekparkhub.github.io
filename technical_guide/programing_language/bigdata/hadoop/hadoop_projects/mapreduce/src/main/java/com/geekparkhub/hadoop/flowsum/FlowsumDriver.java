package com.geekparkhub.hadoop.flowsum;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.fs.Path;
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
 * FlowsumDriver 序列化
 * <p>
 */

public class FlowsumDriver {

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

        /**
         * Preset data input and output path
         * 预设数据输入输出路径
         */
        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_flow",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_flow_002"};

        /**
         * Get configuration information, or job object instance
         * 获取配置信息,或者job对象实例
         */
        Configuration configuration = new Configuration();
        Job job = Job.getInstance(configuration);

        /**
         * Specify the local path where the jar package of the program is located.
         * 指定本程序的jar包所在的本地路径
         */
        job.setJarByClass(FlowsumDriver.class);

        /**
         * Set up a custom Partitioner
         * 设置自定义Partitioner
         */
        job.setPartitionerClass(ProvincePartitioner.class);

        /**
         * Set up Num Reduce Tasks
         * 设置NumReduceTasks
         */
        job.setNumReduceTasks(1);

        /**
         * Specify the mapper/Reducer business class to be used by this business job
         * 指定本业务job要使用的mapper/Reducer业务类
         */
        job.setMapperClass(FlowCountMapper.class);
        job.setReducerClass(FlowCountReducer.class);

        /**
         * Specify the kv type of the mapper output data
         * 指定mapper输出数据的kv类型
         */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(FlowBean.class);

        /**
         * Specify the kv type of the final output data
         * 指定最终输出的数据的kv类型
         */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FlowBean.class);

        /**
         * Specify the directory where the input input file of the job is located.
         * 指定job的输入原始文件所在目录
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * Submit the relevant parameters configured in the job, and the jar package where the java class used by the job is located, and submit it to the yarn to run.
         * 将job中配置的相关参数,以及job所用的java类所在的jar包,提交给yarn去运行
         */
        boolean results = job.waitForCompletion(true);
        System.exit(results ? 0 : 1);
    }
}
