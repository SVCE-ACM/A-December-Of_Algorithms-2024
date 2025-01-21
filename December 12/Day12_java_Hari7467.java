import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day12_java_Hari7467 {
    static void sortvip(List<String> customers)
    {
        customers.sort((c1, c2) -> {
            boolean isC1VIP = c1.endsWith("VIP");
            boolean isC2VIP = c2.endsWith("VIP");
            return Boolean.compare(!isC1VIP, !isC2VIP);
        });
    }
    public static int extract_number(String one_cuctomer)
    {
        Matcher matcher=Pattern.compile("\\d+").matcher(one_cuctomer);
        return matcher.find()?Integer.valueOf(matcher.group()):0;
    }
    public static String extract_name(String one_customer)
    {
        return one_customer.split(" ")[0];
    }
    public static void smartsystem(List<String> customers,int tickets)
    {
        for(int i=0;i<customers.size();i++)
        {
            String customer=customers.get(i);
            int ticketRequested=extract_number(customer);
            String name=extract_name(customer);
            if(tickets>0){
                int ticketsserved=Math.min(ticketRequested,tickets);
                customers.set(i,name + " Purchased " + ticketsserved + " tickets");
                tickets-=ticketsserved;
            }
            else{
               
                customers.set(i, name + " was not served");
            }
        }
    }
    public static void main(String[] args) {
        List<String> customers=new ArrayList<>(Arrays.asList("Eve 4","Diana 3 VIP","Adam 5","Frank 6 VIP"));
        int tickets=10;
        sortvip(customers);
        smartsystem(customers,tickets);
        System.out.println(customers);
    }
}
