import java.util.Arrays;
import java.util.Scanner;
//s1-> start
public class App_2 {
    static Scanner input = new Scanner(System.in);
    static int number = 0;
    static char answer = 'y';
    static int validSize;
// I promise I did not use chatgpt or even google!

    public static void main(String[] args) {

        // s2 --> declare an array but make sure you keep some extra slots
        char[] letters = new char[10];
        letters[letters.length-1] = '-';
        // s3 --> create a variable to hold the user choice of total valid array
        // elements
        // s4--> prompt user to enter the total number of characters they want
        System.out.print("Enter the total number of characters: ");
        try {
            validSize = input.nextInt();
            // s5--> fill the array with elements until valid size
        populateArray(letters, validSize);
        //System.out.println("Number is: " + number);

        System.out.println("----------------------------");
        displayArray(letters, validSize);
        // s6 --> prompt user to enter the new value to insert at beginning
        char newElement;
        while (number == 0){
        System.out.print("Enter a new character: ");
        newElement = input.next().charAt(0);
        validSize = insertAtBeginning(letters, validSize, newElement);
        System.out.println("----------------------------");
        //System.out.println("Number is: " + number);
        displayArray(letters, validSize);
        System.out.println("Do you want to proceed? (y/n): ");
        while (true){
        answer = input.next().charAt(0);
        if (answer == 'y' || answer == 'n'){
            break;
        }
        else{
            System.out.println("Sorry, please try again. Pick either 'y' or 'n': ");
        }
    }
        if (answer == 'y'){
            if (letters[letters.length-1] == '-'){
            System.out.println("Alright");
            }
            else{
                System.out.println("Array is full");
                System.out.print("Final array: " + Arrays.toString(letters));
                break;
            }
        }
        else if (answer == 'n'){
            System.out.println("Good bye!");
            break;

        }
        
        //System.out.println("Val");

        //number = 10;
        //System.out.println("Number is: " + number);
    }
    } catch (Exception e) {
            System.out.println("Error ");
        } 
    } // end of main

    public static void populateArray(char[] letters, int validSize) {

        for (int count = 0; count < validSize; count++) {
            letters[count] = input.next().charAt(0);
        }
        //number = 20;

    }

    public static void displayArray(char[] letters, int validSize) {

        for (int count = 0; count < validSize; count++) {
            System.out.println("Character " + (count + 1) + ": " + letters[count]);
        }

    }

    public static int insertAtBeginning(char[] numbers, int validSize, char newElement) {
        for (int count = validSize - 1; count >= 0; count--) {
            // shifting and copying happens here
            numbers[count + 1] = numbers[count];
        }
        numbers[0] = newElement;
        validSize++;

        //number = 5;

        return validSize;
    }
}

