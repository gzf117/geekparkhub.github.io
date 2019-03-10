package com.geekparkhub.hadoop.flowsum;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;

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
 * ProvincePartitioner
 * <p>
 */

public class ProvincePartitioner extends Partitioner<Text, FlowBean> {

    /**
     * Override the getPartition() method
     * 重写getPartition()方法
     * <p>
     * Key is the phone number, value is the traffic information
     * key是手机号,value是流量信息
     */

    @Override
    public int getPartition(Text key, FlowBean value, int numPartitions) {

        /**
         * Get the top three mobile phone numbers
         * 获取手机号前三位
         */
        String prePhoneNum = key.toString().substring(0, 3);

        /**
         * Partition status
         * 分区状态
         */
        int partition = 4;

        if ("136".equals(prePhoneNum)) {
            /**
             * If the first number is 136, the first data of 136 is written to the 0th partition.
             * 如果获得到首号为136,将136首号数据写入到第0分区.
             */
            partition = 0;
        } else if ("137".equals(prePhoneNum)) {
            /**
             * If the first number is 137, the first data of 137 is written to the first partition.
             * 如果获得到首号为137,将137首号数据写入到第1分区.
             */
            partition = 1;
        } else if ("138".equals(prePhoneNum)) {
            /**
             * If the first number is 138, the first data of 138 is written to the second partition.
             * 如果获得到首号为138,将138首号数据写入到第2分区.
             */
            partition = 2;
        } else if ("139".equals(prePhoneNum)) {
            /**
             * If the first number is 138, the first data of 138 is written to the third partition.
             * 如果获得到首号为138,将138首号数据写入到第3分区.
             */
            partition = 3;
        }
        /**
         * If the first number is obtained, write the other first data to the default 4th partition.
         * 如果获得到首号为其他,将其他首号数据写入到默认第4分区.
         */
        return partition;
    }
}
