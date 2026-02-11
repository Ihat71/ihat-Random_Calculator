import java.util.Arrays;
import java.util.Scanner;
public class insert_at_end {
    static Scanner sc = new Scanner(System.in);
    static int validSize;

    public static void main(String[] args){
        int[] arr = new int[10];
        System.out.print("Enter valid size: ");
        validSize = sc.nextInt();

        System.out.println("--------------------" + "\n" + "Populate it:");
        populateArray(arr, validSize);

        validSize = insertAtEnd(arr, validSize);

        System.out.println(Arrays.toString(arr) + " || valid size: " + validSize);


    }
    public static void populateArray(int[] letters, int validSize) {
        for (int count = 0; count < validSize; count++) {
            System.out.print("Number " + (count + 1) + ": ");
            letters[count] = sc.nextInt();
        }
        //number = 20;

    }
    public static int insertAtEnd(int[] nmbers, int validSize) {
        if (validSize == nmbers.length){
            System.out.println("Array is full");
        }
        else{
        int newInt;
        System.out.print("Insert at end: ");
        newInt = sc.nextInt();
        nmbers[validSize] = newInt;
        validSize++;
        }
        //number = 5;

        return validSize;
    }
}