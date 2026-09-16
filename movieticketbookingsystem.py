# MOVIE TICKET BOOKING SYSTEM

# variables
m_list = []
show = []
m_seats = []
v_booked = []


while True:
    try:
        start = int(input("select the option:  1.Admin section, 2.User section, 3.Exit\n "))
    except ValueError:
        print("Invalid input from user! Enter a number:")
        continue

    # =============== ADMIN ACCOUNT SECTION ===============

    if start == 1:
        print("*" * 5, "welcome to admin section", 5 * "*")

        while True:
            try:
                ad_choice = int(input(
                    "1.add movies \n"
                    "2.add show \n"
                    "3.manage seats \n"
                    "4.delete movie \n"
                    "5.view bookings \n"
                    "6.exit\n"
                ))
            except ValueError:
                print("Invalid input! Enter a number.")
                continue

            # ADD MOVIES

            if ad_choice == 1:
                m_list.extend(input("Enter movie name: ").split(","))
                print("_" * 5, "Movies uploaded successfully", "_" * 5)

            # SHOW TIMINGS

            elif ad_choice == 2:
                show.append(input("Add shows timings: "))
                print("Show timing added successfully!")

            # SEAT NUMBERS

            elif ad_choice == 3:
                m_seats.extend(input("Enter the seat numbers: ").split(","))
                print("Seats added successfully!")

            # DELETE MOVIE

            elif ad_choice == 4:
                movie = input("Enter a movie: ")

                if movie in m_list:
                    m_list.remove(movie)
                    print("Movie deleted successfully!!!")
                else:
                    print("Movie not found!")

            # VIEW BOOKINGS

            elif ad_choice == 5:
                print("Booked seats are:", v_booked)

            # EXIT ADMIN

            elif ad_choice == 6:
                print("Exit")
                break

            else:
                print("Invalid option!")

    # =============== USER ACCOUNT SECTION ===============

    elif start == 2:
        print("*" * 5, "welcome to user section", "*" * 5)

        while True:
            try:
                ur_choice = int(input(
                    "1.view movies and timings \n"
                    "2.select seats \n"
                    "3.view bookings \n"
                    "4.exit\n"
                ))
            except ValueError:
                print("Invalid input! Enter a number.")
                continue

            # AVAILABLE MOVIES

            if ur_choice == 1:
                print("Available Movies are:", m_list)
                print("Available Shows Timings:", show)
                print("Available seats are:", m_seats)

            # SEATS PRE BOOKING

            elif ur_choice == 2:

                if len(m_seats) == 0:
                    print("Seats not available!")

                else:
                    print("Available seats:", m_seats)

                    # FIXED: HANDLE INVALID NUMBER INPUT
                    try:
                        n_seats = int(input("Enter no.of seats: "))
                    except ValueError:
                        print("Invalid input! Enter a number.")
                        continue

                    # CHECK POSITIVE NUMBER

                    if n_seats <= 0:
                        print("Enter a positive number of seats!")
                        continue

                    # CHECK AVAILABLE SEATS

                    if n_seats > len(m_seats):
                        print("Not enough seats available!")
                        continue

                    for i in range(n_seats):

                        seat = input("Enter a seat number: ")

                        if seat in m_seats:
                            m_seats.remove(seat)
                            v_booked.append(seat)
                            print(seat, "seat is confirmed!")

                        else:
                            print(seat, "not available!!")

            # CONFIRMED SEATS

            elif ur_choice == 3:
                print("Booked seats:", v_booked)

            # EXIT USER

            elif ur_choice == 4:
                print("Exit")
                break

            else:
                print("Invalid option!")

    # =============== EXIT ===============

    elif start == 3:
        print("Goodbyee!!!")
        break

    else:
        print("Invalid option!!!")
