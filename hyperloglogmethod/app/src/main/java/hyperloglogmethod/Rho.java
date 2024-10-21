package hyperloglogmethod;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Rho {
    
    public static int functionP(int input){
        int counter = 1;

        for (int i = 31; i >= 0; i--) {
            
            if ((input&(1<<i)) != 0) {
                break;
            } else {
                counter++;
            }
        }
        return counter;
    }

    // public static void main(String[] args) throws FileNotFoundException {
    //     File myFile = new File("hyperloglogmethod/app/src/main/java/hyperloglogmethod/FunctionInputTest.txt");
    //     // Scanner myScanner = new Scanner(System.in);
    //     Scanner myScanner = new Scanner(myFile);

    //     while (myScanner.hasNextLine()) {
    //         String hexString = myScanner.nextLine();

    //         // String lastEightHexDigits = hexString.substring(hexString.length() - 8);
            
    //         int decimalValue = Integer.parseUnsignedInt(hexString, 16);
    //         System.out.println(Rho.functionP(decimalValue));
            
    //     }   
    //     myScanner.close();
    // }

}
