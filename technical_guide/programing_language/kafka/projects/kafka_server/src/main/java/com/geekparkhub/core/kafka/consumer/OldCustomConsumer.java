package com.geekparkhub.core.kafka.consumer;

import kafka.consumer.Consumer;
import kafka.consumer.ConsumerConfig;
import kafka.consumer.ConsumerIterator;
import kafka.consumer.KafkaStream;
import kafka.javaapi.consumer.ConsumerConnector;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
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
 * OldCustomConsumer
 * <p>
 */

public class OldCustomConsumer {

    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.put("zookeeper.connect", "systemhub511:2181");
        properties.put("group.id", "test");
        properties.put("zookeeper.session.timeout.ms", "500");
        properties.put("zookeeper.sync.time.ms", "250");
        properties.put("auto.commit.interval.ms", "1000");

        ConsumerConnector consumer = Consumer.createJavaConsumerConnector(new ConsumerConfig(properties));
        HashMap<String, Integer> topicCount = new HashMap<>();
        topicCount.put("topic001", 1);
        Map<String, List<KafkaStream<byte[], byte[]>>> consumerMap = consumer.createMessageStreams(topicCount);
        KafkaStream<byte[], byte[]> stream = consumerMap.get("topic001").get(0);
        ConsumerIterator<byte[], byte[]> it = stream.iterator();
        while (it.hasNext()) {
            System.out.println(new String(it.next().message()));
        }
    }
}
