package com.geekparkhub.core.kafka.consumer;

import kafka.api.FetchRequestBuilder;
import kafka.cluster.BrokerEndPoint;
import kafka.javaapi.*;
import kafka.javaapi.consumer.SimpleConsumer;
import kafka.javaapi.message.ByteBufferMessageSet;
import kafka.message.MessageAndOffset;

import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

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
 * LowerConsumer
 * <p>
 */

public class LowerConsumer {
    public static void main(String[] args) {

        /**
         * Define related parameters
         * 定义相关参数
         */

        /**
         * Kafka cluster
         * Kafka 集群
         */
        ArrayList<String> brokers = new ArrayList<>();
        brokers.add("systemhub511");
        brokers.add("systemhub611");
        brokers.add("systemhub711");

        /**
         * port number
         * 端口号
         */
        int port = 9092;

        /**
         * Theme Topic
         * 主题 Topic
         */
        String topic = "topic002";

        /**
         * Partition
         * 分区 Partition
         */
        int partition = 0;

        /**
         * Offset
         */
        long offset = 2;

        /**
         * Instantiate the LowerConsumer object
         * 实例化 LowerConsumer对象
         */
        LowerConsumer lowerConsumer = new LowerConsumer();
        lowerConsumer.getData(brokers,port,topic,partition,offset);
    }

    /**
     * Discover partition leader
     * 发现分区Leader
     *
     * @return
     */
    private BrokerEndPoint findLeader(List<String> brokers, int port, String topic, int partition) {

        /**
         * Instantiation Partition Leader Consumer Object
         * 实例化 分区Leader消费者对象
         */
        for (String broker : brokers) {
            SimpleConsumer getLeader = new SimpleConsumer(broker, port, 1000, 1024 * 4, "getLeader");

            /**
             * Create topic metadata information request
             * 创建主题元数据信息请求
             */
            TopicMetadataRequest topicMetadataRequest = new TopicMetadataRequest(Collections.singletonList(topic));

            /**
             * Get theme metadata return value
             * 获取主题元数据返回值
             */
            TopicMetadataResponse metadataResponse = getLeader.send(topicMetadataRequest);

            /**
             * Parse the metadata return value
             * 解析元元数据返回值
             */
            List<TopicMetadata> topicsMetadata = metadataResponse.topicsMetadata();

            /**
             * Loop theme metadata
             * 循环 主题元数据
             */
            for (TopicMetadata topicMetadatum : topicsMetadata) {

                /**
                 * Get multiple partition metadata information
                 * 获取多个分区元数据信息
                 */
                List<PartitionMetadata> partitionsMetadata = topicMetadatum.partitionsMetadata();

                /**
                 * Loop multi-partition metadata
                 * 循环 多分区元数据
                 */
                for (PartitionMetadata partitionMetadata : partitionsMetadata) {
                    /**
                     * Returns the leader metadata information if the partition number is equal to 0
                     * 如果分区号等于0,则返回leader元数据信息
                     */
                    if (partition == partitionMetadata.partitionId()) {
                        return partitionMetadata.leader();
                    }
                }
            }
        }
        return null;
    }

    /**
     * retrieve data
     * 获取数据
     */
    private void getData(List<String> brokers, int port, String topic, int partition, long offset) {

        /**
         * Get Partition leader
         * 获取分区leader
         */
        BrokerEndPoint leader = findLeader(brokers, port, topic, partition);
        if (leader == null) {
            return;
        }

        String leaderHost = leader.host();

        /**
         * Get data consumer object
         * 获取数据消费者对象
         */
        SimpleConsumer getData = new SimpleConsumer(leaderHost, port, 1000, 1024 * 4, "getData");

        /**
         * Instantiation get data object
         * 实例化 获取数据对象
         */
        kafka.api.FetchRequest fetchRequest = new FetchRequestBuilder().addFetch(topic, partition, offset, 50000).build();

        /**
         * Get data return value
         * 获取数据返回值
         */
        FetchResponse fetchResponse = getData.fetch(fetchRequest);

        /**
         * Parse the return value
         * 解析返回值
         */
        ByteBufferMessageSet messageAndOffsets = fetchResponse.messageSet(topic, partition);
        for (MessageAndOffset messageAndOffset : messageAndOffsets) {
            long offset1 = messageAndOffset.offset();
            ByteBuffer payload = messageAndOffset.message().payload();
            byte[] bytes = new byte[payload.limit()];
            payload.get(bytes);
            System.out.println("Offset is = " + offset1 + " -- & -- Message is = " + new String(bytes));
        }
    }
}