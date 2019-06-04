package com.geekparkhub.core.spark.application.partitioner

import org.apache.spark.Partitioner

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
  * CustomerPartitioner
  * <p>
  */

class CustomerPartitioner(partitions: Int) extends Partitioner {
  override def numPartitions: Int = partitions
  override def getPartition(key: Any): Int = {
    0
  }
}
