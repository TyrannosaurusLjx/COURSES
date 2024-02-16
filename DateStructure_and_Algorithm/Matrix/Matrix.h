#include <iostream>  
#include <vector>  
  
/**  
 * @brief Represents a matrix and provides various matrix operations.  
 */  
class Matrix  
{  
    private:  
        int rows; /**< Number of rows in the matrix */  
        int cols; /**< Number of columns in the matrix */  
        std::vector<std::vector<int>> data; /**< 2D vector to store the matrix elements */  
  
    public:  
        /**  
         * @brief Constructs a new Matrix object.  
         *   
         * @param numRows Number of rows in the matrix.  
         * @param numCols Number of columns in the matrix.  
         * @param values Initial values for the matrix elements.  
         */  
        Matrix(int numRows, int numCols, const std::vector<std::vector<int>>& values);  
  
        /**  
         * @brief Destroys the Matrix object.  
         */  
        ~Matrix();  
  
        /**  
         * @brief Performs matrix addition with another matrix.  
         *   
         * @param other The matrix to add.  
         * @return The result of matrix addition.  
         */  
        Matrix Add(const Matrix& other) const;  
  
        /**  
         * @brief Performs matrix left multiplication with another matrix.  
         *   
         * @param other The matrix to multiply with.  
         * @return The result of matrix left multiplication.  
         */  
        Matrix leftMul(const Matrix& other) const;  
  
        /**  
         * @brief Performs matrix right multiplication with another matrix.  
         *   
         * @param other The matrix to multiply with.  
         * @return The result of matrix right multiplication.  
         */  
        Matrix rightMul(const Matrix& other) const;  
  
        /**  
         * @brief Performs scalar multiplication with the matrix.  
         *   
         * @param k The scalar value to multiply with.  
         * @return The result of scalar multiplication.  
         */  
        Matrix kMul(int k) const;  

        /**  
         * @brief Returns the inverse of the matrix.  
         *   
         * @return The inverse of the matrix.  
         */  
        Matrix inverse() const;  
        
        /**  
         * @brief Multiplies the matrix with a vector.  
         *   
         * @param vector The vector to be multiplied with the matrix.  
         * @return The resulting vector after multiplication.  
         */  
        std::vector<double> mulVector(std::vector<double>& vector) const;  
        
        /**  
         * @brief Gets the eigenvalues of the matrix.  
         *   
         * @return The eigenvalues of the matrix.  
         */  
        std::vector<double> getEigenvalues() const;  

        /**  
         * @brief Prints the matrix.  
         */  
        void Print();  
  
        /**  
         * @brief Sets the value of an element in the matrix.  
         *   
         * @param row The row index of the element.  
         * @param col The column index of the element.  
         * @param item The value to set.  
         */  
        void setElement(int row, int col, int item);  
  
        /**  
         * @brief Prints the value of an element in the matrix.  
         *   
         * @param row The row index of the element.  
         * @param col The column index of the element.  
         */  
        void printElement(int row, int col) const;  
};  


Matrix::Matrix(int numRows, int numCols, const std::vector<std::vector<int>>& values)
{
    rows = numRows;
    cols = numCols;
    if(!values.empty()){
        data = values;
    }else{
        std::vector<std::vector<int>> matrix(numRows, std::vector<int>(numCols,0));
        data = matrix;
    }
}

Matrix::~Matrix()
{
}

Matrix Matrix::Add(const Matrix& other) const{

    if(rows != other.rows || cols != other.rows){
        std::cout<<"dim error! "<<std::endl;
        return Matrix(rows, cols, std::vector<std::vector<int>>());
    }

    std::vector<std::vector<int>> result(rows, std::vector<int>(cols, 0));
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            result[i][j] = data[i][j] + other.data[i][j];
        }
    }
    return Matrix(rows, cols, result);
}


Matrix Matrix::rightMul(const Matrix& other) const{

    if(cols != other.rows){
        std::cout<<"dim error"<<std::endl;
        return Matrix(rows, cols, data);
    }
    int item ;
    std::vector<std::vector<int>> result(rows, std::vector<int>(other.cols,0));

    for(int i = 0; i < rows; i++){
        for(int j = 0; j < other.cols; j++){
            item = 0;
            for(int k = 0; k < cols; k++){
                item += data[i][k]*other.data[k][j];
            }
            result[i][j] = item;
        }
    }
    return Matrix(rows, other.cols, result);
}


Matrix Matrix::leftMul(const Matrix& other) const{

    if(rows != other.cols){
        std::cout<<"dim error"<<std::endl;
        return Matrix(rows, cols, data);
    }
    int item ;
    std::vector<std::vector<int>> result(other.rows, std::vector<int>(cols,0));

    for(int i = 0; i < other.rows; i++){
        for(int j = 0; j < cols; j++){
            item = 0;
            for(int k = 0; k < other.cols; k++){
                item += other.data[i][k]*data[k][j];
            }
            result[i][j] = item;
        }
    }
    return Matrix(other.rows, cols, result);
}


Matrix Matrix::kMul(int k) const {
    std::vector<std::vector<int>> result(rows, std::vector<int>(cols,0));
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            result[i][j] = k*data[i][j];
        }
    }
    return Matrix(rows, cols, result);
}

void Matrix::Print(){
    for(int i = 0; i< rows; i++){
        for(int j = 0; j< cols; j++){
            std::cout<<data[i][j]<<" ";
        }
        std::cout<<std::endl;
    }
}

void Matrix::setElement(int row, int col, int item){
    data[row][col] = item;
}

void Matrix::printElement(int row, int col) const{
    std::cout<<data[row][col]<<std::endl;
}

