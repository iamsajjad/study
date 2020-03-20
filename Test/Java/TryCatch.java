class TryCatch{
   public static void main(String args[]){
     try{
         int a[]=new int[7];
         a[4]=30/0;
         System.out.println("First print statement in try block");
     }
     catch(ArithmeticException e){
        System.out.println("Warning: ArithmeticException");
     }
     catch(ArrayIndexOutOfBoundsException e){
        System.out.println("Warning: ArrayIndexOutOfBoundsException");
     }
     catch(Exception e){
        System.out.println("Warning: Some Other exception");
     }
     /* Finally block will always execute
       * even if there is no exception in try block
       */
    finally{
	    System.out.println("This is finally block");
    }  
    System.out.println("Out of try-catch-finally");
  }
}
