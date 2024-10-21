// package hyperloglogmethod;


// import java.util.concurrent.ConcurrentHashMap;
// import java.io.FileNotFoundException;
// import java.util.Scanner;
// import java.util.stream.*;
// import java.io.File;
// import java.util.ArrayList;



// public class Threshold {
//     private Registers registers;
//     private int[] stream;
//     private final int m = 1024;
//     private final double alphaM = 0.7213 / (1.0 + 1.079 / m);

//     public Threshold(int[] stream){

//         registers = new Registers(m);
//         this.stream = stream;

//     }

//     public void processStream(){
//         for (int i = 0 ; i<stream.length ; i++) {
//             int n = stream[i];
//             registers.updateRegister(n);  
//         }

//     }

//     public double estimateCardinality(){
//         double harmonicSum = 0.0;

//         int[] M = registers.getM();


//         for (int j = 0; j < M.length; j++) {

//             harmonicSum += Math.pow(2, -M[j]);
            
//         }
        
//         double rawEstimate = alphaM*m*m*(Math.pow(harmonicSum, (-1.0)));

//         // count empty registers
//         int V = 0;
//         for (int i : M) {
//             if(i==0){
//                 V++;
//             }
//         }


//         if (((5.0/2.0)*m) >= rawEstimate && V > 0 ) {
//             return m*Math.log((double) m/V);
//         }

//         else if(rawEstimate > (1.0/30.0)*Math.pow(2.0, 32.0)){
//             rawEstimate = -Math.pow(2.0, 32.0) * Math.log(1.0- (rawEstimate/(Math.pow(2.0, 32.0))));
//         }
        
        
//         return rawEstimate;
        

//     }
    
//     public static void main(String[] args) throws FileNotFoundException {


//         // int[] million = IntStream.rangeClosed(1, 1000000).toArray();
      
        
//         Scanner myScanner = new Scanner(System.in);
//         ArrayList<Integer> liste = new ArrayList<>();

//         int firstNumber = myScanner.nextInt();
//         myScanner.nextLine();

//         while (myScanner.hasNextLine()){
//             liste.add(Integer.parseInt(myScanner.nextLine().strip()));
//         }
        
//         int size = liste.size();
//         int[] intList = new int[size];
//         for (int i = 0; i < intList.length; i++) {
//             intList[i] = liste.get(i);
//         }

//         Hash hashing = new Hash();

//         Threshold T = new Threshold(intList);

        
//         T.processStream();
//         double cardinalityEstimate = T.estimateCardinality();
//         // System.out.println(cardinalityEstimate);

//         if (cardinalityEstimate>=firstNumber) {
//             System.out.println("above");
            
//         } else {
//             System.out.println("below");
            
//         }
        
//         myScanner.close();
        
//     }
// }

// class Registers {
//     private int[] m;

//     public Registers(int m){
//         this.m = new int[m];
//     }


//     public int functionF(int x){
//         return ((x*0xbc164501) & 0x7fffffff) >> 21;
//     }

//     public void updateRegister(int n){
//         int index = functionF(n);
//         int hashedValue = Hash.hashMethod(n);
//         int pFunctionValue = Rho.functionP(hashedValue);

//         if (m[index]<pFunctionValue) {
//             m[index] = pFunctionValue;
//         }

//     }

//     public int[] getM(){
//         return m;
//     }

// }


// class Hash{

//     private static int[] bits;
//     private static ConcurrentHashMap<Integer,Integer> map;

//     public Hash() throws FileNotFoundException{

//         // File appendix = new File("Appendix1.txt");

//         // Scanner myScanner = new Scanner(appendix);

//         this.bits = new int[32];
//         String[] lines = "0x21ae4036, 0x32435171, 0xac3338cf, 0xea97b40c, 0x0e504b22, 0x9ff9a4ef, 0x111d014d, 0x934f3787, 0x6cd079bf, 0x69db5c31, 0xdf3c28ed, 0x40daf2ad, 0x82a5891c, 0x4659c7b0, 0x73dc0ca8, 0xdad3aca2, 0x00c74c7e, 0x9a2521e2, 0xf38eb6aa, 0x64711ab6, 0x5823150a, 0xd13a3a9a, 0x30a5aa04, 0x0fb9a1da, 0xef785119, 0xc9f0b067, 0x1e7dde42, 0xdda4a7b2, 0x1a1c2640, 0x297c0633, 0x744edb48, 0x19adce93".split(", ");

//         int counter = 0;
//         for (String string : lines) {
//             String hexString = string;

//         // Convert the last 8 hex characters to an unsigned 32-bit integer
//             String lastEightHexDigits = hexString.substring(hexString.length() - 8);
            
//             int decimalValue = Integer.parseUnsignedInt(lastEightHexDigits, 16);
//             bits[counter] = decimalValue;
//             counter++;
            
//         }
//         // myScanner.close();

//     }

//     public static int hashMethod(int k){
//         int finalNumber = 0;
//         // int number = k;

//         for (int i = 0; i < bits.length; i++) {
//             int aNumber = bits[i];
//             int bitnumber = aNumber & k;
//             // System.out.println(bitnumber);
            
//             int leastSignificantBit = Integer.bitCount(bitnumber)&1;

//             finalNumber |= (leastSignificantBit << i);

//             // System.out.println(finalNumber);

//         }
//         return finalNumber;
//         // return String.format("%08x", finalNumber);

//     }

//     public void computeHashing(){
//         Thread[] threads = new Thread[4];
//         int arraySize = 1000000; // total siz
//         int chunkSize = arraySize / 4; // size of each chunk
//         map = new ConcurrentHashMap<>();

//         for (int i = 0; i < threads.length; i++) {
//             final int start = i * chunkSize + 1; // start index for this thread
//             final int end = (i + 1) * chunkSize; // end index for this thread

    
//             threads[i] = new Thread(() -> {
//                 for (int j = start; j < end; j++) {
//                     int number = Rho.functionP(hashMethod(j));
//                     map.merge(number, 1, Integer::sum); // Increment atomically
//                 }
//                 // System.out.println("Thread completed for range: " + start + " to " + end);
//             });
//         }

//         for (Thread thread : threads) {
//             thread.start();
//         }
//         for (Thread thread2 : threads) {
//             try {
//                 thread2.join();
//             } catch (Exception e) {
//                 // TODO: handle exception
//                 System.out.println("unusccessfull join");
//             }   
//         }
//     }

//     public ConcurrentHashMap<Integer,Integer> getMap(){
//         // Not atomic, so dont call until all threads have joined
//         return map;
//     }


// }

// class Rho {
    
//     public static int functionP(int input){
//         int counter = 1;

//         for (int i = 31; i >= 0; i--) {
            
//             if ((input&(1<<i)) != 0) {
//                 break;
//             } else {
//                 counter++;
//             }
//         }
//         return counter;
//     }


// }