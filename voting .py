# Hi everyone in this project I have created a small voting system 
nominee1 = input("Enter your 1st nominee: ")
nominee2 = input("Enter your 2nd nominee: ")
nomin1_votes = 0
nomin2_votes = 0
voters_id = [10, 20, 30, 40, 50]
no_of_voters = len(voters_id)
print("number of voters:", no_of_voters)
voted = []
while True:
    if voters_id == []:
        print("Voting is over")
        if nomin1_votes > nomin2_votes:
            print(f"{nominee1} won the election with {nomin1_votes}")
        elif nomin2_votes > nomin1_votes:
            print(f"{nominee2} won the election with {nomin2_votes}")
        elif nomin1_votes == nomin2_votes:
            print("tied !")
        break

    else:
        voter = int(input("Enter your Id"))
        if voter in voted:
            print("You already voted")
        else:
            if voter in voters_id:
                print(f"1.{nominee1}\n2.{nominee2}")
                choice = int(input("Enter your choice"))
                if choice == 1:
                    nomin1_votes += 1
                    print(f"you voted {nominee1}")
                elif choice == 2:
                    nomin2_votes += 1
                    print("you voted {nominee2}")
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("you are not allowed to vote")
