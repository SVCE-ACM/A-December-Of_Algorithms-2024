import java.time.Duration;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
class Record{
    String time,id;
    int t_level;
    public Record(String id,String time,int t_level)
    {
        this.time=time;this.t_level=t_level;this.id=id;
    }   
    @Override
    public String toString() {
        return "{id: " + id + ", timestamp: " + time + ", threat_level: " + t_level + "}";
    }
}
public class Day17_java_Hari7467
{
    static Map<String,List<Record>> threadtable=new LinkedHashMap<>();
    static DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");
    static List<Record> output=new ArrayList<>();
    private static void addrecord(String id,String time,int t_level)
    {
        threadtable.putIfAbsent(id, new ArrayList<>());
        threadtable.get(id).add(new Record(id,time,t_level));
          
    }
    private static void duplicate_alerts()
    {
           
            LocalTime startTime = LocalTime.parse("00:00:00", formatter);
            LocalTime endTime = LocalTime.parse("00:00:00", formatter);
            LocalTime current_i = LocalTime.parse("00:00:00", formatter);
            LocalTime current_j = LocalTime.parse("00:00:00", formatter);
            for(Map.Entry<String,List<Record>> thread:threadtable.entrySet())
            {
                List<Record> records = thread.getValue();
                for(int i=0;i<records.size();i++)
                {
                    current_i=LocalTime.parse(records.get(i).time, formatter);
                    startTime=current_i;
                    int sec=current_i.getSecond();
                    endTime=endTime.withSecond((30-sec)+sec);
                    for(int j=i+1;j<records.size();j++)
                    {
                        current_j=LocalTime.parse(records.get(j).time, formatter);
                        if(current_j.isAfter(startTime) && current_j.isBefore(endTime))
                        {
                            records.remove(j);
                            j--;
                        }
                    }
                }
            }     
    }
    private static void  priority_update()
    {   
        for(Map.Entry<String,List<Record>> thread:threadtable.entrySet())
        {
            List<Record> records = thread.getValue();
            int high_level=records.get(0).t_level;
            for(int i=1;i<records.size();i++)
            {
                if(high_level<records.get(i).t_level)
                {
                    high_level=records.get(i).t_level;
                    i--;
                    records.remove(i);
                }  
            }
        } 
    }
    private static void Eviction()
    {
            for(Map.Entry<String,List<Record>> thread:threadtable.entrySet())
            {
                List<Record> records = thread.getValue();
                for(int i=1;i<records.size();i++)
                {
                    LocalTime time1=LocalTime.parse(records.get(i-1).time);
                    
                        LocalTime time2=LocalTime.parse(records.get(i).time);
                        Duration duration=Duration.between(time1, time2);
                        Long sec=duration.toSeconds();
                        if(sec<300)
                        {
                            i=i-1;;
                            records.remove(i);
                            
                        }
                }
            }     
    }
    private static void result()
    {
        for(Map.Entry<String,List<Record>> thread:threadtable.entrySet())
        {
            output.addAll(thread.getValue());
        }
        output.sort(Comparator.comparing(record -> record.time));
    }
    
    private static void alert_management()
    {
        duplicate_alerts();
        priority_update();
        Eviction();
        result();
    }
    private static void display()
    {
        System.out.println(output);
    }
    public static void main(String[] args)
    {
          List<Record> records = Arrays.asList(
                new Record("A123", "00:00:10", 3),
                new Record("A123", "00:00:15", 3), 
                new Record("B456","00:00:20", 2),
                new Record("A123","00:00:30", 5), 
                new Record("B456", "00:05:05", 2)
        );
        for(Record record:records)
        {
            addrecord(record.id, record.time, record.t_level);
        }
        alert_management();
        display();
    }
}
