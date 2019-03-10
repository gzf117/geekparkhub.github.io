package com.geekparkhub.hadoop.flowsum;

import org.apache.hadoop.io.Writable;
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
 * @author system
 * <p>
 * FlowBean 序列化
 * <p>
 */

public class FlowBean implements Writable {

    /**
     * Upstream traffic
     * 上行流量
     */
    private long upFlow;

    /**
     * Downstream traffic
     * 下行流量
     */
    private long downFlow;

    /**
     * Total flow
     * 总流量
     */
    private long sumFlow;

    /**
     * When deserializing, you need to reflect the call to the null parameter constructor.
     * 反序列化时,需要反射调用空参构造器
     */
    public FlowBean() {
        super();
    }

    /**
     * Parametric constructor
     * 有参构造器
     *
     * @param upFlow
     * @param downFlow
     */
    public FlowBean(long upFlow, long downFlow) {
        super();
        upFlow = upFlow;
        downFlow = downFlow;
        sumFlow = upFlow + downFlow;
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
        out.writeLong(upFlow);
        out.writeLong(downFlow);
        out.writeLong(sumFlow);
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
        upFlow = in.readLong();
        downFlow = in.readLong();
        sumFlow = in.readLong();
    }

    /**
     * Write a to String method to facilitate subsequent printing to text
     * 编写toString方法,方便后续打印到文本
     *
     * @return
     */
    @Override
    public String toString() {
        return upFlow + "\t" + downFlow + "\t" + sumFlow;
    }

    /**
     * Get&Set method
     * Get&Set方法
     *
     * @return
     */
    public long getUpFlow() {
        return upFlow;
    }

    public void setUpFlow(long upFlow) {
        this.upFlow = upFlow;
    }

    public long getDownFlow() {
        return downFlow;
    }

    public void setDownFlow(long downFlow) {
        this.downFlow = downFlow;
    }

    public long getSumFlow() {
        return sumFlow;
    }

    public void setSumFlow(long sumFlow) {
        this.sumFlow = sumFlow;
    }

    public void set(long upFlow2,long downFlow2){
        upFlow = upFlow2;
        downFlow = downFlow2;
        sumFlow = upFlow2 + downFlow2;
    }

}
