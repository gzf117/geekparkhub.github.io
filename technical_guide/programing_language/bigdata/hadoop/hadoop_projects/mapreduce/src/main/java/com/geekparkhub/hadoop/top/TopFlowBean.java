package com.geekparkhub.hadoop.top;

import org.apache.hadoop.io.WritableComparable;

import java.io.DataInput;
import java.io.DataOutput;
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
 * TopFlowBean
 * <p>
 */

public class TopFlowBean implements WritableComparable<TopFlowBean> {

    /**
     * Total flow
     * 总流量
     */
    private Long sumFlow;

    /**
     * phone number
     * 手机号
     */
    private String phoneNum;

    /**
     * When deserializing, you need to reflect the call to the null parameter constructor.
     * 反序列化时,需要反射调用空参构造器
     */
    public TopFlowBean() {
        super();
    }

    /**
     * Parametric constructor
     * 有参构造器
     *
     * @param sumFlow
     * @param phoneNum
     */
    public TopFlowBean(Long sumFlow, String phoneNum) {
        super();
        this.sumFlow = sumFlow;
        this.phoneNum = phoneNum;
    }

    /**
     * Serialization method
     * 序列化方法
     *
     * @param out
     * @throws IOException
     */
    @Override
    public void write(DataOutput out) throws IOException {
        out.writeLong(sumFlow);
        out.writeUTF(phoneNum);

    }

    /**
     * Deserialization method, the deserialization method read order must be consistent with the write order of the write serialization method
     * 反序列化方法,反序列化方法读顺序必须和写序列化方法的写顺序必须一致
     *
     * @param in
     * @throws IOException
     */
    @Override
    public void readFields(DataInput in) throws IOException {
        this.sumFlow = in.readLong();
        this.phoneNum = in.readUTF();
    }

    /**
     * Rewrite the compare To() method
     * 重写compareTo()方法
     *
     * @param bean
     * @return
     */
    @Override
    public int compareTo(TopFlowBean bean) {
        int result;
        result = this.sumFlow.compareTo(bean.sumFlow);
        if ((result == 0)) {
            result = this.phoneNum.compareTo(bean.phoneNum);
        }
        return result;
    }

    /**
     * Get&Set method
     * Get&Set方法
     *
     * @return
     */
    public Long getSumFlow() {
        return sumFlow;
    }

    public void setSumFlow(Long sumFlow) {
        this.sumFlow = sumFlow;
    }

    public String getPhoneNum() {
        return phoneNum;
    }

    public void setPhoneNum(String phoneNum) {
        this.phoneNum = phoneNum;
    }

    /**
     * Write a to String method to facilitate subsequent printing to text
     * 编写toString方法,方便后续打印到文本
     */
    @Override
    public String toString() {
        return sumFlow + "\t" + phoneNum;
    }
}
