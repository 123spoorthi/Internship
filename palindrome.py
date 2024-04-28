class A:
    def reverse(self,n):
        s=str(n)
        return s[::-1]
class B(A):
    def palindrome(self,n):
        if self.reverse(n)==n:
            return "palindrome"
        else:
            return "Not palindrome"
print(B().reverse(121))#palindrome

