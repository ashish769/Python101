# class Quiz:
#     def __init__(self,question,answer) -> None:
#         self.question=question
#         self.answer=answer
class User:
    Question=[

        "1.What is the capital of Nepal?",
        "2.Captain of the Nepali national cricket team?",
        "3.What is the capital of India?",
        "4.What is the currency of Japan?",
        "5.Who is the current president of France?",
        "6.Which planet is known as the Red Planet?",
        "7.Who painted the Mona Lisa?",
        "8.What is the tallest mountain in the world?",
        "9.Which country is famous for the Great Barrier Reef?",
        "10.Who wrote 'To Kill a Mockingbird'?",
        "11.Which city hosted the 2016 Summer Olympics?",
        "12.What is the chemical symbol for gold?",
        "13.Who is the author of 'The Catcher in the Rye'?"


    ]
    option=[   
        ["a. KTM", "b. PKR", "c. Lalitpur", "d. Damauli"],
        ["a. Rohit", "b. Sompal", "c. Sandip", "d. Dippi"],
        ["a. Delhi", "b. Punjab", "c. Pune", "d. Goa"],
        ["a. Yen", "b. Won", "c. Yuan", "d. Ringgit"],
        ["a. Emmanuel Macron", "b. Angela Merkel", "c. Boris Johnson", "d. Justin Trudeau"],
        ["a. Mars", "b. Jupiter", "c. Venus", "d. Saturn"],
        ["a. Leonardo da Vinci", "b. Pablo Picasso", "c. Vincent van Gogh", "d. Michelangelo"],
        ["a. Mount Everest", "b. K2", "c. Mount Kilimanjaro", "d. Mount McKinley"],
        ["a. Australia", "b. Brazil", "c. Canada", "d. South Africa"],
        ["a. Harper Lee", "b. J.K. Rowling", "c. Ernest Hemingway", "d. George Orwell"],
        ["a. Rio de Janeiro", "b. Tokyo", "c. London", "d. Beijing"],
        ["a. Au", "b. Ag", "c. Fe", "d. Pb"],
        ["a. J.D. Salinger", "b. F. Scott Fitzgerald", "c. Ernest Hemingway", "d. Mark Twain"]
        ]

    answer=['a','b','a','a','a','a','a','a','a','a','a','a','a']
    def show(self):
        self.score=0
        for i in range(len(self.Question)):
            user=input(f"{self.Question[i]}\n{self.option[i][0]}\n{self.option[i][1]}\n{self.option[i][2]}\n{self.option[i][3]} \n enter the correct choice=>\n " )
            if user==self.answer[i]:
                self.score+=1
                print(" Brilliant !!!correct!!!")
            else:
                print(f"you are wronng the correct answer is {self.answer[i]}")
        print(f"Your score is {self.score}/{len(self.Question)} ")   
        
class Admin(User):
    
    def Authorization(self):
        Admin_pin=1234
        self.pin=int(input("Enter The Admin pin"))
        if(self.pin==Admin_pin):
            print("welcome!you are logged in")
        else:
            print("invalid pin")
            # return Authorization()
    @classmethod       
    def Add_question(cls):
        print("you are in the question addition center".title()) 
        
        question=input("enter your question\n")
        add_option=[]
        for i in range(4):
            op=input(f"enter your option {i+1} in the format of 'a.option1'\n") 
            add_option.append(op) 
        cls.option.append(add_option)#this are the class variable or static variable in the user class
 
        an=input("enter your correct option of the above question\n")
        cls.answer.append(an)
        print("question addition program end here")
        
        
    

                #starting portion
print("WELCOME TO THE MCQ ROOM".center(80,'*'))


choice=int(input(f"""ARE You User or Admin
                ENTER 1 FOR ADMIN
                ENTER 2 FOR USER\n
             """))
if choice==1:
    admin=Admin()
    admin.Authorization()
    admin.Add_question() 
if choice==2:
    user=User()
    user.show()

