import copy
import random
import logging



class Hat:

    #  *args: Receive multiple arguments as a tuple
    #  **kwargs: Receive multiple keyword arguments as a dictionary

    

    def __init__(self, **kwargs):
        #logging.info('kwargs: ', kwargs)
        #logging.info('type: ', type(kwargs))

        #for item in kwargs.items():
            #logging.info(item)
            #logging.info(item.values)

        self.contents = []
        for key in kwargs.keys():
            #logging.info(key)
            #logging.info(kwargs[key])
            ii = kwargs[key]
            while ii > 0:
                self.contents.append(key)
                ii -= 1
            #logging.info(item.values)        

        #logging.info(self.contents)

    def draw1(self, n):
        
        #workList = copy.deepcopy(self.contents)
        workList = self.contents

        if (n >= len(workList)):
            return workList
        
        return random.choices(workList,k=n)



    def draw(self, n):
        
        #logging.info("\n\nContents Before draw is {}".format(self.contents))
        workList = self.contents
        retList = []

        if (n >= len(self.contents)):
            retList = workList
            return retList
        
        while n > 0:
            n -= 1
            idx = random.randrange(0, len(workList))
            logging.info("Found {} at index {} and length is {}".format(workList[idx], idx, len(workList)))
            retList.append(workList[idx])
            del workList[idx]
            logging.info("Contents after this draw is {}".format(workList))
        
        logging.info("Contents after draw is {}".format(workList))
        logging.info("Drawing {} and remaining is {}\n\n".format(retList, workList))
        return retList

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    foundMatchCount = 0
    total = num_experiments
    while num_experiments > 0:
        logging.info("\n\nExperiment # {}".format(num_experiments))
        workhat = copy.deepcopy(hat)
        num_experiments -= 1
        drawn = workhat.draw(num_balls_drawn)
        logging.info(drawn)

        foundMatch = True
        for key in expected_balls:
            
            value = expected_balls[key]
            count = 0
            for ball in drawn:
                if ball == key:
                    count += 1
            
            logging.info("Processing Key {} Value {} Found Matches {}".format(key, expected_balls[key], count))

            if value > count:
                foundMatch = False


        if foundMatch == True:
            foundMatchCount += 1

    logging.info("Total match {} out of  {}".format(foundMatchCount, total))
    return foundMatchCount/total



if __name__ == "__main__":

    #logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(format='%(levelname)s:%(asctime)s:%(funcName)s:%(lineno)d:%(message)s', level=logging.DEBUG)

    random.seed(95)
    hat1 = Hat(red=5,blue=5)
    logging.info(hat1.draw(2))
    
    
    hat = Hat(black=6, red=6)
    probability = experiment(hat=hat, 
                  expected_balls={"red":1,"black":1},
                  num_balls_drawn=2,
                  num_experiments=2)

    logging.info(probability)

    hat = Hat(red=5,blue=2)
    actual = hat.draw(2)
    expected = ['blue', 'red']

    actual = len(hat.contents)
    expected = 5