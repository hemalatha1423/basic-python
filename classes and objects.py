
class Cart:
    def __init__(self,imageURL,price,rating,description,deliverydate,comments,brandName):
        self.image=imageURL
        self.price=price
        self.rating=rating
        self.description=description
        self.deliverydate=deliverydate
        self.comments=comments
        self.brandName=brandName
  
    def printalldetials(self):
        print(self.image)
        print(self.price)
        print(self.rating)
        print(self.description)
        print(self.deliverydate)
        print(self.comments)
        print(self.brandName)




commentsforlaptop=["good","simple","ok"]
laptop=Cart("img123",75000,4.2,"display 14.5","4 days",commentsforlaptop,"hp")
laptop.printalldetials()

commentsforphone=["best","battery is good","camera is good"]
phone=Cart("img142",25000,4.5,"high storage","3days",commentsforphone,"Samsung")
phone.printalldetials()

commentsforwatch=["satifiedwithitem"]
watch=Cart("img126",3000,4.8,"smart and sim available","8 days",commentsforwatch,"boat")
watch.printalldetials()
