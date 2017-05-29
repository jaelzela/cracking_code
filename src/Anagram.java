import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Anagram {

	public static int NUMBER_LETTERS = 26;
	
	public static int numberNeeded(String first, String seccond) {
		int[] charCount1 = getCharCounts(first);
		int[] charCount2 = getCharCounts(seccond);
		return getDelta(charCount1, charCount2);
	}
	
	private static int getDelta(int[] charCount1, int[] charCount2) {
		int delta = 0;
		for (int i = 0; i < NUMBER_LETTERS; i++) {
			delta += Math.abs(charCount1[i] - charCount2[i]); 
		}
		return delta;
	}

	private static int[] getCharCounts(String s) {
		int[] counts = new int[NUMBER_LETTERS];
		
		for(int i=0; i<s.length(); i++) {
			String c = String.valueOf(s.charAt(i));
			int idx = "abcdefghijklmnopqrstuvwxyz".indexOf(c);
			counts[idx] += 1;
		}
		return counts;
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String first = br.readLine();
		String second = br.readLine();
		System.out.println(numberNeeded(first, second));
	}

}
