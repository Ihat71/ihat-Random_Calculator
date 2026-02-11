import java.util.Stack;

public class stack {
    public static void main(String[] args){
        Stack<Integer> st1 = new Stack<>(); // the <> are angle brackets, in this case it accepts integer values
        st1.push(15);
        System.out.println(st1);
        //System.out.println("Current size is " + st1.size());
        st1.push(25);
        st1.push(35);
        System.out.println("Current size is " + st1.size());
        System.out.println("The item at the top is: " + st1.peek());

        System.out.println("The popped element is: " + st1.pop());
        System.out.println("The stack is: " + st1 + " --- And the size is: " + st1.size());

        if(st1.search(100)==-1){
            System.out.println("Not found!");
        }
        else{
            System.out.println("Found!");
        }
        if (st1.isEmpty()) {
            System.out.println("The stack is empty.");
        } else {
            System.out.println("The stack is not empty.");
        }
    }
}
