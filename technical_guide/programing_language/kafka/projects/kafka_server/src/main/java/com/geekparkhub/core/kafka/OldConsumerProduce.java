package com.geekparkhub.core.kafka;

import kafka.javaapi.producer.Producer;
import kafka.producer.KeyedMessage;
import kafka.producer.ProducerConfig;

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
 * OldConsumerProduce
 * <p>
 */

public class OldConsumerProduce {
    @SuppressWarnings("deprecation")
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
        props.put("metadata.broker.list", "systemhub511:9092");

        /**
         * Response level
         * 应答级别
         */
        props.put("request.required.acks", "1");

        /**
         * K value serialization
         * K值 序列化
         */
        props.put("serializer.class", "kafka.serializer.StringEncoder");

        /**
         * Instantiate producer object
         * 实例化 生产者对象
         */
        Producer<Integer, String> producer = new Producer<Integer, String>(new ProducerConfig(props));

        /**
         * Send data
         * 发送数据
         */
        KeyedMessage<Integer, String> message = new KeyedMessage<Integer, String>("topic001", "Hello,World");
        producer.send(message);

    }
}
