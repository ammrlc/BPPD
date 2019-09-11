
# coding: utf-8

# # Extending Classes to Make New Classes
# ## Building the child class

# In[1]:

class Animal:
   def __init__(self, Name="", Age=0, Type=""):
      self.Name = Name
      self.Age = Age
      self.Type = Type
   def GetName(self):
      return self.Name
   def SetName(self, Name):
      self.Name = Name
   def GetAge(self):
      return self.Age
   def SetAge(self, Age):
      self.Age = Age
   def GetType(self):
      return self.Type
   def SetType(self, Type):
      self.Type = Type
   def __str__(self):
      return "{0} is a {1} aged {2}".format(self.Name,
                                            self.Type,
                                            self.Age)


# In[2]:

class Chicken(Animal):
   def __init__(self, Name="", Age=0):
      self.Name = Name
      self.Age = Age
      self.Type = "Chicken"
   def SetType(self, Type):
      print("Sorry, {0} will always be a {1}"
            .format(self.Name, self.Type))
   def MakeSound(self):
      print("{0} says Cluck, Cluck, Cluck!".format(self.Name))


# In[ ]:



