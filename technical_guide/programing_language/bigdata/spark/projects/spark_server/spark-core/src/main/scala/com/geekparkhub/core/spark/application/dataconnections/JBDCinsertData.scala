package com.geekparkhub.core.spark.application.dataconnections

import org.apache.spark.{SparkConf, SparkContext}

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
  * JBDCinsertData
  * <p>
  */

object JBDCinsertData {
  def main(args: Array[String]): Unit = {

    // 创建SpakConf
    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("JBDCRead")

    // 创建SC
    val sc = new SparkContext(sparkConf)

    // 创建数据
    val data = sc.parallelize(List("Female", "Male", "Female"))

    // 调用添加数据方法
    data.foreachPartition(insertData)
  }

  // 添加数据方法
  def insertData(iterator: Iterator[String]): Unit = {
    Class.forName("com.mysql.jdbc.Driver").newInstance()
    val conn = java.sql.DriverManager.getConnection("jdbc:mysql://systemhub711:3306/company", "root", "000000")
    iterator.foreach(data => {
      val ps = conn.prepareStatement("insert into staff(name) values(?)")
      ps.setString(1, data)
      ps.executeUpdate()
    })
  }
}
