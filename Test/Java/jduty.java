public class Corona {
// 0 is normal 1 is more than normal 2 is too much
int sneeze;

// 37.5 normal body temperature
double temperature;

boolean headache;

boolean transform;

// result is between 1 and 10
// 1 - 5 not coronavires
// 6 - 7 must be check by Dr.
// 7 - 10 must be in Quarantine 100% coronavires
int result = 0;

Corona(int sneeze, double temperature, boolean headache, boolean transform)
{
this.sneeze = sneeze;
this.temperature = temperature;
this.headache = headache;
this.transform = transform;
this.result = result;
}

void coronaTest(){
_sneeze_();
_temperature_();
_headache_();
_transform_();

if (this.result <= 5) {
System.out.println("result is " + this.result + " not coronavires");
} else if (this.result >= 6 && this.result <= 7) {
System.out.println("result is " + this.result + " 50% is coronavires");
} else {
System.out.println("result is " + this.result + " 100% coronavires");
}

}

void _sneeze_(){
this.result += this.sneeze;
}

void _temperature_(){
if (this.temperature >= 38.0 && this.temperature < 39.0) {
this.result += 3;
} else if (this.temperature >= 39.0) {
this.result += 5;
}
}

void _headache_(){
if (this.headache == true) {
this.result += 1;
}
}

void _transform_(){
if (this.transform == true) {
this.result += 2;
}
}

public static void main(String args[]) {

}
}



// create another class call MyClass in MyClass.java

public class MyClass {
public static void main(String args[]) {
Corona person = new Corona(2, 39.0, true, true);
person.coronaTest();
}
}
