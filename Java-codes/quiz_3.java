import java.util.Arrays;
import java.util.Scanner;
public class quiz_3{
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args){
    System.out.println("Enter array length (minimum of 15-20)");
    int size = sc.nextInt();
    int[] values = new int[size];
    System.out.println("Do you pick Ascending (a/A) or Descending (d/D)");
    char answer = sc.next().charAt(0);
    int count = 0;
    while(values[values.length - 1] == 0){
        System.out.println("Enter value " + (count + 1));
        int inputs = sc.nextInt();
        if (inputs < 0 || inputs > 35){
            System.out.println("Invalid input");
            continue;
        }
        else{
            values[count] = inputs;
        }
        count++;
    }
    System.out.println("Array before sorting:" + Arrays.toString(values));

    bubbleSort(values, answer);

    System.out.println("Array after sorting" + Arrays.toString(values));
    }
    public static void bubbleSort(int[] charArray, char choice) {
        boolean swapped;
        if (choice == 'A' || choice == 'a'){
        for (int out = 0; out < charArray.length - 1; out++) {
            swapped = false;
            System.out.println("Outer value: " + out);

            for (int in = 0; in < charArray.length - 1 - out; in++) {
                System.out.println("inner is: " + in);
                if (charArray[in] > charArray[in + 1]) {
                    System.out.println(charArray[in] + "> " + charArray[in + 1]);

                    swap(charArray, in, in + 1);
                    swapped = true;
                }

            } // end of inner loop
            if (swapped == false)
                break;
        }

        } // end of outer loop
        else if (choice == 'd' || choice == 'D'){
            for (int out = 0; out < charArray.length - 1; out++) {
                swapped = false;
                System.out.println("Outer value: " + out);
    
                for (int in = 0; in < charArray.length - 1 - out; in++) {
                    System.out.println("inner is: " + in);
                    if (charArray[in] < charArray[in + 1]) {
                        System.out.println(charArray[in] + "< " + charArray[in + 1]);
    
                        swap(charArray, in + 1, in);
                        swapped = true;
                    }
    
                } // end of inner loop
                if (swapped == false)
                    break;
            }
        }
    }
    public static void swap(int[] charArray, int in1, int in2) {

        int temp = charArray[in1];
        charArray[in1] = charArray[in2];
        charArray[in2] = temp;

    }
}
    
