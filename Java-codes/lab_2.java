import java.util.Scanner;
public class lab_2 {
    static Scanner sc = new Scanner(System.in);
    static String[] list = new String[10];
    static int validyearly = 1;
    static int validmonthly = 1;

    public static void main(String[] args) {
        char choice = 'y';
        while (choice == 'y'){
        int year_count = 0;
        int month_count = 5;
        //String[] list = new String[10];
        System.out.println("Hello! do you want to join the book club? (y/n)");
        choice = sc.next().charAt(0);
        if (choice == 'n'){
            System.out.println("Good bye");
            break;
        }
        else if (choice == 'y'){
        }
        else{
            System.out.println("That is not a choice!");
            break;
        }
        System.out.println("What is your name?");
        sc.nextLine();
        String name = sc.nextLine();
        System.out.println("Do you want a year or monthly membership? (y/m)");
        char sub = sc.next().charAt(0);

        if (sub == 'y'){
            insertAtSpecificPos(list, name, year_count, validyearly, sub);
            year_count++;
            validyearly++;
        }
        else if (sub == 'm'){
            insertAtSpecificPos(list, name, month_count, validmonthly, sub);
            month_count++;
            validmonthly++;
        }
        else{
            System.out.println("That is not a choice!");
            break;
        }
        displayArray(list, 10);
        // System.out.println(Arrays.toString(list));
    }


    }

    public static void displayArray(String[] letters, int validSize) {

        for (int count = 0; count < validSize; count++) {
            System.out.println("User " + (count + 1) + ": " + letters[count]);
        }
    }
    public static void insertAtSpecificPos(String[] names, String newChar, int index, int validSize, char sub) {
        if (names[4] != null && names[9] != null) {
            System.out.println("The book club seems to be full!");
        } 
        // else if ((names[4] != null )||(names[9] != null)){
        //     if (names[4] != null){
        //         System.out.println("Yearly subscriptions are unavailable at this moment");
        //     }
        //     else if (names[9] != null){
        //         System.out.println("Monthly subscriptions are unavailable at this moment");
        //     }
        //}
        else{
            if (sub == 'm'){
                validSize = validSize + 5;
                if (names[9] != null){
                System.out.println("Monthly subscriptions are unavailable at this moment");
                return;
                }

            }else if (sub == 'y'){
                if (names[4] != null){
                System.out.println("Yearly subscriptions are unavailable at this moment");
                return;
                }
                
            }
            // loop for shifting the elements
            for (int count = validSize - 1; count >= index; count--) {
                if (validSize == 10){
                    names[(names.length - 1)] = names[count];
                    continue;
                }
                names[count + 1] = names[count];
            }
            names[index] = newChar;
            validSize++;
        }
    }
}
