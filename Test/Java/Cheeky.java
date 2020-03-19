

import java.util.Calendar;
public class Cheeky {

    String name;
    int age, cakeday;
    double height;

    Cheeky(String name, int age, double height) {
        this.name = name;
        this.age = age;
        this.height = height;
        this.cakeday = Calendar.getInstance().get(Calendar.YEAR) - this.age;
    }

    double avaMarks(double[] marks){

        double sum = 0.0;
        for (int i = 0; i<marks.length;i++){
            sum += marks[i];
        }
        double ava = sum / marks.length;
        return ava;
    }

    public static void main(String args[]) {

    }
}

public class MyClass {
    public static void main(String args[]) {
        Cheeky boi = new Cheeky("sajjad", 21, 178.0);
        System.out.println(boi.name);
        System.out.println(boi.age);
        System.out.println(boi.height);
        System.out.println(boi.cakeday);

        double marks[] = {77.0, 88.0, 99.0, 30.0};
        System.out.println(boi.avaMarks(marks));
    }
}
