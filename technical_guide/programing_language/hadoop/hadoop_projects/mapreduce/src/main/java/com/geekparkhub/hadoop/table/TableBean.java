package com.geekparkhub.hadoop.table;

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
 *
 * @author system
 * <p>
 * TableBean
 * <p>
 */

public class TableBean implements Writable {

    /**
     * Order ID
     * 订单ID
     */
    private String order_id;

    /**
     * Product ID
     * 产品ID
     */
    private String p_id;

    /**
     * Merchandise Quantity
     * 产品数量
     */
    private int amount;

    /**
     * Product Name
     * 产品名称
     */
    private String pname;

    /**
     * Table Mark
     * 表标记
     */
    private String flag;

    /**
     * Empty reference constructor
     * 空参构造器
     */
    public TableBean() {
        super();
    }

    /**
     * Parameter constructor
     * 参数构造器
     * @param order_id
     * @param p_id
     * @param amount
     * @param pname
     * @param flag
     */
    public TableBean(String order_id, String p_id, int amount, String pname, String flag) {
        this.order_id = order_id;
        this.p_id = p_id;
        this.amount = amount;
        this.pname = pname;
        this.flag = flag;
    }

    /**
     * Copy serialization method
     * 复写 序列化方法
     * @param out
     * @throws IOException
     */
    @Override
    public void write(DataOutput out) throws IOException {
        out.writeUTF(order_id);
        out.writeUTF(p_id);
        out.writeInt(amount);
        out.writeUTF(pname);
        out.writeUTF(flag);
    }

    /**
     * Overwrite deserialization method
     * 复写 反序列化方法
     * @param in
     * @throws IOException
     */
    @Override
    public void readFields(DataInput in) throws IOException {
        this.order_id = in.readUTF();
        this.p_id = in.readUTF();
        this.amount = in.readInt();
        this.pname = in.readUTF();
        this.flag = in.readUTF();
    }

    /**
     * Get&Set method
     * Get&Set方法
     */
    public String getOrder_id() {
        return order_id;
    }

    public void setOrder_id(String order_id) {
        this.order_id = order_id;
    }

    public String getP_id() {
        return p_id;
    }

    public void setP_id(String p_id) {
        this.p_id = p_id;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public String getPname() {
        return pname;
    }

    public void setPname(String pname) {
        this.pname = pname;
    }

    public String getFlag() {
        return flag;
    }

    public void setFlag(String flag) {
        this.flag = flag;
    }

    /**
     * Override toString() method
     * 复写 toString()方法
     * @return
     */
    @Override
    public String toString() {
        return order_id + "\t" + pname + "\t" + amount + "\t" ;
    }
}
