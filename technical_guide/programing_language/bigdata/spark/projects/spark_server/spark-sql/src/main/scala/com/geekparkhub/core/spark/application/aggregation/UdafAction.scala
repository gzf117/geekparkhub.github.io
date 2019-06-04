package com.geekparkhub.core.spark.application.aggregation

import org.apache.spark.sql.{DataFrame, SparkSession}

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
  * UdafAction
  * <p>
  */

object UdafAction {
  def main(args: Array[String]): Unit = {

    // 创建SparkSession
    val sparkSession: SparkSession = SparkSession
      .builder().master("local[*]").appName("UdafAction").getOrCreate()

    // 创建DF
    val df: DataFrame = sparkSession.read.json("/Volumes/GEEK-SYSTEM/Technical_Framework/spark/projects/spark_server/spark-sql/data/people.json")

    // SQL风格 数据查询 | 创建临时表
    df.createTempView("PEOPLE")

    // 注册自定义函数
    sparkSession.udf.register("AvgAction", AvgAction)

    // 使用自定义函数
    sparkSession.sql("SELECT AvgAction(age) FROM PEOPLE").show()

    // 关闭资源
    sparkSession.stop()
  }
}
