package com.geekparkhub.core.spark.application.dataconnections

import java.sql.DriverManager

import org.apache.spark.deploy.worker.DriverWrapper
import org.apache.spark.rdd.JdbcRDD
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
  * JDBCConnection
  * <p>
  */

object JDBCConnection {

  def main(args: Array[String]): Unit = {

    // 创建SpakConf
    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("JDBCConnection")

    // 创建SC
    val sc = new SparkContext(sparkConf)

    // 定义JDBC连接属性信息
    val driver = "com.mysql.jdbc.Driver"
    val url = "jdbc:mysql://systemhub711:3306/company"
    val userName = "root"
    val passWd = "000000"

    // 创建JDBC RDD
    val JdbcRDD = new JdbcRDD[(Int, String)](sc, () => {
      Class.forName(driver)
      DriverManager.getConnection(url, userName, passWd)
    }, "select id,name from staff where ? <= id and id <= ?",
      1,
      10,
      1,
      x => {
        (x.getInt(1), x.getString(2))
      }
    )

    // 打印JdbcRDD结果
    JdbcRDD.collect().foreach(println)

    // 关闭资源
    sc.stop()
  }
}