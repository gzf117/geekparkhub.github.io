package com.geekparkhub.core.spark.application.datastream

import org.apache.spark.SparkConf
import org.apache.spark.rdd.RDD
import org.apache.spark.streaming.dstream.{DStream, InputDStream}
import org.apache.spark.streaming.{Seconds, StreamingContext}

import scala.collection.mutable

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
  * QueuStreamAction
  * <p>
  */

object QueuStreamAction {
  def main(args: Array[String]): Unit = {
    // 创建 SparkConf
    val sc: SparkConf = new SparkConf().setMaster("local[*]").setAppName("QueuStreamAction")

    //创建 StreamingContext
    val ssc = new StreamingContext(sc, Seconds(3))

    // 创建RDD队列
    val rddQueue = new mutable.Queue[RDD[Int]]()

    // 创建 rddDStream
    val rddDStream: InputDStream[Int] = ssc.queueStream(rddQueue,false)

    // 统计计算
    val result: DStream[Int] = rddDStream.reduce(_ + _)

    // 输出日志信息
    result.print()

    // 启动流式任务
    ssc.start()

    // 循环创建RDD
    for (i <- 1 to 5) {
      rddQueue += ssc.sparkContext.makeRDD(1 to 100, 10)
      Thread.sleep(2000)
    }
    ssc.awaitTermination()
  }
}
