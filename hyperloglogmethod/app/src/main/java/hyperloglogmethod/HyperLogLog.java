package hyperloglogmethod;

import java.util.concurrent.ConcurrentHashMap;

import java.io.FileNotFoundException;
import java.util.Scanner;

public class HyperLogLog {

    private Registers registers;
    private int[] stream;
    private final int m;
    private final double alphaM;

    public HyperLogLog(int[] stream, int msize){
        this.m = msize;
        this.alphaM = 0.7213 / (1.0 + 1.079 / m);

        registers = new Registers(m);
        this.stream = stream;

    }

    public void processStream(){
        for (int i = 0 ; i<stream.length ; i++) {
            int n = stream[i];
            registers.updateRegister(n);  
        }

    }

    public double estimateCardinality(){
        double harmonicSum = 0.0;

        int[] M = registers.getM();


        for (int j = 0; j < M.length; j++) {

            harmonicSum += Math.pow(2, -M[j]);
            
        }
        
        double rawEstimate = alphaM*m*m*(Math.pow(harmonicSum, (-1.0)));

        // count empty registers
        int V = 0;
        for (int i : M) {
            if(i==0){
                V++;
            }
        }


        if (((5.0/2.0)*m) >= rawEstimate && V > 0 ) {
            return m*Math.log((double) m/V);
        }

        else if(rawEstimate > (1.0/30.0)*Math.pow(2.0, 32.0)){
            rawEstimate = -Math.pow(2.0, 32.0) * Math.log(1.0- (rawEstimate/(Math.pow(2.0, 32.0))));
        }
        
        
        return rawEstimate;
    }
    
    public static void main(String[] args) throws FileNotFoundException {
        
        if("HyperLogLogQualityTest".equals(args[0])){

            // Hashing and p functions test
            Hash hashing = new Hash();

            hashing.computeHashing();
            ConcurrentHashMap<Integer,Integer> map = hashing.getMap();
            for (Integer number : map.keySet()) {
                System.out.println(number + " " + map.get(number));
                }
            
        }
            

        if("hyperLogLogMillion".equals(args[0])){

            // Make test for both the inputStream & 1.000.000 - 2000.000


            // ***********
            // make the stream in the array below instead of the new int[] and initialize Hash
            int[] inputStream = new int[1000000];
            Hash hashing = new Hash();
            // ***********

            // Initialize registers
            HyperLogLog hyperLogLog = new HyperLogLog(inputStream,1000000);

            // update and process the register
            hyperLogLog.processStream();
            
            // estimate cardinality
            double n = hyperLogLog.estimateCardinality();
            System.out.println(n);

        }

        if("HyperLogLog512".equals(args[0])){
            Scanner myScanner = new Scanner(System.in);

            int amount = Integer.parseInt(myScanner.nextLine());
            int[] numbers = new int[amount];

            for (int i = 0; i < amount; i++) {
                numbers[i] = myScanner.nextInt();
                // myScanner.nextLine();
            }

            Hash hashingInit = new Hash();
            HyperLogLog hyperLogLog = new HyperLogLog(numbers,512);

            // update an process the register
            hyperLogLog.processStream();

            // estimate cardinality
            double output = hyperLogLog.estimateCardinality();

            System.out.println(output);

            myScanner.close();


        }

        if("HyperLogLog1024".equals(args[0])){
            Scanner myScanner = new Scanner(System.in);

            int amount = Integer.parseInt(myScanner.nextLine());
            int[] numbers = new int[amount];

            for (int i = 0; i < amount; i++) {
                numbers[i] = myScanner.nextInt();
                // myScanner.nextLine();
            }

            Hash hashingInit = new Hash();
            HyperLogLog hyperLogLog = new HyperLogLog(numbers,1024);

            // update an process the register
            hyperLogLog.processStream();

            // estimate cardinality
            double output = hyperLogLog.estimateCardinality();

            System.out.println(output);

            myScanner.close();


        }

        if("HyperLogLog2048".equals(args[0])){
            Scanner myScanner = new Scanner(System.in);

            int amount = Integer.parseInt(myScanner.nextLine());
            int[] numbers = new int[amount];

            for (int i = 0; i < amount; i++) {
                numbers[i] = myScanner.nextInt();
                // myScanner.nextLine();
            }

            Hash hashingInit = new Hash();
            HyperLogLog hyperLogLog = new HyperLogLog(numbers,2048);

            // update an process the register
            hyperLogLog.processStream();

            // estimate cardinality
            double output = hyperLogLog.estimateCardinality();

            System.out.println(output);

            myScanner.close();


        }
        
    }
}
