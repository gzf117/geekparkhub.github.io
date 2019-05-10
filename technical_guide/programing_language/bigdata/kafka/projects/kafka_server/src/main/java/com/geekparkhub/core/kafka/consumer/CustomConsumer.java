package com.geekparkhub.core.kafka.consumer;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;

import java.util.Arrays;
import java.util.Properties;

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
 * CustomConsumer
 * <p>
 */

public class CustomConsumer {

    public static void main(String[] args) {

        /**
         * Configuration information
         * 配置信息
         */
        Properties props = new Properties();

        /**
         * Kafka configuration information
         * Kafka配置信息
         */
        props.put("bootstrap.servers", "systemhub511:9092");

        /**
         * Consumer group ID
         * 消费者组ID
         */
        props.put("group.id", "test");

        /**
         * Set auto-submit offset
         * 设置自动提交offset
         */
        props.put("enable.auto.commit", "true");

        /**
         * Submission delay
         * 提交延时
         */
        props.put("auto.commit.interval.ms", "1000");

        /**
         * K value Deserialization
         * K值 反序列化
         */
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

        /**
         * V value Deserialization
         * V值 反序列化
         */
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

        /**
         * Instantiation Consumer Object
         * 实例化 消费者对象
         */
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);

        /**
         * Specify Topic
         * 指定Topic
         */
        consumer.subscribe(Arrays.asList("topic001", "topic002", "topic003"));

        while (true) {

            /**
             * retrieve data
             * 获取数据
             */
            ConsumerRecords<String, String> consumerRecords = consumer.poll(100);

            /**
             * Loop output
             * 循环输出
             */
            for (ConsumerRecord<String, String> records : consumerRecords) {
                String topic = records.topic();
                int partition = records.partition();
                String value = records.value();
                System.out.println("Topic is = " + topic + " -- & -- Partition is = " + partition + " -- & -- Value is = " + value);
            }
        }


    }
}
