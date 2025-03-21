class Quize:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer

Question=[
    
    "what is the capital of nepal?\n a.ktm\n b.pkr\n c.lalitpur\n d.damauli",
    "captain of nepali national cricket team?\na.rohit\nb.sompal\nc.sandip\nd.dippi",
    "what is the capital of india?\n a.delhi\n b.punjab\n c.pune\n d.goa"
    
    
         ]

lst=[
    Quize(Question[0],"a"),
    Quize(Question[1],"a"),
    Quize(Question[2],'a')
    
]

def show():
    for i in lst:
        score=0;
        user=input(f"{i.question}\n")
        if user==i.answer:
            score+=1
        else:
            print(f"your enter a wrong answer and the correct answer is {i.answer}")
    print(f"your score is {score}/len(lst)")
        
show()
