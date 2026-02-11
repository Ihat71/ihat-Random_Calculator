import java.util.Scanner;
//you can also do java.util.*

public class hello_world {
    //It's important to note that the main method MUST be void, this is a requirement
    public static void main(String[] args){
            int[] numbers = new int[5];
            //Trick: use shift + alt + F to auto format code
            int x = 5;
            x = changeNumber(x);
            System.out.println(x);

            System.out.println("Please put in 5 elements");

            //create for loop
            populateArray(numbers);
            
            //Seperator
            System.out.println("----------------------------------");

            //Step: traversing through the array
            //for (int counter = 0; counter < numbers.length; counter++){
            //System.out.println("Number " + (counter + 1) + ":" + numbers[counter]);}

            displayArray(numbers);

            //storing the value of addNumbers into a variable
            //int result = addNumbers(5, 6);
            //System.out.print(result);

        }//end of main
    //the replacing of void here is int, which means that the method needs to return an int value
    public static int addNumbers(int n1, int n2){
        int result = n1 + n2;
        return result;
    }

    //method for displaying
    public static void displayArray(int[] numbers){
        for (int counter = 0; counter<numbers.length;counter++){
            System.out.println("Number " + (counter + 1) + ":" + numbers[counter]);}
    }

    public static void populateArray(int[] numbers){
        Scanner input = new Scanner(System.in);
        for (int counter=0;counter<numbers.length;counter++){
            System.out.print("Enter number" + (counter+1) + ":");
            numbers[counter] = input.nextInt();}
        input.close();
        }
    
    //changing the variable inside a method will not change the variable put in as an argument by itself, you have to return a value and put it inside the var
    public static int changeNumber(int x){
        x = x*2;
        System.out.println("The changed number is: " + x);
        return x;
    }
}

