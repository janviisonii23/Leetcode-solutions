class Solution {
    public void swap(int[][] matrix){
        int rows = matrix.length;
        for(int i=0;i<rows/2;i++){
            int[] temp = matrix[i];
            matrix[i] = matrix[rows-1-i];
            matrix[rows-1-i] = temp;
        }
    }
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        swap(matrix);
        for(int i=0;i<n;i++){
            for(int j=i+1;j<matrix[i].length;j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }
}
