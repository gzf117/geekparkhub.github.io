package com.geekparkhub.core.kafka.streams;

import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.processor.Processor;
import org.apache.kafka.streams.processor.ProcessorSupplier;
import org.apache.kafka.streams.processor.TopologyBuilder;

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
 * KafkaStream
 * <p>
 */

public class KafkaStream {
    public static void main(String[] args) {

        /**
         * Instantiate topology objects
         * 实例化 拓扑对象
         */
        TopologyBuilder builder = new TopologyBuilder();

        /**
         * Instantiation configuration file
         * 实例化 配置文件
         */
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "systemhub511:9092");
        properties.put("application.id", "KafkaStream");

        /**
         * Build topology
         * 构建拓扑结构
         */
        builder.addSource("SOURCE", "topic001")
                .addProcessor("PROCESSOR", new ProcessorSupplier() {
                    @Override
                    public Processor get() {
                        return new LogProcessor() {
                        };
                    }
                }, "SOURCE")
                .addSink("SINK", "topic002", "PROCESSOR");

        /**
         * Instantiate KafkaStreams objects
         * 实例化 KafkaStreams对象
         */
        KafkaStreams kafkaStreams = new KafkaStreams(builder, properties);
        kafkaStreams.start();
    }
}


