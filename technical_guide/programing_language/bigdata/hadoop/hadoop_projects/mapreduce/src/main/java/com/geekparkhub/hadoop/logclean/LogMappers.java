package com.geekparkhub.hadoop.logclean;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

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
 * LogMappers
 * <p>
 */

public class LogMappers extends Mapper<LongWritable, Text, Text, NullWritable> {

    Text k = new Text();

    /**
     * Copy map method
     * 复写 map方法
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
         * Get a row of data
         * 获取一行数据
         */
        String line = value.toString();

        /**
         * Is the parsing log legal?
         * 解析日志是否合法
         */
        LogBean logBean = pressLog(line);

        /**
         * If the data is not legal, return directly
         * 如果数据不合法,则直接返回
         */
        if (!logBean.isValid()) {
            return;
        }

        /**
         * Package object
         * 封装对象
         */
        k.set(logBean.toString());

        /**
         * Write data
         * 写出数据
         */
        context.write(k, NullWritable.get());
    }

    /**
     * Parsing log method
     * 解析日志方法
     *
     * @param line
     * @return
     */
    private LogBean pressLog(String line) {
        LogBean logBean = new LogBean();

        /**
         * Cutting data
         * 切割数据
         */
        String[] fields = line.split(" ");

        /**
         * Encapsulate data if the log length is greater than 11.
         * 如果日志长度大于11,则封装数据
         */
        if (fields.length > 11) {
            logBean.setRemote_addr(fields[0]);
            logBean.setRemote_user(fields[1]);
            logBean.setTime_local(fields[3].substring(1));
            logBean.setRequest(fields[6]);
            logBean.setStatus(fields[8]);
            logBean.setBody_bytes_sent(fields[9]);
            logBean.setHttp_referer(fields[10]);

            /**
             * Splice data if the client browser's information is greater than 12.
             * 如果客户浏览器的信息大于12,则拼接数据
             */
            if (fields.length > 12) {
                logBean.setHttp_user_agent(fields[11] + " " + fields[12]);
            } else {
                logBean.setHttp_user_agent(fields[11]);
            }

            /**
             * Clean the data if the network status is greater than 400=HTTPERROR
             * 如果网络状态大于400=HTTPERROR,则清洗该数据
             */
            if (Integer.parseInt(logBean.getStatus()) >= 400) {
                logBean.setValid(false);
            }
        } else {
            logBean.setValid(false);
        }
        return logBean;
    }
}
