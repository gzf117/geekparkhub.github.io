package com.geekparkhub.hadoop.flowsum;

import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.io.Text;
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
 * FlowCountReducer 序列化
 * <p>
 */

public class FlowCountReducer extends Reducer<Text,FlowBean,Text,FlowBean> {

    FlowBean v = new FlowBean();

    @Override
    protected void reduce(Text key, Iterable<FlowBean> values, Context context) throws IOException, InterruptedException {

        long sum_upFlow = 0;
        long sum_downFlow = 0;

        /**
         * Cumulative summation
         * 累加求和
         */
        for (FlowBean flowBean : values){
            sum_upFlow += flowBean.getUpFlow();
            sum_downFlow += flowBean.getDownFlow();
        }
        v.set(sum_upFlow,sum_downFlow);

        /**
         * data input
         * 写入数据
         */
        context.write(key,v);
    }
}
