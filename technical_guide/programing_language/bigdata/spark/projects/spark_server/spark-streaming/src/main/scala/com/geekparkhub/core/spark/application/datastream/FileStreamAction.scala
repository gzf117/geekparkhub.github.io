package com.geekparkhub.core.spark.application.datastream

import org.apache.spark.SparkConf
import org.apache.spark.streaming.dstream.DStream
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
  * FileStreamAction
  * <p>
  */

object FileStreamAction {
  def main(args: Array[String]): Unit = {

    // 创建 SparkConf
    val sc: SparkConf = new SparkConf().setMaster("local[*]").setAppName("FileStreamAction")

    //创建 StreamingContext
    val ssc = new StreamingContext(sc, Seconds(3))

    // 监控文件夹 DStream
    val fileDStream: DStream[String] = ssc.textFileStream("hdfs://systemhub511:9000/core_flow/spark/filestream/")

    // 输出日志信息
    fileDStream.print()

    // 启动流式任务
    ssc.start()
    ssc.awaitTermination()
  }
}
