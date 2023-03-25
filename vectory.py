#carolina Estrada
class Vector:

  def __init__(self,P,Q):
    """"This is the beginning function that takes the variables and relates them back to the class Vector. These variables don't change the function itself it just connects them to later use in different functions in the class Vector.
    """
    
    if all(type(x) == int or float for x in P) and all(type(y)== int or float for y in Q):
      # checking if the values in P or Q are numbers being integers or floats
      if type(P) == list and type(Q) == list:
        if len(P) == len(Q):
          self.initial = P
          self.terminal = Q
          self.vector = []
          for element1, element2 in zip(P, Q):
            item = element2 - element1
            self.vector.append(item)
        else:
          raise AssertionError("AssertionError")
      else:
        # raising these errors incase any of the if statements fail. 
        raise TypeError("TypeError")
    else:
      raise TypeError("TypeError")
          
  def dim(self): 
    return len(self.initial)
    # taking the length of P which should be the same as Q so either works. 
    

  def __str__(self):
    s = ','.join(str(i)for i in self.vector)
    return f'<{s}>'
    # used the join function with the commas in between to make the self.vector look like a vector in form of string. 

  def __getitem__(self,value):
    try: 
      return self.vector[value-1]
      # getting the index before because it will give a different index if left as value. 
    except IndexError:
      raise AssertionError("AssertionError")
      
  def __setitem__(self,num,new_value):
    """This function sets any value that the user may input to change any number in the vector as the new value, so it changes the vector itself once its set
    """
    self.vector[num-1] = new_value
    print(self.vector)
    
    
  def __eq__(self,other):
    """This function looks if the vectors are equal to each other being the same values, and checking if they are vectors themselves first before checking if they're the same vectors. 
    """
    if not isinstance(other,Vector):
      return False
    if self.vector == other.vector:
      return True
    else:
      return False
      
  def __add__(self,other):
    """This add function takes an empty list and looks through two vectors element by element and adds thems to then append to that list before turning it into vector form, this is done to basically add the same indexs and then return as vector.
    """
    try:
      vect_add = []
      for element1, element2 in zip(self.vector, other.vector):
        # using the zip to look at the elements in self.vect and other.vector one by one. 
        element = element1 + element2
        vect_add.append(element)
      return Vector([0 for i in range(len(vect_add))],vect_add)
    except AttributeError:
      # raising this error when it is not a vector
      raise AssertionError("AssertionError")
      
  def __sub__(self,other):
    
    try:
      vect_subt = []
      for element1, element2 in zip(self.vector, other.vector):
        element = element1 - element2
        vect_subt.append(element)
        # has the same concept as the add function, just subtracting the elements in both vectors. 
      return Vector([0 for i in range(len(vect_subt))],vect_subt)
    except AttributeError:
      raise AssertionError("AssertionError")


  def __rmul__(self,value):
    """ This function has two steps where it is either multiplied by two vectors or by a vector and integer. This process only function with the vector and integer when it was ordered in the form (vector * integer), hence another funciton was implemented to allow the other input (integer * vector) in order to satisfy the requirements. If a vector and vecter were multiplied, the dot product was used and returned as vector. This executed the result of a scalar vector or the dot product.
    """
    try:
      if not isinstance(value, Vector):
        new = [value*i for i in self.vector]
        return (Vector([0 for i in range(len(new))],new))
      else: 
        dot_product = 0
        # started at 0 for safety check that the addition wasn't messed up in the dot product, used zip again to look at each element. 
        for vect1, vect2 in zip(self.vector, value.vector):
          dot_product = dot_product + vect1*vect2
        return dot_product
        
    except TypeError:
      raise AssertionError("AssertionError")

  def __mul__(self,value):
    # again used this function for the __rm__() function so that any order of the scalar multiplication would function properly. 
    return self.__rmul__(value)
            
  def __abs__(self):
    num = 0
    for i in self.vector:
      num+= i**2
      # got the square of each element in a vector to then square root it to get magnitude. 
    magnitude = (num)**.5
    return round(magnitude,4)
    
r = Vector

def cross_product(v1,v2):
  if v1.dim() == 3 and v2.dim() == 3:
    # checking if the dimensions of two vectors were 3 and then allowing cross product. 
    cross_p = [v1[2]*v2[3] - v1[3]*v2[2],
                v1[3]*v2[1] - v1[1]*v2[3],
                v1[1]*v2[2] - v1[2]*v2[1]]
    
    return (Vector([0 for i in range(len(cross_p))],cross_p))
    # returning as vector. 
  else:
    raise AssertionError("AssertionError")

def is_parallel(v1,v2):
  # no fail case to demonstrate but had to do some formula to check if it was parallel. 
  parallel = (v1[1] * v2[2] - v1[2] * v2[1]) * (v1[1] * v2[2] - v1[2] * v2[1]) + (v1[0] * v2[2] - v2[0] * v1[2]) * \
  (v1[0] * v2[2] - v2[0] * v1[2]) + (v1[0] * v2[1] - v1[1] * v2[0]) * (v1[0] * v2[1] - v1[1] * v2[0])
  print(parallel)
  # looked at the index of each value in vector to replace in the formula.
  # was multiplying each element but backwards and subtracting to see if the result was 0 for each element. If they're parallel then both numbers should cancel out otherwise it would give a number
  if parallel == 0:
    # if that formula resulted in 0 then that means they're parallel and return true
    return True
  else:
    # any number resulted in that formula not 0 means non-parallel.
    return False
