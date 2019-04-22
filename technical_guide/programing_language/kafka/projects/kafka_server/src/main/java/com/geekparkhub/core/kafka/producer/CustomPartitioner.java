package com.geekparkhub.core.kafka.producer;

import org.apache.kafka.clients.producer.Partitioner;
import org.apache.kafka.common.Cluster;

import java.util.Map;

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
 * CustomPartitioner
 * <p>
 */

public class CustomPartitioner implements Partitioner {

    /**
     * Empty reference constructor
     * 空参构造器
     */
    public CustomPartitioner() {
        super();
    }

    /**
     * 复写分区方法
     *
     * @param topic
     * @param key
     * @param keyBytes
     * @param value
     * @param valueBytes
     * @param cluster
     * @return
     */
    @Override
    public int partition(String topic, Object key, byte[] keyBytes, Object value, byte[] valueBytes, Cluster cluster) {
        return 0;
    }

    /**
     * Close resource
     * 关闭资源
     */
    @Override
    public void close() {
    }

    /**
     * Configuration information
     * 配置信息
     *
     * @param configs
     */
    @Override
    public void configure(Map<String, ?> configs) {
    }
}
