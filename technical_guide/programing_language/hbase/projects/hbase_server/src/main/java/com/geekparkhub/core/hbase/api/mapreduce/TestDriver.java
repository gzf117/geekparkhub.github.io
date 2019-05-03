package com.geekparkhub.core.hbase.api.mapreduce;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableMapReduceUtil;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

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
 * TestDriver
 * <p>
 */

public class TestDriver extends Configuration implements Tool {

    Configuration configuration = null;

    public int run(String[] args) throws Exception {

        /**
         * 实例化 Job对象
         */
        Job job = Job.getInstance(configuration);
        job.setJarByClass(TestDriver.class);

        TableMapReduceUtil.initTableMapperJob("test002", new Scan(), TestMapper.class, ImmutableBytesWritable.class, Put.class, job);

        TableMapReduceUtil.initTableReducerJob("test002_mr", TestReducer.class, job);

        boolean completion = job.waitForCompletion(true);

        return completion ? 0 : 1;
    }

    public void setConf(Configuration conf) {
        this.configuration = conf;
    }

    public Configuration getConf() {
        return configuration;
    }

    public static void main(String[] args) throws Exception {
        Configuration configuration = HBaseConfiguration.create();
        int run = ToolRunner.run(configuration, new TestDriver(), args);
    }
}
