import numpy as np


def calculate(list):

    #print(type(list))

    try:
        a1 = np.array(list).reshape(3, 3)
    except ValueError as ve:
        print(ve)
        raise ValueError("List must contain nine numbers.")

    print(a1)
    print(a1.mean(axis=0))

    return {
        'mean': [a1.mean(axis=0).tolist(), a1.mean(axis=1).tolist(), a1.reshape(9).mean(axis=0).tolist()],
        'variance': [a1.var(axis=0).tolist(), a1.var(axis=1).tolist(), a1.reshape(9).var(axis=0).tolist()],
        'standard deviation': [a1.std(axis=0).tolist(), a1.std(axis=1).tolist(), a1.reshape(9).std(axis=0).tolist()],
        'max': [a1.max(axis=0).tolist(), a1.max(axis=1).tolist(), a1.reshape(9).max(axis=0).tolist()],
        'min': [a1.min(axis=0).tolist(), a1.min(axis=1).tolist(), a1.reshape(9).min(axis=0).tolist()],
        'sum': [a1.sum(axis=0).tolist(), a1.sum(axis=1).tolist(), a1.reshape(9).sum(axis=0).tolist()],
    }


if __name__ == "__main__":

    #calculate(np.zeros(9).tolist())  # 9 zeros, passed as a list (tolist())
    #calculate(np.ones(9).tolist())  # 9 zeros, passed as a list (tolist())
    #calculate(np.random.rand(9))    # 9 random floats passed as a numpy array.
    
    # 9 Random int between 0 to 29 passed as a numpy array.
    #calculate(np.random.randint(0, high=30, size=9))

    print(calculate([0,1,2,3,4,5,6,7,8]))
