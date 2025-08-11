# **Fibonacci Generator**

This is a simple Python script that allows you to generate numbers from the Fibonacci sequence. The program offers two main functionalities:

1. Get a specific number from the sequence by its index.  
2. Generate a list containing a specified number of Fibonacci numbers.

## **How to Use**

1. **Run the script:** Open your terminal or command prompt and run the following command:  
   python fibonacci\_generator.py

2. **Choose an option:** The program will prompt you with a question:¿Quieres obtener un número específico de la secuencia de Fibonacci (1) o una lista de números (2)? (Escribe 'x' para salir):  
   * Enter 1 to get a single Fibonacci number at a specific index.  
   * Enter 2 to generate a list of Fibonacci numbers up to a certain count.  
   * Enter x to exit the program.  
3. **Provide input:**  
   * If you chose 1, you will be asked for the index of the number you want to retrieve. The program will then print the corresponding Fibonacci number.  
   * If you chose 2, you will be asked for the number of Fibonacci numbers you want to generate. The program will then display the full list.  
4. **Repeat or Exit:** After displaying the result, the program will return to the main menu, allowing you to perform another action or exit the program by typing x.

## **Functions**

The script contains two main functions:

* fibonacci\_list(n: int) \-\> list: Takes an integer n as input and returns a list containing the first n numbers of the Fibonacci sequence.  
* fibonacci\_index(n: int) \-\> int: Takes an integer n as input and returns the Fibonacci number at that specific index.
