class A:
    def method(self):
        print(10+10)
class B(A):
      def method(self):
          print(10-10)
A().method() #if we give A() it will print A we give function Bit wiil print B