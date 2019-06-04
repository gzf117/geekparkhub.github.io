package com.geekparkhub.core.spark.application.methods

import org.apache.spark.util.AccumulatorV2

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
  * AccumulatorAction
  * <p>
  */

class AccumulatorAction extends AccumulatorV2[Int,Int]{

  var sum  = 0

  // 判断是否为空
  override def isZero: Boolean = sum == 0

  // 复制方法
  override def copy(): AccumulatorV2[Int, Int] = {
    val accumulatorAction = new AccumulatorAction
    accumulatorAction.sum = this.sum
    accumulatorAction
  }

  // 重置方法
  override def reset(): Unit = 0

  // 累加方法
  override def add(v: Int): Unit = sum += v

  // 合并方法
  override def merge(other: AccumulatorV2[Int, Int]): Unit = sum += other.value

  // 返回值
  override def value: Int = sum
}
