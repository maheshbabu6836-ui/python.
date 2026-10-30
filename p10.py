# PYTHON ACTIVITY-BASED LEARNING

## ADDITIONAL 10 CASE STUDIES

Name: N Varun Kumar Reddy\
Roll Number: 26001228\
Section: CSM-6\
Course: Python Programming\
Year: B.Tech First Year

# CASE STUDY 7: RETAIL BILLING WITH MULTIPLE DISCOUNT RULES

## 1. Problem Statement

Develop a Python program to calculate the total bill for multiple products and apply discounts based on the purchase amount.

## 2. Objectives

- Accept multiple product prices and quantities.
- Calculate the total purchase amount.
- Apply discounts based on billing slabs.
- Display the final payable amount.

## 3. Assumptions

- A 10% discount is applied for bills of ₹2000 or above.
- A 5% discount is applied for bills of ₹1000 or above.
- No discount is provided below ₹1000.

## 4. Algorithm

1. Read the number of products.
2. Input the price and quantity of each product.
3. Calculate the subtotal.
4. Check the discount conditions.
5. Calculate the discount amount.
6. Calculate the final bill.
7. Display the bill details.

## 5. Flowchart

START → INPUT NUMBER OF PRODUCTS → INPUT PRICE AND QUANTITY → CALCULATE SUBTOTAL → CHECK DISCOUNT → CALCULATE FINAL BILL → DISPLAY BILL → END

## 6. Pseudocode

START\
INPUT number_of_products\
total = 0\
FOR each product:\
INPUT price and quantity\
total = total + price \* quantity\
IF total >= 2000:\
discount = total \* 0.10\
ELSE IF total >= 1000:\
discount = total \* 0.05\
ELSE:\
discount = 0\
final_bill = total - discount\
DISPLAY total, discount, final_bill\
END

## 7. Python Source Code

```
n = int(input("Enter number of products: "))total = 0for i in range(n):    price = float(input("Enter product price: "))    quantity = int(input("Enter quantity: "))    total += price * quantityif total >= 2000:    discount = total * 0.10elif total >= 1000:    discount = total * 0.05else:    discount = 0final_bill = total - discountprint("Subtotal:", total)print("Discount:", discount)print("Final Bill:", final_bill)
```

## 8. Test Cases

- Purchase amount ₹2500: 10% discount.
- Purchase amount ₹1500: 5% discount.
- Purchase amount ₹500: No discount.

## 9. Sample Output

```
Enter number of products: 2
Enter product price: 1000
Enter quantity: 2
Enter product price: 500
Enter quantity: 1
Subtotal: 2500.0
Discount: 250.0
Final Bill: 2250.0
```

## 10. Conclusion

The program calculates retail bills and applies discounts using conditional statements and loops.

# CASE STUDY 13: ATM TRANSACTION SEQUENCE SIMULATION

## 1. Problem Statement

Develop a Python program to simulate multiple ATM transactions, including deposits and withdrawals, while maintaining the account balance.

## 2. Objectives

- Maintain an account balance.
- Process deposits and withdrawals.
- Validate transaction amounts.
- Display the final account balance.

## 3. Assumptions

- The initial balance is ₹5000.
- Deposits increase the balance.
- Withdrawals decrease the balance.
- Withdrawals cannot exceed the available balance.

## 4. Algorithm

1. Initialize the account balance.
2. Read the number of transactions.
3. Accept the transaction type.
4. Accept the transaction amount.
5. Process deposits or withdrawals.
6. Check available balance before withdrawal.
7. Display the updated balance.

## 5. Flowchart

START → INITIALIZE BALANCE → INPUT TRANSACTION TYPE → INPUT AMOUNT → CHECK TRANSACTION → UPDATE BALANCE → DISPLAY BALANCE → END

## 6. Pseudocode

START\
balance = 5000\
INPUT number_of_transactions\
FOR each transaction:\
INPUT transaction_type and amount\
IF transaction_type = deposit:\
balance = balance + amount\
ELSE IF transaction_type = withdrawal:\
IF amount = 75:\
category = Excellent\
ELSE IF average >= 50:\
category = Good\
ELSE:\
category = Needs Improvement\
DISPLAY total, average and category\
END

## 7. Python Source Code

```
n = int(input("Enter number of students: "))for i in range(n):    print("Student", i + 1)    marks = []    for j in range(3):        mark = float(input("Enter subject marks: "))        marks.append(mark)    total = sum(marks)    average = total / 3    if average >= 75:        category = "Excellent"    elif average >= 50:        category = "Good"    else:        category = "Needs Improvement"    print("Total:", total)    print("Average:", round(average, 2))    print("Performance:", category)
```

