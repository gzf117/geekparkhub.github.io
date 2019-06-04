package com.geekparkhub.core.spark.application.methods

import org.apache.spark.rdd.RDD


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
  * Search
  * <p>
  */

class Search(query: String) extends Serializable {

  // 过滤出包含字符串数据
  def isMatch(s: String): Boolean = {
    s.contains(query)
  }

  // 过滤出包含字符串RDD
  def getMatch1(rdd: RDD[String]): RDD[String] = {
    rdd.filter(isMatch)
  }

  // 过滤出包含字符串RDD
  def getMatche2(rdd: RDD[String]): RDD[String] = {
    val q = query
    rdd.filter(x => x.contains(q))
  }
}
