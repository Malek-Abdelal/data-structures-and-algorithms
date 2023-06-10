from stack.stack import Stack

bra = "[]{hi(})"
# def validate_brackets(brackets_str):


def validate_brackets(input):
  brackets = {"{" : "}",
              "[":"]",
              "(":")"}
  stack = Stack()

  for char in input : 
    if char in brackets.keys() :
      stack.push(char)
    elif char in brackets.values():
      try :
        if brackets[str(stack.peek())] != char :
          return False
        stack.pop()
      except:
        # raisng excption for empty stack or input 
        return "something went wrong !"
  return True if stack.is_empty()   else False   
        


    # stack = Stack()
    # brackets = ["{", "}", "[", "]", "(", ")"]
    # counter = 0
    # for ele in brackets_str:
    #     if ele in brackets:
    #         stack.push(ele)
    #         counter += 1
    # if counter % 2 != 0:
    #     return False
    # current = stack.top
    # counter = 0
    # while current:
    #     if counter % 2 == 0:
    #         if brackets.index(current.value) - 1 != brackets.index(current.next.value) :
    #             return False
    #     counter += 1
    #     current = current.next
    # # print(not stack)
    # return True

print(validate_brackets(bra))