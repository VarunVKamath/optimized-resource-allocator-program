#Optimized resource allocator program that can be used for cost planning.
import sys
sys.setrecursionlimit(10**6)

#Class to gernerate the Number of Combinations for a given input.
class Sol:
    def com_sum(self, capacities:[], total_units: int):
        return sumsolve(capacities, total_units, 0, 0, ())

# Recursive calls to avoid duplicates and preserving the order of the outputs.
def sumsolve(capacities, total_units, sum, start, path):  
    result = []
    for i in range(start, len(capacities)):     
        total = sum + capacities[i]
        if total < total_units:
            result += sumsolve(capacities, total_units, total, i, path + (capacities[i],))
        elif total == total_units:
            result.append(list(path + (capacities[i],)))
            
    return result
#Function to generate the output
def main():
  ip=int(input('enter the capacity'))
  hours=int(input('Enter the number of hours'))
  #Calculating the total number of units required.
  IP=ip*hours
  
  #Calculations for 1st Region ie. New York
  #Creation of object based on New York region specifications.
  ob1=Sol().com_sum([10,20,40,80,160,320],IP)

  #lists to store counts of different containers Ex: cnt_10 will store for container of 10 units(Large) and so on.
  cnt_10=[]
  cnt_20=[]
  cnt_40=[]
  cnt_80=[]
  cnt_160=[]
  cnt_320=[]

  #List to store all the possible costs needed to run a input.
  cost1=[]
  #Function to calculate all the possible costs needed to run a input.
  def NY_Cost(a,b,c,d,e,f):
      c1=(120*a)+(230*b)+(450*c)+(774*d)+(1400*e)+(2820*f)
      return c1
  # Calculating the minuimum Cost from the posssible costs
  for i in range(len(ob1)):
      cnt_10.append(ob1[i].count(10))
      cnt_20.append(ob1[i].count(20))
      cnt_40.append(ob1[i].count(40))
      cnt_80.append(ob1[i].count(80))
      cnt_160.append(ob1[i].count(160))
      cnt_320.append(ob1[i].count(320))
      cost1.append(NY_Cost(cnt_10[i], cnt_20[i],cnt_40[i],cnt_80[i],cnt_160[i],cnt_320[i]))

  min_cost1=min(cost1)
  min_cost_pos1=cost1.index(min_cost1)

  #Storing the Output.
  ans1={'10XLarge':cnt_320[min_cost_pos1],'8XLarge':cnt_160[min_cost_pos1],'4XLarge':cnt_80[min_cost_pos1],'2XLarge':cnt_40[min_cost_pos1],'XLarge':cnt_20[min_cost_pos1],'Large':cnt_10[min_cost_pos1]}
      
  res1={key : val for key, val in ans1.items()  
             if not isinstance(val, int) or val!=0}

  #Calculations for 2nd Region ie. India.
  #Creation of object based on India region specifications.
  ob2=Sol().com_sum([10,40,80,160,320],IP)

  cnt_10I=[]
  cnt_40I=[]
  cnt_80I=[]
  cnt_160I=[]
  cnt_320I=[]
  cost2=[]
  
  def IND_Cost(a,c,d,e,f):
      c2=(140*a)+(413*c)+(890*d)+(1300*e)+(2970*f)
      return c2
  for i in range(len(ob2)):
      cnt_10I.append(ob2[i].count(10))
      cnt_40I.append(ob2[i].count(40))
      cnt_80I.append(ob2[i].count(80))
      cnt_160I.append(ob2[i].count(160))
      cnt_320I.append(ob2[i].count(320))
      cost2.append(IND_Cost(cnt_10I[i],cnt_40I[i],cnt_80I[i],cnt_160I[i],cnt_320I[i]))

  min_cost2=min(cost2)
  min_cost_pos2=cost2.index(min_cost2)
  ans2={'10XLarge':cnt_320I[min_cost_pos2],'8XLarge':cnt_160I[min_cost_pos2],'4XLarge':cnt_80I[min_cost_pos2],'2XLarge':cnt_40I[min_cost_pos2],'Large':cnt_10I[min_cost_pos2]}
  res2={key : val for key, val in ans2.items()  
             if not isinstance(val, int) or val!=0}

  #Lists Used for 3rd Region ie. China
  #Creation of object based on China region specifications.
  ob3=Sol().com_sum([10,20,80,160],IP)

  cnt_10C=[]
  cnt_20C=[]
  cnt_80C=[]
  cnt_160C=[]
  cost3=[]
  def CHN_Cost(a,b,d,e):
      c3=(110*a)+(200*b)+(670*d)+(1180*e)
      return c3
  for i in range(len(ob3)):
      cnt_10C.append(ob3[i].count(10))
      cnt_20C.append(ob3[i].count(20))
      cnt_80C.append(ob3[i].count(80))
      cnt_160C.append(ob3[i].count(160))
      cost3.append(CHN_Cost(cnt_10C[i], cnt_20C[i],cnt_80C[i],cnt_160C[i]))


  min_cost3=min(cost3)
  min_cost_pos3=cost3.index(min_cost3)
  ans3={'8XLarge':cnt_160C[min_cost_pos3],'4XLarge':cnt_80C[min_cost_pos3],'XLarge':cnt_20C[min_cost_pos3],'Large':cnt_10C[min_cost_pos3]}

  res3={key : val for key, val in ans3.items()  
             if not isinstance(val, int) or val!=0}

  #Displaying The Outputs
  output=[
      {
        'region':'New York',
        'total_cost': '$'+str(min_cost1),
        'machines':res1
      },
      {
        'region': 'India',
        'total_cost':'$'+str(min_cost2),
        'machines':res2 ,
      },
      {
        'region': 'China',
        'total_cost':'$'+str(min_cost3) ,
        'machines': res3,
      },
    ]
  print (output)

#Calling the main function.
main()