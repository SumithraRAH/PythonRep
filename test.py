import pytest

def fuzzy_math(num1,op,num2):
    if type(num1) != int or type(num2) != int:
        raise Exception('We need to do fuzzy math on ints')
    if op == '+':
        result = num1 + num2
    elif op  == '*':
        result = num1 * num2
    else:
        raise Exception(f"I don't know the operator to do math with'{op}'")  
    
    if result <0:
        return ' Negative'
    elif result<10:
        return ' Small Number'
    elif result<30:
        return ' Medium Number'
    else:
        return ' Large Number'



class TestFuzzyMath:
    def test_non_int_input_for_num1(self):
        with pytest.raises(Exception) as exc_info:
            fuzzy_math('hi','+',2)
        assert 'fuzzy math on ints' in str(exc_info)

    def test_non_int_input_for_num2(self):
        with pytest.raises(Exception) as exc2_info:
            fuzzy_math(2,'+','hi')
            assert 'fuzzy math on ints' in str(exc2_info)

    def test_addition_with_negative_result(self):
        assert ' Negative' in fuzzy_math(-1,'+' ,0)        
    def test_addition_with_small_result(self):
        assert ' Small Number' in fuzzy_math(2,'+',2)
              
    def test_addition_with_medium_result(self):
        assert ' Medium Number' in fuzzy_math(9,'+',9)

    def test_addition_with_large_result(self):
        assert ' Large Number' in fuzzy_math(9,'+',119)
      

    def test_multiplication_with_negative_result(self):
        assert ' Negative' in fuzzy_math(-1,'*' ,1)           
    def test_multiplication_with_small_result(self):
        assert ' Small Number' in fuzzy_math(2,'*',3)      
    def test_multiplication_with_medium_result(self):
        assert ' Medium Number' in fuzzy_math(3,'*', 9)         
    def test_multiplication_with_large_result(self):
        assert 'Large Number'  in fuzzy_math(5,'*', 10)  

    def test_invalid_operator(self):
     with pytest.raises(Exception) as exc3_info:
         fuzzy_math(4,'-',5)
         print(exc3_info)
         assert 'Invalid operator1' in str(exc3_info)
