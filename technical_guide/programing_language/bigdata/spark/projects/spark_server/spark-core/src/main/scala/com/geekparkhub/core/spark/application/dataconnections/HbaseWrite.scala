package com.geekparkhub.core.spark.application.dataconnections

import org.apache.hadoop.hbase.client.Put
import org.apache.hadoop.hbase.io.ImmutableBytesWritable
import org.apache.hadoop.hbase.mapred.TableOutputFormat
import org.apache.hadoop.hbase.util.Bytes
import org.apache.hadoop.mapred.JobConf
import org.apache.spark.rdd.RDD
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
  * HbaseWrite
  * <p>
  */

//object HbaseWrite {
//  def main(args: Array[String]): Unit = {
//
//    // 创建SpakConf
//    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("HbaseWrite")
//
//    // 创建SC
//    val sc = new SparkContext(sparkConf)
//
//    // 创建RDD
//    val initialRDD: RDD[(Int, String, Int)] = sc.parallelize(List((1, "apple", 11), (2, "banana", 12), (3, "pear", 13)))
//
//    // 创建JobConf
//    val conf = new JobConf()
//    conf.set("hbase.zookeeper.quorum", "systemhub511,systemhub611,systemhub711")
////    conf.setOutputFormat(classOf[TableOutputFormat[ImmutableBytesWritable]])
//    conf.set(TableOutputFormat.OUTPUT_TABLE, "test")
//
//    // 定义 Hbase 添加数据方法
//    def convert(triple: (Int, String, Int)): (ImmutableBytesWritable, Put) = {
//      val put = new Put(Bytes.toBytes(triple._1))
//      put.addImmutable(Bytes.toBytes("info"), Bytes.toBytes("name"), Bytes.toBytes(triple._2))
//      put.addImmutable(Bytes.toBytes("info"), Bytes.toBytes("price"), Bytes.toBytes(triple._3))(new ImmutableBytesWritable, put)
//    }
//
//    // 转换RDD
//    val writRDD: RDD[(ImmutableBytesWritable, Put)] = initialRDD.map(convert)
//
//    // 写入HBASE
//    writRDD.saveAsHadoopDataset(conf)
//
//    // 关闭资源
//    sc.stop()
//  }
//}
