package com.geekparkhub.core.spark.application.sparksql

import org.apache.spark.SparkContext
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.types.{IntegerType, StructField, StructType}
import org.apache.spark.sql.{DataFrame, Row, SparkSession}

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
  * SqlAction
  * <p>
  */

object SqlAction {
  def main(args: Array[String]): Unit = {

    // 创建SparkSession
    val sparkSession: SparkSession = SparkSession
      .builder().master("local[*]").appName("SqlAction").getOrCreate()

    // 创建SC
    val sc: SparkContext = sparkSession.sparkContext

    // 创建 RDD
    val rdd: RDD[Int] = sc.parallelize(Array(1,2,3,4,5))

    // 将Int类型RDD转换为Row类型RDD
    val rowRDD: RDD[Row] = rdd.map(x => {Row(x)})

    // 数据输出
    rowRDD.collect().foreach(println)

    // 创建元数据信息
    val structType = new StructType
    val structTypes: StructType = structType.add(StructField("id", IntegerType))
    val dataFrame: DataFrame = sparkSession.createDataFrame(rowRDD,structTypes)

    // 导入隐式转换
    import sparkSession.implicits._

    // 创建DF
    val df: DataFrame = sparkSession.read.json("/Volumes/GEEK-SYSTEM/Technical_Framework/spark/projects/spark_server/spark-sql/data/people.json")

    // SQL风格 数据查询 | 创建临时表
    df.createTempView("PEOPLE")
    sparkSession.sql("SELECT * FROM PEOPLE").show()

    // DSL风格 数据查询
    df.select("name").show()
    dataFrame.select("id").show()

    // 关闭资源
    sparkSession.stop()
  }
}
