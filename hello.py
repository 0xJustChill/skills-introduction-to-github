def greetHim(people: str) -> bool:
    print(f"Hello! Nice to meet you, {people}.")
    if len(people) >= 10:
        return False
    else:
        return True

if __name__=="__main__":
    greetHim(people="Joachim")