## 8. Test Cases

- Marks 80, 85, 90: Excellent.
- Marks 60, 55, 65: Good.
- Marks 30, 40, 35: Needs Improvement.

## 9. Sample Output

```
Enter number of students: 1
Student 1
Enter subject marks: 80
Enter subject marks: 85
Enter subject marks: 90
Total: 255.0
Average: 85.0
Performance: Excellent
```

## 10. Conclusion

The program analyses student performance using lists, loops, and conditional statements.

# CASE STUDY 23: STUDENT TIMETABLE CONFLICT DETECTION

## 1. Problem Statement

Develop a Python program to check whether two scheduled classes overlap by comparing their starting and ending times.

## 2. Objectives

- Store class schedules.
- Compare class timings.
- Detect overlapping periods.
- Display timetable conflicts.

## 3. Assumptions

- Time is entered in 24-hour HH:MM format.
- Class timings are entered in the same format.
- Two classes conflict if their time periods overlap.

## 4. Algorithm

1. Read the starting and ending times of the first class.
2. Read the starting and ending times of the second class.
3. Compare the time intervals.
4. Check whether the intervals overlap.
5. Display the result.

## 5. Flowchart

START → INPUT FIRST CLASS TIMING → INPUT SECOND CLASS TIMING → COMPARE TIME INTERVALS → CHECK OVERLAP → DISPLAY RESULT → END

## 6. Pseudocode

START\
INPUT start1, end1\
INPUT start2, end2\
IF start1 < end2 AND start2 < end1:\
DISPLAY timetable conflict\
ELSE:\
DISPLAY no conflict\
END

## 7. Python Source Code

```
start1 = input("Enter first class start time (HH:MM): ")end1 = input("Enter first class end time (HH:MM): ")start2 = input("Enter second class start time (HH:MM): ")end2 = input("Enter second class end time (HH:MM): ")if start1 < end2 and start2 < end1:    print("Timetable conflict detected")else:    print("No timetable conflict")
```

## 8. Test Cases

- Class 1: 09:00–10:00; Class 2: 09:30–10:30: Conflict.
- Class 1: 09:00–10:00; Class 2: 10:00–11:00: No conflict.
- Class 1: 10:00–11:00; Class 2: 12:00–13:00: No conflict.

## 9. Sample Output

```
Enter first class start time (HH:MM): 09:00
Enter first class end time (HH:MM): 10:00
Enter second class start time (HH:MM): 09:30
Enter second class end time (HH:MM): 10:30
Timetable conflict detected
```

## 10. Conclusion

The program compares class schedules and identifies overlapping time periods using conditional statements.

# CASE STUDY 28: REPEATED TRANSACTION DETECTION

## 1. Problem Statement

Develop a Python program to analyse transaction IDs and identify duplicate transactions and transactions with unusually high values.

## 2. Objectives

- Store transaction IDs and amounts.
- Identify duplicate transaction IDs.
- Detect high-value transactions.
- Display suspicious transaction details.

## 3. Assumptions

- Each transaction has an ID and amount.
- Duplicate IDs are considered repeated transactions.
- Transactions above ₹10,000 are considered high-value for this demonstration.

## 4. Algorithm

1. Read the number of transactions.
2. Input transaction IDs and amounts.
3. Store transaction details.
4. Check for duplicate IDs.
5. Check whether the transaction amount exceeds ₹10,000.
6. Display warnings where necessary.

## 5. Flowchart

START → INPUT TRANSACTION DETAILS → STORE TRANSACTIONS → CHECK DUPLICATE IDS → CHECK HIGH VALUE → DISPLAY WARNINGS → END

## 6. Pseudocode

START\
INPUT number_of_transactions\
CREATE empty list of transaction IDs\
FOR each transaction:\
INPUT transaction ID and amount\
IF ID already exists:\
DISPLAY duplicate transaction\
ELSE:\
ADD ID to list\
IF amount > 10000:\
DISPLAY high-value warning\
END

## 7. Python Source Code

```
n = int(input("Enter number of transactions: "))ids = []for i in range(n):    tid = input("Enter transaction ID: ")    amount = float(input("Enter amount: "))    if tid in ids:        print("Duplicate transaction detected")    else:        ids.append(tid)    if amount > 10000:        print("High-value transaction detected")    print("Transaction ID:", tid)    print("Amount:", amount)
```

## 8. Test Cases

- Transaction ID T101 entered twice: Duplicate detected.
- Transaction amount ₹15000: High-value warning.
- Unique transaction ID with ₹500: No warning.

