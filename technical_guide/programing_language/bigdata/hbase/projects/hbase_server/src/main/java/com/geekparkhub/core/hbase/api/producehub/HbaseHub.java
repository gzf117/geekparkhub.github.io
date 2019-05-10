package com.geekparkhub.core.hbase.api.producehub;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

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

    /**
     * Public Configuration information
     * 公共配置信息
     */
    private static Admin admin = null;
    private static Connection connection = null;
    private static Configuration configuration;

    static {

        /**
         * HBase ConfigurationFile
         * HBase 配置文件
         */
        configuration = HBaseConfiguration.create();
        configuration.set("hbase.zookeeper.quorum", "172.16.168.130");
        configuration.set("hbase.zookeeper.property.clientPort", "2181");
        try {

            /**
             * Get Connected
             * 获取连接
             */
            connection = ConnectionFactory.createConnection(configuration);

            /**
             * Get HBase Administrator Object
             * 获取HBase管理员对象
             */
            admin = connection.getAdmin();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Close Resource
     * 关闭资源
     *
     * @param conf
     * @param admin
     */
    private static void close(Connection conf, Admin admin) {
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
     * Determine if DataTable Exists
     * 判断数据表是否存在
     *
     * @param tableName
     */
    public static boolean isTableExist(String tableName) throws IOException {

        /**
         * Execution Method
         * 执行方法
         */
        boolean tableExists = admin.tableExists(TableName.valueOf(tableName));

        return tableExists;
    }

    /**
     * Create DataTable
     * 创建数据表
     *
     * @param tableName
     * @param columnFamily
     * @throws IOException
     */
    public static void createTable(String tableName, String... columnFamily) throws IOException {

        /**
         * Verify that the DataTable Exists Before Creating the DataTable
         * 创建数据表前,验证数据表是否存在
         */
        if (isTableExist(tableName)) {
            System.out.printf(tableName + " Data table creation failed , " + tableName + " Data table already exists!" + "\n");
            return;
        }

        /**
         * Instantiation Table Description information
         * 实例化 表描述信息
         */
        HTableDescriptor tableDescriptor = new HTableDescriptor(TableName.valueOf(tableName));

        /**
         * Add Multiple Column Families
         * 添加多个列族
         */
        for (String cn : columnFamily) {
            /**
             * Instantiation Column Name Description information
             * 实例化 列名描述信息
             */
            HColumnDescriptor columnDescriptor = new HColumnDescriptor(String.valueOf(cn));
            tableDescriptor.addFamily(columnDescriptor);
        }

        /**
         * Execution Method
         * 执行方法
         */
        admin.createTable(tableDescriptor);

        /**
         * Logger INFO
         */
        System.out.printf(tableName + " Data Sheet Was Created Successfully!" + "\n");
    }

    /**
     * Delete Data Table
     * 删除数据表
     *
     * @param tableName
     * @throws IOException
     */
    public static void deleteTable(String tableName) throws IOException {

        /**
         * Before Deleting the Data Table, Verify that the Data Table Exists.
         */
        if (!isTableExist(tableName)) {
            System.out.println("Data Table Deletion Failed , Reason : The Data Table Does Not Exist !");
            return;
        }

        /**
         * Data Table Offline
         * 数据表下线
         */
        admin.disableTable(TableName.valueOf(tableName));

        /**
         * Delete Data Table
         * 删除数据表
         */
        admin.deleteTable(TableName.valueOf(tableName));

        /**
         * Logger INFO
         */
        System.out.println("Data Table Has Been Deleted Successfully!");
    }

    /**
     * Adding Data
     * 添加数据
     *
     * @param tableName
     * @param rowKey
     * @param columnFamily
     * @param columnName
     * @param value
     * @throws IOException
     */
    public static void addData(String tableName, String rowKey, String columnFamily, String columnName, String value) throws IOException {

        /**
         * Instantiated Table Object
         * 实例化 表对象
         */
        Table table = connection.getTable(TableName.valueOf(tableName));

        /**
         * Verify that the data table exists before adding data
         * 添加数据前,验证数据表是否存在
         */
        if (!isTableExist(String.valueOf(TableName.valueOf(tableName)))) {
            System.out.println("Adding Data Failed, Reason: " + table + "DataTable Does Not Exist !");
            return;
        }

        /**
         * Instantiate Put Object
         * 实例化 Put对象
         *
         * Convert String type primary key ID to byte data
         * 将String类型主键ID转换字节数据
         */
        Put put = new Put(Bytes.toBytes(rowKey));

        /**
         * Add data (column family/column name/numeric) and convert the String type to a byte array
         * 添加数据 (列族/ 列名 / 数值)并将String类型转换为字节数组
         */
        put.addColumn(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName), Bytes.toBytes(value));

        /**
         * Execution method
         * 执行方法
         */
        table.put(put);

        System.out.println(table.toString() + " Data added Successfully !");

        /**
         * Close resource
         * 关闭资源
         */
        table.close();
    }

    /**
     * Change Data
     * 修改数据
     *
     * @param tableName
     * @param rowKey
     * @param columnFamily
     * @param columnName
     * @param value
     */
    public static void changeData(String tableName, String rowKey, String columnFamily, String columnName, String value) throws IOException {

        /**
         * Instantiated Table Object
         * 实例化 表对象
         */
        Table table = connection.getTable(TableName.valueOf(tableName));

        /**
         * Verify that the data table exists before modifying the data
         * 修改数据前,验证数据表是否存在
         */
        if (!isTableExist(String.valueOf(TableName.valueOf(tableName)))) {
            System.out.println("Change Data Failed, Reason: " + table + "DataTable Does Not Exist !");
            return;
        }

        /**
         * Instantiate Put Object
         * 实例化 Put对象
         *
         * Convert String type primary key ID to byte data
         * 将String类型主键ID转换字节数据
         */
        Put put = new Put(Bytes.toBytes(rowKey));

        /**
         * Change data (column family/column name/numeric) and convert the String type to a byte array
         * 修改数据 (列族/ 列名 / 数值)并将String类型转换为字节数组
         */
        put.addColumn(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName), Bytes.toBytes(value));

        /**
         * Execution method
         * 执行方法
         */
        table.put(put);

        System.out.println(table.toString() + " Data Change Successfully !");

        /**
         * Close resource
         * 关闭资源
         */
        table.close();
    }

    /**
     * Full Table Scan - Query Data
     * 全表扫描 - 查询数据
     *
     * @param tableName
     */
    public static void scanTable(String tableName) throws IOException {

        /**
         * Instantiated Table Object
         * 实例化 表对象
         */
        Table table = connection.getTable(TableName.valueOf(tableName));

        /**
         * Verify that the data table exists before modifying the data
         * 查询数据前,验证数据表是否存在
         */
        if (!isTableExist(String.valueOf(TableName.valueOf(tableName)))) {
            System.out.println("Inquire Data Failed, Reason: " + table + "DataTable Does Not Exist !");
            return;
        }

        /**
         * Instantiation Scanner
         * 实例化 扫描器
         */
        Scan scan = new Scan();

        /**
         * Execution Method
         * 执行方法
         */
        ResultScanner results = table.getScanner(scan);

        /**
         * Traversing RowKey data
         * 遍历RowKey数据
         */
        for (Result result : results) {
            Cell[] cells = result.rawCells();
            /**
             * Traversing the Row Key collection data
             * 遍历RowKey集合数据
             */
            for (Cell cell : cells) {
                System.out.println("RowKey is = " + Bytes.toString(CellUtil.cloneRow(cell))
                        + " & " + "ColumnFamily is = " + Bytes.toString(CellUtil.cloneFamily(cell))
                        + " & " + "ColumnName is = " + Bytes.toString(CellUtil.cloneQualifier(cell))
                        + " & " + "Value is = " + Bytes.toString(CellUtil.cloneValue(cell))
                        + "\n" + ("===========================================================================")
                );
            }
        }

        /**
         * Logger INFO
         */
        System.out.println("FullTable Data Query Success !");

        /**
         * Close resource
         * 关闭资源
         */
        table.close();
    }

    /**
     * Specified Parameter - Query Data
     * 指定参数 - 查询数据
     *
     * @param tableName
     * @param rowKey
     * @param columnFamily
     * @param columnName
     * @throws IOException
     */
    public static void getData(String tableName, String rowKey, String columnFamily, String columnName) throws IOException {

        /**
         * Instantiated Table Object
         * 实例化 表对象
         */
        Table table = connection.getTable(TableName.valueOf(tableName));

        /**
         * Verify that the data table exists before modifying the data
         * 查询数据前,验证数据表是否存在
         */
        if (!isTableExist(String.valueOf(TableName.valueOf(tableName)))) {
            System.out.println("Inquire Data Failed, Reason: " + table + "DataTable Does Not Exist !");
            return;
        }

        /**
         * Instantiate the Get object
         * 实例化Get对象
         */
        Get get = new Get(Bytes.toBytes(rowKey));

        /**
         * Specify column family & column name
         * 指定列族&列名
         */
        get.addColumn(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName));

        /**
         * Execution method
         * 执行方法
         */
        Result result = table.get(get);

        Cell[] cells = result.rawCells();

        /**
         * Traversing the Row Key collection data
         * 遍历RowKey集合数据
         */
        for (Cell cell : cells) {
            System.out.println("RowKey is = " + Bytes.toString(CellUtil.cloneRow(cell))
                    + " & " + "ColumnFamily is = " + Bytes.toString(CellUtil.cloneFamily(cell))
                    + " & " + "ColumnName is = " + Bytes.toString(CellUtil.cloneQualifier(cell))
                    + " & " + "Value is = " + Bytes.toString(CellUtil.cloneValue(cell))
                    + "\n" + ("===========================================================================")
            );
        }

        /**
         * Logger INFO
         */
        System.out.println("Specified Parameter Data Query Success !");

        /**
         * Close resource
         * 关闭资源
         */
        table.close();
    }

    /**
     * Delete Data
     * 删除数据
     *
     * @param tableName
     * @param rowKey
     * @param columnFamily
     * @param columnName
     * @throws IOException
     */
    public static void deleteData(String tableName, String rowKey, String columnFamily, String columnName) throws IOException {

        /**
         * Instantiated Table Object
         * 实例化 表对象
         */
        Table table = connection.getTable(TableName.valueOf(tableName));

        /**
         * Verify that the data table exists before modifying the data
         * 删除数据前,验证数据表是否存在
         */
        if (!isTableExist(String.valueOf(TableName.valueOf(tableName)))) {
            System.out.println("Delete Data Failed, Reason: " + table + "DataTable Does Not Exist !");
            return;
        }

        /**
         * Instantiate the delete object
         * 实例化 delete对象
         */
        Delete delete = new Delete(Bytes.toBytes(rowKey));

        /**
         * 删除指定数据
         */
        delete.addColumns(Bytes.toBytes(columnFamily), Bytes.toBytes(columnName));

        /**
         * Execution method
         * 执行方法
         */
        table.delete(delete);

        /**
         * Logger INFO
         */
        System.out.println("Data Deletion is Successful!");

        /**
         * Close resource
         * 关闭资源
         */
        table.close();
    }

    public static void main(String[] args) throws IOException {

        /**
         * isTableExist Result
         */
        System.out.printf("test isTableExist Result is = " + String.valueOf(isTableExist("test")) + "\n");
        System.out.printf("test001 isTableExist Result is = " + String.valueOf(isTableExist("test001")) + "\n");
        System.out.printf("test002 isTableExist Result is = " + String.valueOf(isTableExist("test002")) + "\n");
        System.out.printf("test003 isTableExist Result is = " + String.valueOf(isTableExist("test003")) + "\n");

        /**
         * CreateTable Result
         */
        createTable("test001", "info");
        createTable("test_factory", "factorymode", "factoryinfo");
        System.out.printf("factory TableExist Result is = " + String.valueOf(isTableExist("factory")) + "\n");
        System.out.printf("test_factory TableExist Result is = " + String.valueOf(isTableExist("test_factory")) + "\n");

        /**
         * Delete Data Table
         */
        deleteTable("test_factory");

        /**
         * Adding Data
         */
        addData("test001", "0003", "info", "name", "testUser003");

        /**
         * Change Data
         */
        changeData("test001", "0003", "info", "name", "testUser004");

        /**
         * Delete Data
         */
        deleteData("test001", "0003", "name", "testUser004");

        /**
         * Full Table Scan - Query Data
         */
        scanTable("test");

        /**
         * Specified Parameter - Query Data
         */
        getData("test", "0001", "info", "name");

        /**
         * Close Resource
         * 关闭资源
         */
        close(connection, admin);
    }
}
