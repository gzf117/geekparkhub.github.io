package com.geekparkhub.core.spark.application.sparksql

import org.apache.spark.sql.SparkSession

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
  * SparkHiveAction
  * <p>
  */

object SparkHiveAction {
  def main(args: Array[String]): Unit = {
    // 创建SparkSession
    val sparkSession: SparkSession = SparkSession
      .builder()
      .enableHiveSupport()
      .master("local[*]")
      .appName("SparkHiveAction")
      .getOrCreate()

    // 展示数据表信息
    sparkSession.sql("show tables").show()

    // 关闭资源
    sparkSession.stop()
  }
}