## 9. Sample Output

```
Enter number of transactions: 2
Enter transaction ID: T101
Enter amount: 500
Transaction ID: T101
Amount: 500.0
Enter transaction ID: T101
Enter amount: 15000
Duplicate transaction detected
High-value transaction detected
Transaction ID: T101
Amount: 15000.0
```

## 10. Conclusion

The program uses lists and conditional statements to identify repeated transaction IDs and high-value transactions.

# CASE STUDY 34: STUDENT FEEDBACK SENTIMENT SCORING

## 1. Problem Statement

Develop a Python program to analyse student feedback using positive and negative keywords and classify the feedback sentiment.

## 2. Objectives

- Accept student feedback.
- Identify positive keywords.
- Identify negative keywords.
- Calculate a sentiment score.
- Classify feedback.

## 3. Assumptions

- Positive and negative keywords are predefined.
- Each positive keyword adds one point.
- Each negative keyword subtracts one point.
- A positive score indicates Positive feedback.
- A negative score indicates Negative feedback.
- A zero score indicates Neutral feedback.

## 4. Algorithm

1. Read student feedback.
2. Convert feedback into lowercase.
3. Split feedback into words.
4. Compare words with positive and negative keyword lists.
5. Calculate the sentiment score.
6. Classify the feedback.
7. Display the result.

## 5. Flowchart

START → INPUT FEEDBACK → CONVERT TO LOWERCASE → IDENTIFY KEYWORDS → CALCULATE SCORE → CLASSIFY SENTIMENT → DISPLAY RESULT → END

## 6. Pseudocode

START\
INPUT feedback\
CONVERT feedback to lowercase\
SPLIT feedback into words\
score = 0\
FOR each word:\
IF word is positive:\
score = score + 1\
ELSE IF word is negative:\
score = score - 1\
IF score > 0:\
DISPLAY Positive\
ELSE IF score < 0:\
DISPLAY Negative\
ELSE:\
DISPLAY Neutral\
END

## 7. Python Source Code

```
positive = ["good", "excellent", "nice", "helpful", "great"]negative = ["bad", "poor", "boring", "difficult", "worst"]feedback = input("Enter student feedback: ").lower()words = feedback.split()score = 0for word in words:    if word in positive:        score += 1    elif word in negative:        score -= 1print("Sentiment Score:", score)if score > 0:    print("Feedback: Positive")elif score < 0:    print("Feedback: Negative")else:    print("Feedback: Neutral")
```

## 8. Test Cases

- "The teaching is excellent and helpful": Positive.
- "The class is boring and difficult": Negative.
- "The class is today": Neutral.

## 9. Sample Output

```
Enter student feedback: The teaching is excellent and helpful
Sentiment Score: 2
Feedback: Positive
```

## 10. Conclusion

The program analyses student feedback using string operations, lists, and conditional statements to classify sentiment.

# CASE STUDY 38: ATM MENU-DRIVEN BANKING SIMULATION

## 1. Problem Statement

Develop a menu-driven Python program to simulate basic ATM operations such as checking balance, depositing money, withdrawing money, and exiting the system.

## 2. Objectives

- Display an ATM menu.
- Check account balance.
- Deposit money.
- Withdraw money.
- Exit the banking system.

## 3. Assumptions

- Initial account balance is ₹5000.
- Deposits and withdrawals must be positive.
- Withdrawals cannot exceed the available balance.

## 4. Algorithm

1. Initialize the account balance.
2. Display the ATM menu.
3. Read the user's choice.
4. Perform the selected operation.
5. Update the account balance.
6. Repeat until the user selects Exit.

## 5. Flowchart

START → INITIALIZE BALANCE → DISPLAY MENU → INPUT CHOICE → PERFORM OPERATION → UPDATE BALANCE → CHECK EXIT → END

## 6. Pseudocode

START\
balance = 5000\
REPEAT:\
DISPLAY ATM MENU\
INPUT choice\
IF choice = 1:\
DISPLAY balance\
ELSE IF choice = 2:\
INPUT deposit amount\
ADD amount to balance\
ELSE IF choice = 3:\
INPUT withdrawal amount\
IF amount  0:\
balance += amount\
print("Deposit successful")\
else:\
print("Invalid amount")

elif choice == 3:\
amount = float(input("Enter withdrawal amount: "))

if amount > 0 and amount <= balance:\
balance -= amount\
print("Withdrawal successful")\
else:\
print("Invalid amount or insufficient balance")

elif choice == 4:\
print("Thank you for using ATM")\
break

else:\
print("Invalid choice")

````

