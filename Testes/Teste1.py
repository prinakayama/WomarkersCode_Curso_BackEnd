import unittest


def str_to_bool(value):   #recebe uma cadeia de caracteres 
    try:
        value = value.lower() #atribuir a variável value para minúscula
    except AttributeError:  #se um valor com tipo diferente de cadeia de caracteres for usado
        raise AttributeError(f"{value} must be of type string")
    true_values = ['y','yes']
    false_values = ['no', 'n']
  

    if value in true_values:
        return True
    if value in false_values:
        return False

class TestStrToBool(unittest.TestCase): #Teste da funcao 
    
    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
    

    def test_invalid_input(self):  #metodo de assercao, verifica se AttributeError é gerado pela entrada não cadeia de caracteres:
         with self.assertRaises(AttributeError):
             str_to_bool(1)