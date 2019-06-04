package com.geekparkhub.core.spark.application.methods

import org.apache.spark.rdd.RDD
import org.apache.spark.util.LongAccumulator
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
  * AccuAction
  * <p>
  */

object AccuAction {
  def main(args: Array[String]): Unit = {

    // 创建SpakConf
    val sparkConf: SparkConf = new SparkConf().setMaster("local[*]").setAppName("AccuAction")

    // 创建SC
    val sc = new SparkContext(sparkConf)

    // 累加器
//    val sum: LongAccumulator = sc.longAccumulator("sum")
    val sum = new AccumulatorAction

    // 注册自定义累加器
    sc.register(sum)

    // 创建RDD
    val value: RDD[Int] = sc.parallelize(Array(1, 2, 3, 4))

    val word: RDD[(Int, Int)] = value.map(x => {
      // 添加累加
      sum.add(x)
      (x, 1)
    })

    word.collect().foreach(println)

    println(sum.value)

    // 关闭资源
    sc.stop()
  }
}
