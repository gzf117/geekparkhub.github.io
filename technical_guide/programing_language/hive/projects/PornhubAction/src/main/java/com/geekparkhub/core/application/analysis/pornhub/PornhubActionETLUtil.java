package com.geekparkhub.core.application.analysis.pornhub;

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
 * PornhubActionETLUtil
 * <p>
 * 过滤不合法数据 | Filter illegal data
 * 去除类别字段中的空格 | Remove spaces in the category field
 * 将\t替换成&符 | Replace \t with ampersand
 * <p>
 */

public class PornhubActionETLUtil {

    /**
     * Data cleaning Method
     * 数据清洗方法
     *
     * @param ori
     * @return
     */
    public static String getETLString(String ori) {

        /**
         * 1.Get data and cut data
         * 获取数据并切割数据
         */
        String[] split = ori.split("\t");

        /**
         * 2.Filter illegal data
         * 过滤不合法数据
         */
        if (split.length < 9) {
            return null;
        }

        /**
         * 3.Remove spaces in the category field
         * 去除类别字段中的空格
         */
        split[3] = split[3].replace(" ", "");

        /**
         * 4.Replace \t with ampersand
         * 将\t替换成&符
         */
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < split.length; i++) {
            if (i < 9) {
                // 如果字段长度相等,则不追加\t字符
                if (i == split.length - 1) {
                    sb.append(split[i]);
                } else {
                    // 如果字段长度小于9,则追加\t字符
                    sb.append(split[i] + "\t");
                }
            } else {
                // 如果字段长度相等,则不追加字符
                if (i == split.length - 1) {
                    sb.append(split[i]);
                } else {
                    // 如果字段长度小于9,则追加&字符
                    sb.append(split[i] + "&");
                }
            }
        }
        return sb.toString();
    }
}
