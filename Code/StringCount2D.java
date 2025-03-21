package Progarm12;
	class StringCount2D {
	    static int[] rowDir = {-1, -1, -1, 0, 0, 1, 1, 1}; // Row directions
	    static int[] colDir = {-1, 0, 1, -1, 1, -1, 0, 1}; // Column directions

	    // Function to search for the given word in all 8 directions
	    static int search2D(char[][] grid, int row, int col, String word) {
	        int R = grid.length;
	        int C = grid[0].length;
	        int wordLen = word.length();

	        // Check all 8 directions
	        int count = 0;
	        for (int dir = 0; dir < 8; dir++) {
	            int k, rd = row, cd = col;

	            // Move in the chosen direction and match characters
	            for (k = 0; k < wordLen; k++) {
	                if (rd < 0 || rd >= R || cd < 0 || cd >= C || grid[rd][cd] != word.charAt(k)) {
	                    break;
	                }
	                rd += rowDir[dir];
	                cd += colDir[dir];
	            }

	            // If full word was found
	            if (k == wordLen) {
	                count++;
	            }
	        }
	        return count;
	    }

	    // Function to count total occurrences of the word in the grid
	    static int countStringOccurrences(char[][] grid, String word) {
	        int total = 0;
	        for (int i = 0; i < grid.length; i++) {
	            for (int j = 0; j < grid[0].length; j++) {
	                total += search2D(grid, i, j, word);
	            }
	        }
	        return total;
	    }

	    public static void main(String[] args) {
	        char[][] grid = {
	            {'C', 'A', 'T'},
	            {'A', 'T', 'A'},
	            {'T', 'A', 'C'}
	        };
	        String word = "CAT";
	        
	        System.out.println("Occurrences of '" + word + "' in grid: " + countStringOccurrences(grid, word));
	    }
	}


