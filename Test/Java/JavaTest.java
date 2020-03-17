
public class JavaTest {
    public static void main(String[] args){
        //System.out.println("Sajjad Jawad .");
        //System.out.println(Math.floor(8.552));
        JavaTest me = new JavaTest();
        /*System.out.println(me.testAge(21));
        System.out.println(me.cakeday(21));
        System.out.println(me.testName("sajjsad"));
        */
        System.out.println(me.fact(6));
        PythonTest py = new PythonTest();
        System.out.println(py.pypy());
    }

    public String testName(String name){

        if (name == "sajjad" || name == "Sajjad" || name == "SAJJAD"){
            return "Sajjad Jawad";
        }
        return "name not allowed";
    }
    public int cakeday(int age){
        return 2020 - age;
    }
    public boolean testAge(int age){
        if (age >= 18){
            return true;
        }
        return false;
    }
    public int fact(int num){
        int out = 1;
        for (int i = 1; i <= num; i++){
            out *= i;
        }
        return out;
    }
}






