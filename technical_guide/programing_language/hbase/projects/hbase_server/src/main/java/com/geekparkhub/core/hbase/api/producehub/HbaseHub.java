package com.geekparkhub.core.hbase.api.producehub;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.Admin;
import org.apache.hadoop.hbase.client.Connection;
import org.apache.hadoop.hbase.client.ConnectionFactory;

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
 * HbaseHub
 * <p>
 */

public class HbaseHub {

    private static Admin admin = null;

    /**
     * Public configuration information
     * 公共配置信息
     */
    static {

        /**
         * HBase configuration file
         * HBase 配置文件
         */
        Configuration configuration = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "172.16.168.130");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");

        try {
            /**
             * Get connected
             * 获取连接
             */
            Connection connection = ConnectionFactory.createConnection(configuration);

            /**
             * Get the HBase administrator object
             * 获取HBase管理员对象
             */
            admin = connection.getAdmin();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Close resource
     * 关闭资源
     *
     * @param conf
     * @param admin
     */
    private void close(Connection conf, Admin admin) {
        if (conf != null) {
            try {
                conf.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        if (admin != null) {
            try {
                admin.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Determine if the data table exists
     * 判断数据表是否存在
     *
     * @param tableName
     */
    public static boolean isTableExist(String tableName) throws IOException {

        /**
         * Execution method
         * 执行方法
         */
        boolean tableExists = admin.tableExists(TableName.valueOf(tableName));

        /**
         * Close resource
         * 关闭资源
         */
        admin.close();

        return tableExists;
    }

    /**
     * Create a data table
     * 创建数据表
     */
    private static void createTable(String tableName, String... columnName) throws IOException {

        /**
         * Verify that the data table exists before creating the data table
         * 创建数据表前,验证数据表是否存在
         */
        if (isTableExist(tableName)) {
            System.out.printf(tableName + " Data table creation failed , " + tableName + " Data table already exists!" + "\n");
            return;
        }

        /**
         * Instantiation table description information
         * 实例化 表描述信息
         */
        HTableDescriptor tableDescriptor = new HTableDescriptor(TableName.valueOf(tableName));

        /**
         * Add multiple column families
         * 添加多个列族
         */
        for (String cn : columnName) {

            /**
             * Instantiation column name description information
             * 实例化 列名描述信息
             */
            HColumnDescriptor columnDescriptor = new HColumnDescriptor(String.valueOf(cn));
            tableDescriptor.addFamily(columnDescriptor);
        }

        /**
         * Execution method
         * 执行方法
         */
        admin.createTable(tableDescriptor);

        System.out.printf(tableName + " Data sheet was created successfully!" + "\n");
    }

    /**
     * Delete data table
     * 删除数据表
     */

    /**
     * adding data
     * 添加数据
     */

    /**
     * change the data
     * 修改数据
     */

    /**
     * Query data
     * 查询数据
     */

    /**
     * delete data
     * 删除数据
     */

    public static void main(String[] args) throws IOException {

        /**
         * isTableExist Result
         */
        System.out.printf("test isTableExist Result is = " + String.valueOf(isTableExist("test")) + "\n");
        System.out.printf("test001 isTableExist Result is = " + String.valueOf(isTableExist("test001")) + "\n");
        System.out.printf("test002 isTableExist Result is = " + String.valueOf(isTableExist("test002")) + "\n");
        System.out.printf("test003 isTableExist Result is = " + String.valueOf(isTableExist("test003")) + "\n");


        /**
         * createTable Result
         */
        createTable("test001", "info");
        createTable("test_factory", "factorymode", "factoryinfo");
        System.out.printf("factory TableExist Result is = " + String.valueOf(isTableExist("factory")) + "\n");
        System.out.printf("test_factory TableExist Result is = " + String.valueOf(isTableExist("test_factory")) + "\n");
    }
}
