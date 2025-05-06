package org.example;

public class App {

    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) {
        App app = new App();
        System.out.println(app.getGreeting());

        Calculator calculator = new Calculator();

        int sum = calculator.add(10, 5);
        int product = calculator.multiply(10, 5);

        System.out.println("Sum: " + sum);
        System.out.println("Product: " + product);
    }
}


