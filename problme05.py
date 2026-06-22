class train :
    def book(self,book,status,getfare):
        self.book = book
        self.status = status
        self.getfare = getfare
        print(f"the train is {self.book}. The status is {self.status}. The fare is {self.getfare}")
    
p = train("ticket1","running late",4500)
print(p.book,p.status,p.getfare)