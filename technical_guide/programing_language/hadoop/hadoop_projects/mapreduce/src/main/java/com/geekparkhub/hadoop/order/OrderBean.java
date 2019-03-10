package com.geekparkhub.hadoop.order;

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
 * OrderBean
 * <p>
 */

public class OrderBean implements WritableComparable<OrderBean> {

    /**
     * OrderBean attribute Product ID
     * OrderBean属性 商品ID
     */
    private int order_id;

    /**
     * OrderBean attribute
     * OrderBean属性 商品金额
     */
    private double order_money;

    /**
     * OrderBean no-argument constructor
     * OrderBean 无参构造器
     */
    public OrderBean() {
        super();
    }

    /**
     * OrderBean parameter constructor
     * OrderBean 参数构造器
     *
     * @param order_id
     * @param order_money
     */
    public OrderBean(int order_id, double order_money) {
        super();
        this.order_id = order_id;
        this.order_money = order_money;
    }

    /**
     * Rewrite the compare To() method
     * 重写compareTo()方法
     * <p>
     * Handling core business logic
     * 处理核心业务逻辑
     *
     * @param bean
     * @return
     */

    @Override
    public int compareTo(OrderBean bean) {

        /**
         * Sort by order ID in ascending order, if the same will be sorted by item amount in descending order
         * 先按照订单ID升序排序,如果相同将按照商品金额降序排序.
         */

        /**
         * Sort status
         * 排序状态
         *
         * State 1 : Indicates positive order sort
         * State -1 : Indicates descending sort
         * State 0 : Indicates equal
         *
         * 状态 1  : 表示 正序排序
         * 状态 -1 : 表示降序排序
         * 状态 0 : 表示相等
         */
        int result;

        if (order_id > bean.getOrder_id()) {
            result = 1;
        } else if (order_id < bean.getOrder_id()) {
            result = -1;
        } else {
            if (order_money > bean.getOrder_money()) {
                result = -1;
            } else if (order_money < bean.getOrder_money()) {
                result = 1;
            } else {
                result = 0;
            }
        }
        return result;
    }

    /**
     * Rewrite serialization method
     * 重写 序列化方法
     *
     * @param out
     * @throws IOException
     */
    @Override
    public void write(DataOutput out) throws IOException {
        out.writeInt(order_id);
        out.writeDouble(order_money);
    }

    /**
     * Overwrite deserialization method
     * 重写 反序列化方法
     *
     * @param in
     * @throws IOException
     */
    @Override
    public void readFields(DataInput in) throws IOException {
        order_id = in.readInt();
        order_money = in.readDouble();
    }

    /**
     * Get & Set method
     * Get & Set方法
     *
     * @return
     */
    public int getOrder_id() {
        return order_id;
    }

    public void setOrder_id(int order_id) {
        this.order_id = order_id;
    }

    public double getOrder_money() {
        return order_money;
    }

    public void setOrder_money(double order_money) {
        this.order_money = order_money;
    }

    /**
     * To String method
     * toString方法
     *
     * @return
     */
    @Override
    public String toString() {
        return order_id + "\t" + order_money;
    }
}
