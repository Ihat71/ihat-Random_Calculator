package obj_orient;
public class oop_1{
public static void main(String[] args){
    class Circle{
        private double radius;
        void setRadius(double r){
            radius = r;
        }
    }
    Circle circ = new Circle();
    circ.setRadius(6.7);
}
}