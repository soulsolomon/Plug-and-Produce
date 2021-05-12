class ValueCreate:
    ''' This class will automatically generate the coordinates value based on the start and end position and number of operations'''
    def __init__(self,startPosition, endPosition, distance, numberOperations):
        ''' initialize the class with the parameters'''
        self.startPosition = startPosition
        self.endPosition = endPosition
        self.distance = distance
        self.numberOperations = numberOperations
    
    def valueArray(self):
        arr = [0 for ar in range(0,self.numberOperations)]
        if (self.startPosition != self.endPosition):
            # check if there are more than two operations
                
            if (self.numberOperations > 1):
                distApart = self.distance                   
                for i in range(0,self.numberOperations):
                    # Check the direction of x value whether increasing or decreasing
                    if (self.endPosition > self.startPosition):
                        pos = self.startPosition + distApart * i
                        arr[i] = pos
                    else:
                        pos = self.startPosition - distApart * i
                        arr[i] = pos
            else:
                arr = [self.startPosition,self.endPosition]
        else: 
            arr = [self.startPosition for ar in range(0,self.numberOperations)]
            
        return arr