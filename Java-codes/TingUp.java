import java.util.Arrays;

public class TingUp {
    public static void main(String[] args){
    int[] arr = {9,59,3,7,2,889,23,7865,1};
    //bubble(arr);
    //insertion(arr);
    //selection(arr);
    //betterBubble(arr);
    System.out.println("----------------------------------------------");
    System.out.println("Final array is: " + Arrays.toString(arr));
    }
    public static void selection(int[] arr){
        //Selection Sort finds the smallest (or largest) element in each pass and places it in its correct position.
        // Steps:
        // Find the smallest element in the array.
        // Swap it with the first unsorted element.
        // Move to the next unsorted position and repeat.
        int min, in, out;
        for (out = 0; out < arr.length; out++){
            min = out;
            for (in = out; in < arr.length; in++){
                if (arr[in] < arr[min]){
                    min = in;
                }
            }
            swap(arr, out, min);
                
        }
    }
    public static void insertion(int[] arr){
        int temp;
        int in, out;
        for (out = 1; out<arr.length; out++){
            System.out.println("Pass: " + out);
            System.out.println(Arrays.toString(arr));
            System.out.println("----------------------------------------------");
            if (arr[out] > arr[out-1]){
                continue;
            }
            temp = arr[out];
            arr[out] = arr[out-1];
            for (in = out; in > 0 &&arr[in-1]>temp; in--){
                System.out.println("We are replacing " + arr[in] + " With " + arr[in-1]);
                arr[in] = arr[in-1];
                System.out.println(Arrays.toString(arr));
                System.out.println("----------------------------------------------");
                
            }
            System.out.println("----------------------------------------------");
            System.out.println("And finally the temp goes where it belongs: ");
            arr[in] = temp;
            System.out.println(Arrays.toString(arr));
            System.out.println("++++++++++++++++++++++++++++++++++++++++++++++");

        }
    }
    public static void bubble(int[] arr){
        //bubble sort repeatedly compares adkacent elements in an array ans swaps them if they are in the wrong order
        for (int out = 0; out<arr.length - 1; out++){
            System.out.println("Outer: " + out);
            for (int in = 0; in < arr.length - 1 - out; in++){
                System.out.println("Inner: " + in);
                if (arr[in] > arr[in+1]){
                    swap(arr, in, in+1);
                }

            }
        }
    }
    public static void betterBubble(int[] arr){
        boolean swapped;
        for (int i = 0; i<arr.length-1;i++){
            swapped = false;
            for (int j = 0; j<arr.length - 1 - i;j++){
                if (arr[j] > arr[j+1]){
                    swap(arr, arr[j], arr[j+1]);
                    swapped = true;
                
                }
            }
            if (swapped == false){
                break;
            }            
        }
    }
    public static void swap(int[] arr, int swap_1, int swap_2){
        int temp = arr[swap_2];
        arr[swap_2] = arr[swap_1];
        arr[swap_1] = temp;
    }
}

