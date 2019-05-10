package com.geekparkhub.hadoop.table;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;

import static org.apache.commons.beanutils.BeanUtils.*;

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
 * TableReducer
 * <p>
 */

public class TableReducer extends Reducer<Text, TableBean, TableBean, NullWritable> {
    /**
     * @param key
     * @param values
     * @param context
     * @throws IOException
     * @throws InterruptedException
     */
    @Override
    protected void reduce(Text key, Iterable<TableBean> values, Context context) throws IOException, InterruptedException {

        /**
         * Store all order collections
         * 存放所有订单集合
         */
        ArrayList<TableBean> orderBeans = new ArrayList<>();

        /**
         * Store all product collections
         * 存放所有产品集合
         */
        TableBean pdBean = new TableBean();

        /**
         * Loop traversal
         * 循环遍历
         */
        for (TableBean tableBean : values) {
            if ("order".equals(tableBean.getFlag())) {
                TableBean tmp = new TableBean();
                try {
                    copyProperties(tmp, tableBean);
                    orderBeans.add(tableBean);
                } catch (IllegalAccessException e) {
                    e.printStackTrace();
                } catch (InvocationTargetException e) {
                    e.printStackTrace();
                }
            } else {
                try {
                    copyProperties(pdBean, tableBean);
                } catch (IllegalAccessException e) {
                    e.printStackTrace();
                } catch (InvocationTargetException e) {
                    e.printStackTrace();
                }
            }
        }

        /**
         * Loop through the orderBeans
         * 循环遍历 orderBeans
         */
        for (TableBean tableBean : orderBeans) {
            tableBean.setPname(pdBean.getPname());
            context.write(tableBean, NullWritable.get());
        }

    }
}