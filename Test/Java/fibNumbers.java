
import java.util.Arrays;

public class MyClass {
    
    public static long[] fib(int len){
        
        long[] fibNumbers = new long[len];
        fibNumbers[0] = 0;
        fibNumbers[1] = 1;
        
        for(int i = 2; i<fibNumbers.length; i++){
            fibNumbers[i] = fibNumbers[i-1] + fibNumbers[i - 2];
        }
        return fibNumbers;
    }
    
    public static void main(String args[]) {
        // first 800 fib number
        System.out.println(Arrays.toString(fib(800)));
    }
}
