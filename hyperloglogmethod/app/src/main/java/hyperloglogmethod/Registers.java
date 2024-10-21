package hyperloglogmethod;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.concurrent.ConcurrentHashMap;

public class Registers {
    private int[] m;

    public Registers(int m){
        this.m = new int[m];
    }


    public int functionF(int x){
        int correction;
        if(m.length == 512){
            correction = 22;
        }
        else if(m.length == 1024){
            correction = 21;
        }
        else{
            correction = 20;
        }


        return ((x*0xbc164501) & 0x7fffffff) >> correction;
    }

    public void updateRegister(int n){
        int index = functionF(n);
        int hashedValue = Hash.hashMethod(n);
        int pFunctionValue = Rho.functionP(hashedValue);

        if (m[index]<pFunctionValue) {
            m[index] = pFunctionValue;
        }

    }

    public int[] getM(){
        return m;
    }
    
    // public static void main(String[] args) throws FileNotFoundException {

    //     File myFile = new File("hyperloglogmethod/app/src/main/java/hyperloglogmethod/inputRegisters.txt");
    //     Scanner mySystemScanner = new Scanner(myFile);
    //     while (mySystemScanner.hasNextLine()) {
    //         String hexLine = mySystemScanner.nextLine();
    //         int n = (int) Long.parseLong(hexLine, 16);
    //         Registers.registers(n);
    //     }

    //     for (int i : m) {
    //         System.out.println(i);
            
    //     }

    //     mySystemScanner.close();

    // }

}
