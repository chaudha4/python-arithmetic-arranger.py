"""
A year is divided into four seasons: winter, spring, summer and autumn in that order. 
A year has N days and every season lasts for exactly N/4 days. The year starts on the first day of winter and ends on the last day of autumn.

Given the history of temperatures from the previous year, find the season with the highest amplitude of temperatures. 
The amplitude is the difference between the highest and lowest temperatures over the given period. Assume that all seasons 
within one year have different temperature amplitudes.


For example, given T = [−3, −14, −5, 7, 8, 42, 8, 3]:
the function should return "SUMMER", since the highest amplitude (34) occurs in summer.

Given T = [2, −3, 3, 1, 10, 8, 2, 5, 13, −5, 3, −18]:
the correct answer is "AUTUMN" (amplitude equals 21).
"""


def four_seasons(T):
    """
    >>> four_seasons([-3, -14, -5, 7, 8, 42, 8, 3])
    'SUMMER'
    >>> four_seasons([2, -3, 3, 1, 10, 8, 2, 5, 13, -5, 3, -18])
    'AUTUMN'
    """

    count = len(T) // 4

    winter_ampli = max(T[:count:]) - min(T[:count:])
    spring_ampli = max(T[count:count*2:]) - min(T[count:count*2:])
    
    summer_ampli = max(T[count*2:count*3:]) - min(T[count*2:count*3:])

    autumn_ampli = max(T[count*3::]) - min(T[count*3::])

    max_ampli = winter_ampli
    season = "WINTER"
    if (spring_ampli > max_ampli):
        max_ampli = spring_ampli
        season = "SPRING"
    
    if (summer_ampli > max_ampli):
        max_ampli = summer_ampli
        season = "SUMMER"
    
    if (autumn_ampli > max_ampli):
        max_ampli = autumn_ampli
        season = "AUTUMN"
    
    return season

if __name__ == "__main__":
    assert four_seasons([-3, -14, -5, 7, 8, 42, 8, 3]) == "SUMMER", "Test 1"

    #four_seasons([2, -3, 3, 1, 10, 8, 2, 5, 13, -5, 3, -18])

    import doctest  # See https://docs.python.org/3/library/doctest.html
    #doctest.testmod(verbose=True)      