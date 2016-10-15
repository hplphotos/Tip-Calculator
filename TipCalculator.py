# Calculate the amount people pay when splitting a restaurant bill
#
# Get input
Total_bill=float(input("What is the total bill? "))
How_Many_People=int(input("How many people will be splitting the bill? "))
Tip_percent=float(input("What is the tip percentage? "))/100

#Calculate results
pre_tip_per_person=Total_bill/How_Many_People
tip_per_person=pre_tip_per_person*Tip_percent
each_person_share_incl_tip=pre_tip_per_person+tip_per_person
total_bill_incl_tip=each_person_share_incl_tip*How_Many_People

#Print results
print("\nAmount per person before tip", "{:6.2f}".format(pre_tip_per_person))
print("Tip per person", "{:5.2f}".format(tip_per_person))
print("Amount per person including tip", "{:6.2f}".format(each_person_share_incl_tip))
print("Total tip", "{:5.2f}".format(How_Many_People*tip_per_person))
print("Total bill including tip", "{:6.2f}".format(Total_bill+How_Many_People*tip_per_person))