package com.geekparkhub.hadoop.table;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;

import java.io.IOException;

/**
 * Geek International Park | 极客国际公园
 * GeekParkHub | 极客实验室
 * Website | https://www.geekparkhub.com/
 * Description | Open开放 · Creation创想 | OpenSource开放成就梦想 GeekParkHub共建前所未见
 * HackerParkHub | 黑客公园枢纽
 * Website | https://www.hackerparkhub.com/
 * Description | 以无所畏惧的探索精神 开创未知技术与对技术的崇拜
 * GeekDeveloper : JEEP-711
 *
 * @author system
 * <p>
 * TableMapper
 * <p>
 */

public class TableMapper extends Mapper<LongWritable, Text, Text, TableBean> {

    /**
     * file name
     * 文件名称
     */
    String name;

    TableBean tableBean = new TableBean();
    Text k = new Text();

    /**
     * Override initialization method
     * 复写 初始化方法
     *
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void setup(Mapper<LongWritable, Text, Text, TableBean>.Context context) throws IOException, InterruptedException {
        /**
         * Get the file name
         * 获取文件名称
         */
        FileSplit inputSplit = (FileSplit) context.getInputSplit();
        name = inputSplit.getPath().getName();
    }

    /**
     * Rewrite the map() method
     * 复写 map()方法
     *
     * @param key
     * @param value
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        /**
         * Get the first row of data
         * 获取第一行数据
         */
        String line = value.toString();

        /**
         * If it starts with order, it proves to be the order form, otherwise it is the product list.
         * 如果以order开头,则证明是订单表,否则是产品表
         */
        if (name.startsWith("order")) {

            /**
             * Cutting data
             * 切割数据
             */
            String[] flelds = line.split(" ");

            /**
             * Encapsulate key&value object
             * 封装key&value对象
             */
            tableBean.setOrder_id(flelds[0]);
            tableBean.setP_id(flelds[1]);
            tableBean.setAmount(Integer.parseInt(flelds[2]));
            tableBean.setPname("");
            tableBean.setFlag("order");

            /**
             * Set OID
             * 设置OID
             */
            k.set(flelds[1]);
        } else {

            /**
             * Cutting data
             * 切割数据
             */
            String[] flelds = line.split(" ");

            /**
             * Encapsulate key&value object
             * 封装key&value对象
             */
            tableBean.setOrder_id("");
            tableBean.setP_id(flelds[0]);
            tableBean.setAmount(0);
            tableBean.setPname(flelds[1]);
            tableBean.setFlag("pd");

            /**
             * Set the PID
             * 设置PID
             */
            k.set(flelds[0]);
        }

        /**
         * Write data
         * 写出数据
         */
        context.write(k, tableBean);
    }
}