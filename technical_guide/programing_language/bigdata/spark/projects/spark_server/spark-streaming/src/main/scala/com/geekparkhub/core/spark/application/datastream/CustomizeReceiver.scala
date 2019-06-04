package com.geekparkhub.core.spark.application.datastream

import java.io.{BufferedReader, InputStreamReader}
import java.net.Socket
import java.nio.charset.StandardCharsets

import org.apache.spark.storage.StorageLevel
import org.apache.spark.streaming.receiver.Receiver

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
  * CustomizeReceiver
  * <p>
  */

class CustomizeReceiver(hostName: String, port: Int) extends Receiver[String](StorageLevel.MEMORY_ONLY) {

  // 开始读取数据
  override def onStart(): Unit = {
    new Thread("receiver") {
      override def run(): Unit = {
        receiver()
      }
    }.start()
  }

  // 读取数据
  def receiver(): Unit = {
    try {
      // 创建 Socket
      val socket = new Socket(hostName, port)
      // 定义变量,用来接收端口传过来的数据
      var input: String = null
      // 创建BufferedReader用于读取端口传来的数据
      val reader = new BufferedReader(new InputStreamReader(socket.getInputStream, StandardCharsets.UTF_8))
      // 赋值
      input = reader.readLine()
      while (input != null) {
        store(input)
        input = reader.readLine()
      }
      // 跳出循环则关闭资源
      reader.close()
      socket.close()

      // 重启流式任务
      restart("restart")
    } catch {
      case e: Exception => restart("restart")
    }
  }

  // 结束读取数据
  override def onStop(): Unit = {}
}