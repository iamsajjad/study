public class Project{
    
    int version;
    String project;
    int year;
    String platform;
    String creater = "Sajjad";
    
    int arr[] = {0,10,2,30,4,50,6,70,8,90};
    
    Project(int version, String project, int year, String platform)
    {
        this.version = version;
        this.project = project;
        this.year = year;
        this.platform = platform;
        this.creater = creater;
    }
    
    float getVersion() {
        float version = this.version;
        return version;
    }
    
    long sumArr() {
        long sumarr = 0;
        for(int i=0; i < this.arr.length; i++){
            System.out.println(arr[i]);
            sumarr += arr[i];
        }
        return sumarr;
    }
    
    String info() {
        String information = "";
        
        if(this.platform == "linux"){
            information = "* ";
        }
        // str to int Integer.parseInt();
        information = information + Integer.toString(this.version) + " " + this.project + " " +
                      Integer.toString(this.year) + " " + this.platform;
        return information;
    }
    
    long subArr() {
        
        int counter = this.arr.length - 1;
        long sumarr = 0;
        while(counter != 0){
            sumarr += this.arr[counter];
            counter--;
        } 
        return sumarr;
    }
    
    public static void main(String args[]){
        System.out.println("from Project");
    }
}
