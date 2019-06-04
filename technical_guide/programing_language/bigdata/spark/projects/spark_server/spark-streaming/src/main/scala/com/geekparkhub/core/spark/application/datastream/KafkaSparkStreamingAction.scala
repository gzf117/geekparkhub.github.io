package com.geekparkhub.core.spark.application.datastream

import kafka.serializer.StringDecoder
import org.apache.kafka.clients.consumer.ConsumerConfig
import org.apache.spark.SparkConf
import org.apache.spark.storage.StorageLevel
import org.apache.spark.streaming.dstream.ReceiverInputDStream
import org.apache.spark.streaming.kafka.KafkaUtils
import org.apache.spark.streaming.{Seconds, StreamingContext}

/**
  * Geek International Park | 极客国际公园
  * GeekParkHub | 极客实验室
  * Website | https://www.geekparkhub.com/
  * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
  * HackerParkHub | 黑客公园枢纽
  * Website | https://www.hackerparkhub.org/
  * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
  * GeekDeveloper : JEEP-711
  *
  * @author system
  * <p>
  * KafkaSparkStreamingAction
  * <p>
  */

object KafkaSparkStreamingAction {
  def main(args: Array[String]): Unit = {
    // 创建 SparkConf
    val sc: SparkConf = new SparkConf().setMaster("local[*]").setAppName("KafkaSparkStreamingAction")

    //创建 StreamingContext
    val ssc = new StreamingContext(sc, Seconds(3))

    // 声明 Kafka参数
    val zookeeper = "systemhub511:2181,systemhub611:2181,systemhub711:2181"
    val topic = "topic001"
    val consumerGroup = "spark"

    // 定义 Kafka参数
    val kafkaPara: Map[String, String] = Map[String, String](
      ConsumerConfig.GROUP_ID_CONFIG -> consumerGroup,
      "zookeeper.connect" -> zookeeper,
      ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> "org.apache.kafka.common.serialization.StringDeserializer",
      ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> "org.apache.kafka.common.serialization.StringDeserializer"
    )

    // 创建 KafkaDStream
    val KafkaDStream: ReceiverInputDStream[(String, String)] = KafkaUtils.createStream[String, String, StringDecoder, StringDecoder](ssc, kafkaPara, Map(topic -> 1), StorageLevel.MEMORY_ONLY)

    // 输出日志信息
    KafkaDStream.print()

    // 启动流式任务
    ssc.start()
    ssc.awaitTermination()
  }
}