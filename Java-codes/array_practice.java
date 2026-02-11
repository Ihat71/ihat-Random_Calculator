import java.util.Arrays;
import java.util.Scanner;

public class array_practice {
    public static void main(String[] args){
        int[] arr = {1,2,3,4,0,0,0,0,0,0};
        Scanner sc = new Scanner(System.in);
        System.out.println("How many values do you want to enter? ");
        int values = sc.nextInt();
        int condition = 0;
        int counter = 0;
        while (condition == 0){
        System.out.println("Insert a value into the array: ");
        int x = sc.nextInt();
        for (int i = arr.length-1; i>=0;i--){
            if (i == arr.length-1){
                continue;
            }
            else{
                arr[i+1] = arr[i];
            }
        }
        arr[0] = x;
        counter++;
        if (counter == values){
            condition = 1;
        }
        }
        System.out.println(Arrays.toString(arr));

    }
    public static void InserAtBeginning(int[] numbers, int validSize, int number){
        //Put the algorithm in here
    }

}
    

