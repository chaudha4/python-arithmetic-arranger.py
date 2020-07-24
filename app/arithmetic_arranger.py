
def dashes(n):
    return '-' * n

def spaces(n):
    return ' ' * n


def arithmetic_arranger(problems, printSolution=False):

  if (len(problems) > 5):
    return "Error: Too many problems."

  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  spacing = ""

  for problem in problems:

    entry = problem.split()

    if entry[1] != "-" and entry[1] != "+":
      #print("Error: Operator must be '+' or '-'.")
      return "Error: Operator must be '+' or '-'."

    if not(entry[0].isnumeric() and entry[2].isnumeric()):
      #print("Error: Numbers must only contain digits.")
      return "Error: Numbers must only contain digits."

    if len(entry[0]) > 4 or len(entry[2]) > 4:
      #print("Error: cannot be more than four digits.")
      return "Error: Numbers cannot be more than four digits." 
    
    #print("No errors in Processing - " + problem)

    line1pad = ""
    line2pad = ""
    line3pad = ""
    line4pad = ""
    if len(entry[0]) < len(entry[2]):
      pad1 = len(entry[2]) - len(entry[0])
      line1pad = spaces(pad1+2)
      line2pad = spaces(1)
      line3pad = dashes(len(entry[2])+2)
    elif len(entry[2]) < len(entry[0]):
      pad1 = len(entry[0]) - len(entry[2])
      line1pad = spaces(2)
      line2pad = spaces(pad1+1)
      line3pad = dashes(len(entry[0])+2)
    else:
      line1pad = spaces(2)
      line2pad = spaces(1)
      line3pad = dashes(len(entry[0])+2)

    line1 = line1 + spacing + line1pad + entry[0]
    line2 = line2 + spacing + entry[1] + line2pad + entry[2]
    line3 = line3 + spacing + line3pad

    if(printSolution):
      ans = str(eval(problem))
      line4pad = spaces(len(line3pad) - len(ans))
      line4 = line4 + spacing + line4pad + ans

    spacing = "    "


  if(printSolution):
    retstr = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    #print(line4)    
  else:
    retstr = line1 + "\n" + line2 + "\n" + line3

  return retstr