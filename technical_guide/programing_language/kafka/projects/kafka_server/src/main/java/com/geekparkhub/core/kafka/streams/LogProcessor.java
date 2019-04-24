package com.geekparkhub.core.kafka.streams;

import org.apache.kafka.streams.processor.Processor;
import org.apache.kafka.streams.processor.ProcessorContext;

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
 * LogProcessor
 * <p>
 */

public class LogProcessor implements Processor<byte[], byte[]> {
    private ProcessorContext context;

    @Override
    public void init(ProcessorContext processorContext) {
        context = processorContext;
    }

    @Override
    public void process(byte[] key, byte[] value) {

        /**
         * Get a row of data
         * 获取一行数据
         */
        String line = new String(value);

        /**
         * Remove dirty data
         * 去除脏数据
         */
        line = line.replaceAll(">>>", "_");

        value = line.getBytes();

        context.forward(key, value);
    }

    @Override
    public void punctuate(long l) {

    }

    @Override
    public void close() {

    }
}