## 8. Test Cases
- Check balance: Displays ₹5000 initially.
- Deposit ₹1000: Balance becomes ₹6000.
- Withdraw ₹2000: Balance becomes ₹3000 from an initial ₹5000.
- Withdraw ₹7000: Insufficient balance.
- Select option 4: Exits the program.

## 9. Sample Output

```text
ATM MENU
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter choice: 1
Balance: 5000

ATM MENU
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter choice: 2
Enter deposit amount: 1000
Deposit successful

ATM MENU
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter choice: 1
Balance: 6000.0
````

## 10. Conclusion

The program demonstrates menu-driven programming using loops, conditional statements, and arithmetic operations.

# CASE STUDY 42: STUDENT MARKS MATRIX ANALYSIS

## 1. Problem Statement

Develop a Python program to store marks of multiple students in a matrix and calculate student totals, averages, and subject-wise averages.

## 2. Objectives

- Store marks using nested lists.
- Calculate student-wise totals.
- Calculate student-wise averages.
- Calculate subject-wise averages.

## 3. Assumptions

- Three students are considered.
- Each student has marks in three subjects.
- Maximum marks per subject are 100.
- All marks are entered as numerical values.

## 4. Algorithm

1. Read the number of students and subjects.
2. Create a marks matrix.
3. Input marks for each student.
4. Calculate each student's total and average.
5. Calculate subject-wise averages.
6. Display the results.

## 5. Flowchart

START → INPUT STUDENT AND SUBJECT DETAILS → CREATE MARKS MATRIX → INPUT MARKS → CALCULATE TOTALS → CALCULATE AVERAGES → DISPLAY RESULTS → END

## 6. Pseudocode

START\
INPUT number_of_students\
INPUT number_of_subjects\
CREATE marks matrix\
FOR each student:\
INPUT marks for all subjects\
FOR each student:\
total = sum of marks\
average = total / number_of_subjects\
DISPLAY total and average\
FOR each subject:\
CALCULATE subject average\
DISPLAY subject average\
END

## 7. Python Source Code

```
students = int(input("Enter number of students: "))subjects = int(input("Enter number of subjects: "))marks = []for i in range(students):    row = []    print("Student", i + 1)    for j in range(subjects):        mark = float(input("Enter marks: "))        row.append(mark)    marks.append(row)for i in range(students):    total = sum(marks[i])    average = total / subjects    print("Student", i + 1)    print("Total:", total)    print("Average:", round(average, 2))for j in range(subjects):    total = 0    for i in range(students):        total += marks[i][j]    average = total / students    print("Subject", j + 1, "Average:", round(average, 2))
```

## 8. Test Cases

- Student 1 marks: 80, 90, 70. Total = 240.
- Student 2 marks: 60, 70, 80. Total = 210.
- Student 3 marks: 90, 85, 95. Total = 270.
- Subject 1 average = 76.67.

## 9. Sample Output

```
Enter number of students: 2
Enter number of subjects: 3
Student 1
Enter marks: 80
Enter marks: 90
Enter marks: 70
Student 2
Enter marks: 60
Enter marks: 70
Enter marks: 80

Student 1
Total: 240.0
Average: 80.0

Student 2
Total: 210.0
Average: 70.0

Subject 1 Average: 70.0
Subject 2 Average: 80.0
Subject 3 Average: 75.0
```

## 10. Conclusion

The program uses nested lists and loops to analyse student marks and calculate student-wise and subject-wise averages.

# CASE STUDY 57: SMART CANTEEN ORDER AND STOCK MANAGEMENT

## 1. Problem Statement

Develop a Python program to manage canteen orders, calculate order costs, update stock quantities, and display available items.

## 2. Objectives

- Maintain a menu of food items.
- Store item prices and stock quantities.
- Process customer orders.
- Calculate the total bill.
- Update stock after each order.

## 3. Assumptions

- The canteen has a predefined menu.
- Each item has a fixed price.
- Orders cannot exceed available stock.
- Stock is updated after successful orders.

## 4. Algorithm

1. Create a menu with item prices and stock.
2. Display the available menu.
3. Read the selected item.
4. Read the required quantity.
5. Check stock availability.
6. Calculate the bill.
7. Update stock.
8. Display the final bill.

## 5. Flowchart

START → DISPLAY MENU → INPUT ITEM AND QUANTITY → CHECK STOCK → CALCULATE BILL → UPDATE STOCK → DISPLAY BILL → END

## 6. Pseudocode

START\
CREATE menu and stock\
total = 0\
REPEAT:\
DISPLAY menu\
INPUT item\
IF item = exit:\
STOP\
INPUT quantity\
IF quantity
