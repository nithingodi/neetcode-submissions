class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zero_count=0
        
        for num in nums:
            if num ==0:
                zero_count+=1
            else:
                prod*=num

        output=[]

        for num in nums:
            if zero_count>1:
                output.append(0)
            elif zero_count==1:
                output.append(prod if num==0 else 0)
            else:
                output.append(prod//num)
        
        return output

