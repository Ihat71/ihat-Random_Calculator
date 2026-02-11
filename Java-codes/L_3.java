import java.util.Scanner;

public class L_3 {
    public static void main(String[] args){
        //Random value
        int condition = 5;
        int array_condition;
        int[] arr = {1,2,3,4,5,6,7,8,9,10};
        //This loop will break once a index which is inside the boundary is inputed
        while (condition == 5){
        array_condition = search(arr);
        if (array_condition == 1){
            condition = 1;
        }
    }

    }
    // This method searches the array, asks for the index and checks if the index inputed is in the boundary. If it is, it shows the value and then returns 1.
    // This returned value is used to break the while loop
    public static int search(int[] a){
        Scanner sc = new Scanner(System.in);
        show_array(a);
        System.out.println("Enter the index you want, it has to be between 0 and " + (a.length - 1));
        int x = sc.nextInt();
        if (x <= a.length -1 && x >= 0){
        System.out.println("Here it is: " + a[x]);
        return 1;
        }
        else{
            System.out.println("Index Error");
            return 0;
        }
    }

    //This method only shows the array
    public static void show_array(int[] x){
        int y;
        for (int i=0; i<x.length;i++){
            y = x[i];

            if (i < x.length - 1){
                System.out.print(y + ", ");
            }
            else{
                System.out.println(y);
            }
        }
    }
}