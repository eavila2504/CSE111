def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")

  #reverse and print the list
  fruit_list.reverse()
  print(f"reversed: {fruit_list}")

  #apppend orange
  fruit_list.append("orange")
  print(f"append orange: {fruit_list}")

  #insert cherry before apple
  index = fruit_list.index("apple")
  fruit_list.insert(index, "cherry")
  print(f"insert cherry: {fruit_list}")

  #remove banana
  fruit_list.remove("banana")
  print(f"remove banana: {fruit_list}")

  #pop orange
  last = fruit_list.pop()
  print(f"pop {last}: {fruit_list}")

  #sort the list
  fruit_list.sort()
  print(f"sorted: {fruit_list}")

  #clear the list
  fruit_list.clear()
  print(f"Cleared: {fruit_list}")
  

    


if __name__ == "__main__":
 main()

