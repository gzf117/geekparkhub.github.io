package com.geekparkhub.hadoop.logclean;

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
 * LogBean
 * <p>
 */

public class LogBean {

    /**
     *
     * 194.237.142.21 | (Indicating the ip address of the recording client.)
     * - - | (Indicating the record client user name, ignoring attributes.)
     * [18/Sep/2013:06:49:18 +0000] | (Indicating record access time With the time zone.)
     * "GET /wp-content/uploads/2013/07/rstudio-git3.png HTTP/1.1" | (indicating the url of the request request and the http protocol.)
     * 304 | (indicating the status of the record request, the success is 200.)
     * 0 | (Indicating the size of the content of the file sent to the client file.)
     * "-" | (indicating the path used to record the user's access to the page.)
     * "Mozilla/4.0 (compatible;)" | (Indicates information about the client's browser.)
     *
     *  194.237.142.21 | (表示记录客户端的ip地址)
     *  - - | (表示记录客户端用户名称,忽略属性)
     *  [18/Sep/2013:06:49:18 +0000] | (表示记录访问时间与时区)
     *  "GET /wp-content/uploads/2013/07/rstudio-git3.png HTTP/1.1" | (表示记录请求的url与http协议)
     *  304 | (表示记录请求状态,成功是200)
     *  0 | (表示记录发送给客户端文件主体内容大小)
     *  "-" | (表示用来记录用户访问页面链接途径)
     *  "Mozilla/4.0 (compatible;)" | (表示记录客户浏览器的相关信息)
     *
     */

    /**
     * Indicates the ip address of the recording client.
     * 表示记录客户端的ip地址.
     */
    private String remote_addr;

    /**
     * Indicates the record client user name, ignoring attributes.
     * 表示记录客户端用户名称,忽略属性.
     */
    private String remote_user;

    /**
     * Indicates the record access time and time zone.
     * 表示记录访问时间与时区.
     */
    private String time_local;

    /**
     * Indicates the url of the record request and the http protocol.
     * 表示记录请求的url与http协议.
     */
    private String request;

    /**
     * Indicates the status of the record request. The success is 200.
     * 表示记录请求状态,成功是200.
     */
    private String status;

    /**
     * Indicates the size of the body of the file sent to the client.
     * 表示记录发送给客户端文件主体内容大小.
     */
    private String body_bytes_sent;

    /**
     * Indicates the path used to record the user's access to the page.
     * 表示用来记录用户访问页面链接途径.
     */
    private String http_referer;

    /**
     * Indicates information about the client's browser.
     * 表示记录客户浏览器的相关信息.
     */
    private String http_user_agent;

    /**
     * Determine if the data is legal.
     * 判断数据是否合法.
     */
    private boolean valid = true;

    /**
     * Get & Set method
     * Get & Set 方法
     *
     * @return
     */
    public String getRemote_addr() {
        return remote_addr;
    }

    public void setRemote_addr(String remote_addr) {
        this.remote_addr = remote_addr;
    }

    public String getRemote_user() {
        return remote_user;
    }

    public void setRemote_user(String remote_user) {
        this.remote_user = remote_user;
    }

    public String getTime_local() {
        return time_local;
    }

    public void setTime_local(String time_local) {
        this.time_local = time_local;
    }

    public String getRequest() {
        return request;
    }

    public void setRequest(String request) {
        this.request = request;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getBody_bytes_sent() {
        return body_bytes_sent;
    }

    public void setBody_bytes_sent(String body_bytes_sent) {
        this.body_bytes_sent = body_bytes_sent;
    }

    public String getHttp_referer() {
        return http_referer;
    }

    public void setHttp_referer(String http_referer) {
        this.http_referer = http_referer;
    }

    public String getHttp_user_agent() {
        return http_user_agent;
    }

    public void setHttp_user_agent(String http_user_agent) {
        this.http_user_agent = http_user_agent;
    }

    public boolean isValid() {
        return valid;
    }

    public void setValid(boolean valid) {
        this.valid = valid;
    }

    /**
     * To String method
     * toString方法
     */
    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(this.valid);
        stringBuilder.append("\001").append(this.remote_addr);
        stringBuilder.append("\001").append(this.remote_user);
        stringBuilder.append("\001").append(this.time_local);
        stringBuilder.append("\001").append(this.request);
        stringBuilder.append("\001").append(this.status);
        stringBuilder.append("\001").append(this.body_bytes_sent);
        stringBuilder.append("\001").append(this.http_referer);
        stringBuilder.append("\001").append(this.http_user_agent);
        return stringBuilder.toString();
    }
}
