import com.geekparkhub.core.application.analysis.pornhub.PornhubActionETLUtil;

public class PornhubActionETLTest {
    public static void main(String[] args) {
        String ETL_001 = PornhubActionETLUtil.getETLString("LKh7zAJ4nwo\tTheReceptionist\t653\tEntertainment\t424\t13021\t 4.34\t1305\t744\tDjdA-5oKYFQ\tNxTDlnOuybo\tc-8VuICzXtU\tDH56yrIO5nI\tW1Uo5DQTtzc\tE-3zXq_r4w0\t1TCeoRPg5dE\tyAr26YhuYNY\t2ZgXx72XmoE\t-7ClGo-YgZ0\tvmdPOOd6cxI\tKRHfMQqSHpk\tpIMpORZthYw\t1tUDzOp10pk\theqocRij5P0\t_XIuvoH6rUg\tLGVU5DsezE0\tuO2kj6_D8B4\txiDqywcDQRM\tuX81lMev6_o");
        System.out.println(" ETL_Result-001 is = " + ETL_001);

        String ETL_002 = PornhubActionETLUtil.getETLString("LKh7zAJ4nwo\tTheReceptionist\t653\tEntertainment\t424\t13021\t 4.34\t1305\t744");
        System.out.println(" ETL_Result-002 is = " + ETL_002);

        String ETL_003 = PornhubActionETLUtil.getETLString("SDNkMu8ZT68\tw00dy911\t630\tPeople & Blogs\t186\t10181\t3.49\t494\t257\trjnbgpPJUks");
        System.out.println(" ETL_Result-003 is = " + ETL_003);
    }
}
