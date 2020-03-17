
public class MyClass {
    public static void main(String[] args){
        System.out.println("start Main . ");
        
        // now class methods
        MyClass methods = new MyClass();
        
        int age = 21;
        String fullName = "Sajjad Jawad";
        
        
        for(int i = 0; i < methods.fullName(fullName).length; i++){
            System.out.println(methods.fullName(fullName)[i]);
        }
            
        System.out.println(methods.firstName(fullName));
        System.out.println(methods.birthDay(age));
        System.out.println(methods.years(1999, 2020));
        System.out.println(methods.fullName(fullName));
    }
    
    public String firstName(String fullName){
        MyClass name = new MyClass();
        String firstName = name.fullName(fullName)[0];
        return firstName;
    }
    
    public String[] fullName(String fullName){
        String[] fullNameArray = fullName.split("\\s+");
        return fullNameArray;
    }
    
    public int birthDay(int age){
        return 2020 - age;
    }
    
    public int[] years(int start, int end){
        
        int[] allYears = new int[end - start];
        // System.out.println(allYears);
        
        for(int i=0; i < allYears.length; i++){
            allYears[i] = start + i;
        }
        for(int i=0; i < allYears.length; i++){
            System.out.println(allYears[i]);
        }
        return allYears;
    }
}

