
import java.lang.Math;

public class Star{
    
    // method without static mean must call by class instance (class object)
    double number(int num){
        if(num % 2 == 0){
            System.out.println(num + " is even");
        } else {
            System.out.println(num + " is odd");
        }
        
        if (num < 0){
            System.out.println(num + " is nagtive");
        } else {
            System.out.println(num + " is postive");
        }
        
        return Math.pow(num, 2);
    }
    
    //public - it is access specifier means from every where we can access it
    //static - access modifier means we can call this method directly using class name without 
    public static int[] range(int start, int end){
        
        int arrLen = end - start;
        int result[] = new int[arrLen + 1];
        int stat = start;
        
        for (int i=0; i<result.length; i++){
            // a = 10
            // x = ++a x will equle to 11 and a = 11 (a increase by 1 and then x equle to a)
            // x = a++ x will equle to 10 and a = 11 (x equle to a then a increase by 1)
            // as will as --a and a--
            result[i] = stat++;
        }
        return result;
    }
    public static void main(String args[]){
        
    }
}

import java.util.Scanner;
import java.util.Arrays;

public class MyClass {
    public static void main(String args[]) {

      Star s = new Star();
      double out = s.number(55);
      System.out.println(out);

      int ran[] = Star.range(8, 22);
      System.out.println(Arrays.toString(ran));
    }
}
