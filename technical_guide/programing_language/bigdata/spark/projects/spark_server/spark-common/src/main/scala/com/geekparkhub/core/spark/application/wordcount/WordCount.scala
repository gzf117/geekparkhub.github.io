package com.geekparkhub.core.spark.application.wordcount

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
  * WordCountApplication
  * <p>
  */

object WordCount {
  def main(args: Array[String]): Unit = {

    /**
      * Create SparkConf
      * 创建 SparkConf
      */
    val sparkConf = new SparkConf().setMaster(args(0)).setAppName("WordCountApplication")

    /**
      * Create SparkContext
      * 创建 SparkContext
      */
    val sc = new SparkContext()

    /**
      * Read file
      * 读取文件
      */
    val line: RDD[String] = sc.textFile(args(1))

    /**
      * To flatten
      * 压平
      */
    val word: RDD[String] = line.flatMap(_.split(" "))

    /**
      * Word conversion dual group
      * 单词转换二元组
      */
    val wordAndOne: RDD[(String, Int)] = word.map((_, 1))

    /**
      * Count the total number of words
      * 统计单词总数
      */
    val wordCount: RDD[(String, Int)] = wordAndOne.reduceByKey(_+_)

    /**
      * Write out the file
      * 写出文件
      */
    wordCount.saveAsTextFile(args(2))

    /**
      * Close resource
      * 关闭资源
      */
    sc.stop()
  }
}
