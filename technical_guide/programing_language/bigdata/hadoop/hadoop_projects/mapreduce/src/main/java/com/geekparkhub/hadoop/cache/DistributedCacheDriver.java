package com.geekparkhub.hadoop.cache;

import com.geekparkhub.hadoop.table.TableBean;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

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
 * DistributedCacheDriver
 * <p>
 */

public class DistributedCacheDriver {
    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException, URISyntaxException {
        /**
         * Preset data input and output path
         * 预设数据输入输出路径
         */
        args = new String[]{"/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_table",
                "/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/output_table_001"};

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
        job.setJarByClass(DistributedCacheDriver.class);

        /**
         * 3. Associate Map classes
         * 3. 关联Map类
         */
        job.setMapperClass(DistributedCacheMapper.class);

        /**
         * 4. Set the key and value types for the final data output
         * 4. 设置最终数据输出的key与value类型
         */
        job.setOutputKeyClass(TableBean.class);
        job.setOutputValueClass(NullWritable.class);

        /**
         * 5. Set the input path and output path
         * 5. 设置输入路径和输出路径
         */
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         * 6.Loading cached data
         * 6.加载缓存数据
         */
        job.addCacheFile(new URI("/Volumes/GEEK-SYSTEM/Technical_Framework/Hadoop/projects/mapreduce/src/main/resources/input_table/pd.txt"));

        /**
         * 7.The logic of the Join on the Map does not require the Reduce phase. Set the number of Reduce Tasks to 0.
         * 7.Map端Join的逻辑不需要Reduce阶段,设置ReduceTask数量为0
         */
        job.setNumReduceTasks(0);

        /**
         * 8. Submit the Job
         * 8. 提交Job
         */
        boolean result = job.waitForCompletion(true);

        /**
         * 9. Log printing
         * 9. 日志打印
         */
        System.exit(result ? 0 : 1);
    }
}
