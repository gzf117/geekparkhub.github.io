package com.geekparkhub.core.spark.application.dataconnections

import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.hbase.HBaseConfiguration
import org.apache.hadoop.hbase.client.Result
import org.apache.hadoop.hbase.io.ImmutableBytesWritable
import org.apache.hadoop.hbase.mapreduce.TableInputFormat
import org.apache.hadoop.hbase.util.Bytes
import org.apache.spark.rdd.{NewHadoopRDD, RDD}
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
  * HbaseConnection
  * <p>
  */

object HbaseConnection {
  def main(args: Array[String]): Unit = {

    // 创建SpakConf
    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("HbaseConnection")

    // 创建SC
    val sc = new SparkContext(sparkConf)

    //构建HBase配置信息
    val conf: Configuration = HBaseConfiguration.create()
    conf.set("hbase.zookeeper.quorum", "systemhub511,systemhub611,systemhub711")
    conf.set(TableInputFormat.INPUT_TABLE, "test")

    // 读取HBASE数据
    val hbaseRDD = new NewHadoopRDD(sc, classOf[TableInputFormat], classOf[ImmutableBytesWritable], classOf[Result], conf)

    // 获取RowKey
    val value: RDD[String] = hbaseRDD.map(x => Bytes.toString(x._2.getRow))

    // 输出数据
    value.collect().foreach(println)

    // 关闭资源
    sc.stop()
  }
}