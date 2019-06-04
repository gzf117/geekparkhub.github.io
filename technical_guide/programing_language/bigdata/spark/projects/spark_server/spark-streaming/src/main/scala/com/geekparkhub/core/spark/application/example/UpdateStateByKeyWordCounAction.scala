package com.geekparkhub.core.spark.application.example

import org.apache.spark.SparkConf
import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.streaming.dstream.{DStream, ReceiverInputDStream}

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
  * UpdateStateByKeyWordCounAction
  * <p>
  */

object UpdateStateByKeyWordCounAction {
  def main(args: Array[String]): Unit = {

    // 创建 SparkConf
    val sc: SparkConf = new SparkConf().setMaster("local[*]").setAppName("UpdateStateByKeyWordCounAction")

    //创建 StreamingContext
    val ssc = new StreamingContext(sc, Seconds(3))

    // 创建缓存目录检查站
    ssc.checkpoint("./ck")

    // 创建 DStream
    val lineDStream: ReceiverInputDStream[String] = ssc.socketTextStream("systemhub511", 9999)

    // 将行数据转换为单词
    val wordDStream: DStream[String] = lineDStream.flatMap(_.split(" "))

    // 将单词住转换为元祖
    val wordAndOneDStream: DStream[(String, Int)] = wordDStream.map((_, 1))

    /**
      * 定义更新状态方法
      * 参数 values为当前批次单词频度
      * 参数 state为以往批次单词频度
      */
    val updateFunc = (values: Seq[Int], state: Option[Int]) => {
      val count: Int = values.sum
      val perCount: Int = state.getOrElse(0)
      Some(count + perCount)
    }

    // 统计单词出现个数
    val DStreamResult: DStream[(String, Int)] = wordAndOneDStream.updateStateByKey(updateFunc)

    // 输出日志信息
    DStreamResult.print()

    // 启动流式任务
    ssc.start()
    ssc.awaitTermination()
  }
}
