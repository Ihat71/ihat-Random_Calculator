import java.util.Arrays;
import java.util.Scanner;
//s1-> start
public class proj_1 {
    static Scanner input = new Scanner(System.in);
    static int number = 0;
    static char answer = 'y';
// I promise I did not use chatgpt or even google!

    public static void main(String[] args) {

        
        // s2 --> declare an array but make sure you keep some extra slots
        int size_arr;
        System.out.println("What is the size of the array you want? ");
        size_arr = input.nextInt();
        int[] numeros = new int[size_arr];
        numeros[numeros.length-1] = 900;
        // s3 --> create a variable to hold the user choice of total valid array
        // elements
        // s4--> prompt user to enter the total number of characters they want
        System.out.print("Populate your array: ");
        try {
            // s5--> fill the array with elements until valid size
        populateArray(numeros);

        System.out.println("----------------------------");
        displayArray(numeros);
        // s6 --> prompt user to enter the new value to insert at beginning
        while (number == 0){
        System.out.print("Enter a new integer, make sure to populate the array in either ascending or descending order: ");
        //validSize = insertAtBeginning(numeros, validSize, newElement);
        System.out.println("----------------------------");
        //System.out.println("Number is: " + number);
        displayArray(numeros);
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
            if (numeros[numeros.length-1] == 900){
            System.out.println("Alright");
            }
            else{
                System.out.println("Array is full");
                System.out.println("Final array: " + Arrays.toString(numeros));
                break;
            }
        }
        else if (answer == 'n'){
            System.out.println("Good bye!");
            break;

        }
        

    }
    } catch (Exception e) {
            System.out.println("Error ");
        } 
        int search_value;
        int low = 0;
        int high = (numeros.length-1);
        int mid = mid_getter(low, high);
        int count = 0;
        System.out.println("Search for an integer: ");
        search_value = input.nextInt();
        //While loop to iteratively make the boundaries smaller. This loop is if the array is ascending order
        while (low <= high){
            if ((numeros[low] == search_value)||(numeros[high] == search_value)){
                if (low == search_value){
                System.out.println("The number is at index: " + low);
                }
                else{
                    System.out.println("The number is at index: " + high);
                }
                System.out.println("It took " + count + " tries to find");
                break;
            }
            //This conditional is a secondary base case. As the boundary gets smaller, we get closer to the value and eventually hit this base case.
            else if (numeros[mid] == search_value){
                System.out.println("The number is at index: " + mid);
                System.out.println("It took " + count + " tries to find");
                break;
            }
            //If the value at index mid is smaller than the search value, we make the boundary smaller rightwards
            else if (numeros[mid] < search_value){
                low = mid + 1;
                mid = mid_getter(low, high);
            }
            //Same idea but leftwards
            else if (numeros[mid] > search_value){
                high = mid - 1;
                mid = mid_getter(low, high);
            }
        
        count++;
        }



    } // end of main

    public static void populateArray(int[] numeros) {

        for (int count = 0; count < numeros.length; count++) {
            numeros[count] = input.nextInt();
        }

    }

    public static void displayArray(int[] letters) {

        for (int count = 0; count < letters.length-1; count++) {
            System.out.println("Character " + (count + 1) + ": " + letters[count]);
        }

    }

    // public static int insertAtBeginning(int[] numeros, int validSize, int newElement) {
    //     for (int count = validSize - 1; count >= 0; count--) {
    //         // shifting and copying happens here
    //         numeros[count + 1] = numeros[count];
    //     }
    //     numeros[0] = newElement;
    //     validSize++;

    //     return validSize;
    // }
    public static int mid_getter(int low, int high){
        int mid = (low + high)/2;
        return mid;

    }
}

// could not finish