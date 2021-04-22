from tkinter import *



class Frames(object):

    def movie_details(self):
        self.date_disp = StringVar()
        self.day_disp = StringVar()
        self.month_disp = StringVar()
        self.location = StringVar()

        newwin = Toplevel(root)
        newwin.title('Movie Details')
        newwin.geometry("400x300")
        newwin.resizable(0, 0)

        date1 = Label(newwin, text="Date", fg="white", bg="red", width=10, height=1)
        date1.place(x=50, y=30)

        entry_date1 = Entry(newwin, width=20, textvariable=self.date_disp)
        entry_date1.place(x=150, y=30)

        day1 = Label(newwin, text="Day", fg="white", bg="red", width=10, height=1)
        day1.place(x=50, y=60)

        entry_day1 = Entry(newwin, width=20, textvariable=self.day_disp)
        entry_day1.place(x=150, y=60)

        month1 = Label(newwin, text="Month", fg="white", bg="red", width=10, height=1)
        month1.place(x=50, y=90)

        entry_month1 = Entry(newwin, width=20, textvariable=self.month_disp)
        entry_month1.place(x=150, y=90)

        city = Label(newwin, text="Enter Your Preferred City", fg="white", bg="red", width=50, height=2)
        city.place(x=20, y=150)

        entry_city = Entry(newwin, width=20, textvariable=self.location)
        entry_city.place(x=130, y=200)

        search = Button(newwin, text="Search", command=self.sel_theatre)
        search.place(x=180, y=250)


    def sel_theatre(self):
        newwin = Toplevel(root)
        newwin.title('List of Theatres')
        newwin.geometry("400x500")
        newwin.resizable(0, 0)

        top_info = Label(newwin, text="Hi "+ self.query.get()+ ", here are the \n theatres available in "+ self.location.get()
                         , fg="white", bg="grey", width=40, height=4)
        top_info.pack()

        theatre_1 = Button(newwin, text="INOX Cinemas", fg="white", bg="red", width=40, height=3,
                           command= lambda: [ self.th1_assn()])
        theatre_1.place(x=50, y=100)

        theatre_2 = Button(newwin, text="Cineplex", fg="white", bg="red", width=40, height=3,
                           command= lambda: [ self.th2_assn()])
        theatre_2.place(x=50, y=180)

        theatre_3 = Button(newwin, text="Central Mall Theatre", fg="white", bg="red", width=40, height=3,
                           command= lambda: [ self.th3_assn()])
        theatre_3.place(x=50, y=260)

        theatre_4 = Button(newwin, text="PVR Cinemas", fg="white", bg="red", width=40, height=3,
                           command= lambda: [ self.th4_assn()])
        theatre_4.place(x=50, y=340)

        theatre_5 = Button(newwin, text="Uma Talkies", fg="white", bg="red", width=40, height=3,
                           command= lambda: [ self.th5_assn()])
        theatre_5.place(x=50, y=420)


    def th1_assn(self):
        global code
        code = 1
        self.th_assign()


    def th2_assn(self):
        global code
        code = 2
        self.th_assign()


    def th3_assn(self):
        global code
        code = 3
        self.th_assign()


    def th4_assn(self):
        global code
        code = 4
        self.th_assign()


    def th5_assn(self):
        global code
        code = 5
        self.th_assign()


    def th_assign(self):
        global hall
        if code == 1:
            hall ="INOX"

        elif code == 2:
            hall ="Cineplex"

        elif code == 3:
            hall ="Central Mall Theatre"

        elif code == 4:
            hall ="PVR Cinemas"

        elif code == 5:
            hall ="Uma Talkies"


        newwin = Toplevel(root)
        newwin.title('List of Movies')
        newwin.geometry("400x600")
        newwin.resizable(0, 0)

        def sel_movie(self):


            display_top = Label(newwin, text= "The Movies Available in "+ hall + "\n on " + self.date_disp.get() +
                                " " + self.month_disp.get() + ", " + self.day_disp.get(), bg="grey", fg="white", height="3", width="50")
            display_top.pack()

            movie_1 = Button(newwin, text="Avengers Endgame", fg="white", bg="red", width=40, height=3,
                               command=lambda: [film_1(self)])
            movie_1.place(x=50, y=100)

            movie_2 = Button(newwin, text="Weathering With You", fg="white", bg="red", width=40, height=3,
                             command=lambda: [film_2(self)])
            movie_2.place(x=50, y=180)

            movie_3 = Button(newwin, text="Parasite", fg="white", bg="red", width=40, height=3,
                             command=lambda: [film_3(self)])
            movie_3.place(x=50, y=260)

            movie_4 = Button(newwin, text="Toy Story 4", fg="white", bg="red", width=40, height=3,
                             command=lambda: [film_4(self)])
            movie_4.place(x=50, y=340)

            movie_5 = Button(newwin, text="Klaus", fg="white", bg="red", width=40, height=3,
                             command=lambda: [film_5(self)])
            movie_5.place(x=50, y=420)

            movie_6 = Button(newwin, text="Interstellar", fg="white", bg="red", width=40, height=3,
                             command=lambda: [film_6(self)])
            movie_6.place(x=50, y=500)


        def film_1(self):
            newwin = Toplevel(root)
            newwin.title('Available Shows')
            newwin.geometry("400x300")
            newwin.resizable(0, 0)

            global film_name
            film_name = "Avengers Endgame"

            disp_topper = Label(newwin, text="Shows available for 'Avengers Endgame'\n on " + self.date_disp.get() + " " +
                                self.month_disp.get() + ", " + self.day_disp.get() + " at " + hall, bg="grey", fg="white", height=3, width=50)
            disp_topper.pack()

            disp_show1 = Button(newwin, text="Screen 1, 8:30a.m.- 11:00a.m.", fg="white", bg="red", width=30,
                                height=3, command= lambda: [show_time1(), Screen1()])
            disp_show1.place(x=70, y=100)

            disp_show2 = Button(newwin, text="Screen 1, 2:00p.m.- 4:30p.m.", fg="white", bg="red", width=30,
                                height=3, command= lambda: [show_time3(), Screen1()])
            disp_show2.place(x=70, y=170)


        def film_2(self):
            newwin = Toplevel(root)
            newwin.title('Available Shows')
            newwin.geometry("400x300")
            newwin.resizable(0, 0)

            global film_name
            film_name = "Weathering With You"

            disp_topper = Label(newwin, text="Shows available for 'Weathering With You'\n on " + self.date_disp.get() + " " +
                                self.month_disp.get() + ", " + self.day_disp.get() + " at " + hall, bg="grey", fg="white", height=3, width=50)
            disp_topper.pack()

            disp_show1 = Button(newwin, text="Screen 1, 11:15a.m.- 1:45p.m.", fg="white", bg="red", width=30,
                                height=3, command= lambda: [show_time2(), Screen1()])
            disp_show1.place(x=70, y=100)

            disp_show2 = Button(newwin, text="Screen 1, 4:45p.m.- 7:15p.m.", fg="white", bg="red", width=30,
                                height=3, command= lambda: [show_time4(), Screen1()])
            disp_show2.place(x=70, y=170)


        def film_3(self):
            newwin = Toplevel(root)
            newwin.title('Available Shows')
            newwin.geometry("400x300")
            newwin.resizable(0, 0)

            global film_name
            film_name = "Parasite"

            disp_topper = Label(newwin, text="Shows available for 'Parasite'\n on " + self.date_disp.get() + " " +
                                self.month_disp.get() + ", " + self.day_disp.get() + " at " + hall, bg="grey", fg="white", height=3, width=50)
            disp_topper.pack()

            disp_show1 = Button(newwin, text="Screen 2, 4:45p.m.- 7:15p.m.", fg="white", bg="red", width=30,
                                height=3, command= lambda: [show_time4(), Screen2()])
            disp_show1.place(x=70, y=100)


        def film_4(self):
            newwin = Toplevel(root)
            newwin.title('Available Shows')
            newwin.geometry("400x300")
            newwin.resizable(0, 0)

            global film_name
            film_name = "Toy Story 4"

            disp_topper = Label(newwin, text="Shows available for 'Toy Story 4'\n on " + self.date_disp.get() + " " +
                                self.month_disp.get() + ", " + self.day_disp.get() + " at " + hall, bg="grey", fg="white", height=3, width=50)
            disp_topper.pack()

            disp_show1 = Button(newwin, text="Screen 2, 8:30a.m.- 11:00a.m.", fg="white", bg="red", width=30,
                                height=3, command= lambda: [show_time1(), Screen2()])
            disp_show1.place(x=70, y=100)

            disp_show2 = Button(newwin, text="Screen 2, 2:00p.m.- 4:30p.m.", fg="white", bg="red", width=30,
                                height=3, command= lambda: [show_time3(), Screen2()])
            disp_show2.place(x=70, y=170)


        def film_5(self):
            newwin = Toplevel(root)
            newwin.title('Available Shows')
            newwin.geometry("400x300")
            newwin.resizable(0, 0)

            global film_name
            film_name = "Klaus"

            disp_topper = Label(newwin, text="Shows available for 'Klaus'\n on " + self.date_disp.get() + " " +
                                self.month_disp.get() + ", " + self.day_disp.get() + " at " + hall, bg="grey", fg="white", height=3, width=50)
            disp_topper.pack()

            disp_show1 = Button(newwin, text="Screen 2, 11:15a.m.- 1:45p.m.", fg="white", bg="red", width=30,
                                height=3, command= lambda: [show_time2(), Screen2()])
            disp_show1.place(x=70, y=100)

            disp_show2 = Button(newwin, text="Screen 2, 7:30p.m.- 10:00p.m.", fg="white", bg="red", width=30,
                                height=3, command= lambda: [show_time5(), Screen2()])
            disp_show2.place(x=70, y=170)


        def film_6(self):
            newwin = Toplevel(root)
            newwin.title('Available Shows')
            newwin.geometry("400x200")
            newwin.resizable(0, 0)

            global film_name
            film_name = "Interstellar"

            disp_topper = Label(newwin, text="Shows available for 'Interstellar'\n on " + self.date_disp.get() + " " +
                                self.month_disp.get() + ", " + self.day_disp.get() + " at " + hall, bg="grey", fg="white", height=3, width=50)
            disp_topper.pack()

            disp_show1 = Button(newwin, text="Screen 1, 7:30p.m.- 10:00p.m.", fg="white", bg="red", width=30,
                                height=3, command= lambda: [show_time5(), Screen1()])
            disp_show1.place(x=70, y=100)


        def show_time1():
            global show_time
            show_time = "8:30a.m.- 11:00a.m."


        def show_time2():
            global show_time
            show_time = "11:15a.m.- 1:45p.m."


        def show_time3():
            global show_time
            show_time = "2:00p.m.- 4:300p.m."


        def show_time4():
            global show_time
            show_time = "4:45p.m.- 7:15p.m."


        def show_time5():
            global show_time
            show_time = "7:30p.m.- 10:00p.m."


        def Screen1():
            global screen
            screen = "Screen 1"
            seat_booking()


        def Screen2():
            global screen
            screen = "Screen 2"
            seat_booking()



        def seat_booking():
            newwin = Toplevel(root)
            newwin.title('Seats Selection')
            newwin.geometry("815x600")
            newwin.resizable(0, 0)

            global var
            global price
            var = ""
            price = 0

            def Payment():
                newwin = Toplevel(root)
                newwin.title('Payment')
                newwin.geometry("400x480")
                newwin.resizable(0, 0)

                def close():
                    root.destroy()

                def final():
                    newwin = Toplevel(root)
                    newwin.title('Thank You!')
                    newwin.geometry("330x350")
                    newwin.resizable(0, 0)

                    lab_fin = Label(newwin, text="Transaction Successful! \n Amount: Rs."+"{:.2f}".format(total)+
                                            "\n From "+self.query.get()+"\n To Movie Booking System \n\n "+
                                                "Theatre: "+hall+"\n Movie: "+film_name+"\n"+screen+"\nOn "+self.date_disp.get()+
                                                 " "+self.month_disp.get()+", "+self.day_disp.get()+"\n Timing: "+show_time+
                                                "\n Seats Selected: "+var+"\n\n A copy of reciept and tickets has been sent to \n the E-Mail Address: "+
                                    self.query1.get(), fg="white", bg="grey", height=14, width=40)
                    lab_fin.place(x=20, y=30)

                    lab_fi = Label(newwin, text="Thank You! \nWe hope you are satisfied with our service.",
                                   fg="white", bg="red", height=3, width=40)
                    lab_fi.place(x=20, y=250)

                    end1 = Button(newwin, text="Close", command=close)
                    end1.place(x=140, y=310)

                def cr_dr():
                    nm_bk = Label(newwin, text="Name of Bank:", bg="red", fg="white", height=1, width=20)
                    nm_bk.place(x=20, y=260)

                    ent_1 = Entry(newwin, width=20)
                    ent_1.place(x=170, y=260)

                    nm_b = Label(newwin, text="Enter Card Number:", bg="red", fg="white", height=1, width=20)
                    nm_b.place(x=20, y=300)

                    ent_2 = Entry(newwin, width=20)
                    ent_2.place(x=170, y=300)

                    nm_bl = Label(newwin, text="Enter Card PIN:", bg="red", fg="white", height=1, width=20)
                    nm_bl.place(x=20, y=340)

                    ent_3 = Entry(newwin, width=20)
                    ent_3.place(x=170, y=340)

                    fin = Button(newwin, text="Confirm & Pay", command=final)
                    fin.place(x=150, y=375)

                    nm_b2 = Label(newwin,
                                  text="By confirming you agree the Terms \n and Conditions of ank_inc_mov_bk_sys",
                                  bg="grey", fg="white", height=3, width=50)
                    nm_b2.place(x=20, y=400)

                def net_bn():
                    nm_bk = Label(newwin, text="Name of Bank:", bg="red", fg="white", height=1, width=20)
                    nm_bk.place(x=20, y=260)

                    ent_1 = Entry(newwin, width=20)
                    ent_1.place(x=170, y=260)

                    nm_b = Label(newwin, text="Account No:", bg="red", fg="white", height=1, width=20)
                    nm_b.place(x=20, y=300)

                    ent_2 = Entry(newwin, width=20)
                    ent_2.place(x=170, y=300)

                    nm_bl = Label(newwin, text="Enter Security PIN:", bg="red", fg="white", height=1, width=20)
                    nm_bl.place(x=20, y=340)

                    ent_3 = Entry(newwin, width=20)
                    ent_3.place(x=170, y=340)

                    fin = Button(newwin, text="Confirm & Pay", command=final)
                    fin.place(x=150, y=375)

                    nm_b2 = Label(newwin,
                                  text="By confirming you agree the Terms \n and Conditions of ank_inc_mov_bk_sys",
                                  bg="grey", fg="white", height=3, width=50)
                    nm_b2.place(x=20, y=400)

                tax = 0.14*price
                total = price+tax+6.87

                pay_det = Label(newwin, text="Payment Summary", bg="red", fg="white", height=3, width=30)
                pay_det.pack()

                pay_summ = Label(newwin, text="Name of payer: "+self.query.get()+"\n\n Sub Total: Rs."+"{:.2f}".format(price)+
                                 "\n Handling fees: Rs.6.87 \n Service Tax @ 14%: Rs."+"{:.2f}".format(tax), bg="grey", fg="white",
                                 height=7, width=50)
                pay_summ.place(x=20, y=60)

                tot_sum = Label(newwin, text="Total amount to be paid: Rs."+"{:.2f}".format(total), bg="red", fg="white",
                                height=1, width=50)
                tot_sum.place(x=20, y=170)

                pay_1 = Button(newwin, text="Pay with Credit/Debit Card", command=cr_dr)
                pay_1.place(x=20, y=200)

                pay_2 = Button(newwin, text="Pay with Credit/Debit Card", command=net_bn)
                pay_2.place(x=220, y=200)

            def dis():
                newwin = Toplevel(root)
                newwin.title('Booking Details')
                newwin.geometry("400x300")
                newwin.resizable(0, 0)

                boo_det = Label(newwin, text="Booking Summary", bg="red", fg="white", height=3, width=30)
                boo_det.pack()

                book_detail = Label(newwin, text="Theatre: "+hall+"\n Movie: "+film_name+"\n"+screen+"\n Timing: "+show_time+
                                    "\n\n Seats Selected: "+var+"\n Price: Rs."+"{:.2f}".format(price), bg="grey", fg="white", height=7, width=40)
                book_detail.place(x=60, y=100)

                pay_butt = Button(newwin, text="Proceed to Payment", command=Payment)
                pay_butt.place(x=145, y=240)

                #print(var)
                #print(price)

            def on_click1():
                btn_1.configure(bg="grey")
                str2 = "K1"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click2():
                btn_2.configure(bg="grey")
                str2 = "K2"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click3():
                btn_3.configure(bg="grey")
                str2 = "K3"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click4():
                btn_4.configure(bg="grey")
                str2 = "K4"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click5():
                btn_5.configure(bg="grey")
                str2 = "K5"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click6():
                btn_6.configure(bg="grey")
                str2 = "K6"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click7():
                btn_7.configure(bg="grey")
                str2 = "K7"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click8():
                btn_8.configure(bg="grey")
                str2 = "K8"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click9():
                btn_9.configure(bg="grey")
                str2 = "K9"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click10():
                btn_10.configure(bg="grey")
                str2 = "K10"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click11():
                btn_11.configure(bg="grey")
                str2 = "K11"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click12():
                btn_12.configure(bg="grey")
                str2 = "K12"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click13():
                btn_13.configure(bg="grey")
                str2 = "K13"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click14():
                btn_14.configure(bg="grey")
                str2 = "K14"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click15():
                btn_15.configure(bg="grey")
                str2 = "K15"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click16():
                btn_16.configure(bg="grey")
                str2 = "K16"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click17():
                btn_17.configure(bg="grey")
                str2 = "K17"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click18():
                btn_18.configure(bg="grey")
                str2 = "K18"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click19():
                btn_19.configure(bg="grey")
                str2 = "K19"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click20():
                btn_20.configure(bg="grey")
                str2 = "K20"
                val = 250
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click21():
                btn_21.configure(bg="grey")
                str2 = "J1"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click22():
                btn_22.configure(bg="grey")
                str2 = "J2"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click23():
                btn_23.configure(bg="grey")
                str2 = "J3"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click24():
                btn_24.configure(bg="grey")
                str2 = "J4"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click25():
                btn_25.configure(bg="grey")
                str2 = "J5"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click26():
                btn_26.configure(bg="grey")
                str2 = "J6"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click27():
                btn_27.configure(bg="grey")
                str2 = "J7"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click28():
                btn_28.configure(bg="grey")
                str2 = "J8"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click29():
                btn_29.configure(bg="grey")
                str2 = "J9"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click30():
                btn_30.configure(bg="grey")
                str2 = "J10"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click31():
                btn_31.configure(bg="grey")
                str2 = "J11"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click32():
                btn_32.configure(bg="grey")
                str2 = "J12"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click33():
                btn_33.configure(bg="grey")
                str2 = "J13"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click34():
                btn_34.configure(bg="grey")
                str2 = "J14"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click35():
                btn_35.configure(bg="grey")
                str2 = "J15"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click36():
                btn_36.configure(bg="grey")
                str2 = "J16"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click37():
                btn_37.configure(bg="grey")
                str2 = "J17"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click38():
                btn_38.configure(bg="grey")
                str2 = "J18"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click39():
                btn_39.configure(bg="grey")
                str2 = "I1"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click40():
                btn_40.configure(bg="grey")
                str2 = "I2"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click41():
                btn_41.configure(bg="grey")
                str2 = "I3"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click42():
                btn_42.configure(bg="grey")
                str2 = "I4"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click43():
                btn_43.configure(bg="grey")
                str2 = "I5"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click44():
                btn_44.configure(bg="grey")
                str2 = "I6"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click45():
                btn_45.configure(bg="grey")
                str2 = "I7"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click46():
                btn_46.configure(bg="grey")
                str2 = "I8"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click47():
                btn_47.configure(bg="grey")
                str2 = "I9"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click48():
                btn_48.configure(bg="grey")
                str2 = "I10"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click49():
                btn_49.configure(bg="grey")
                str2 = "I11"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click50():
                btn_50.configure(bg="grey")
                str2 = "I12"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click51():
                btn_51.configure(bg="grey")
                str2 = "I13"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click52():
                btn_52.configure(bg="grey")
                str2 = "I14"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click53():
                btn_53.configure(bg="grey")
                str2 = "I15"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click54():
                btn_54.configure(bg="grey")
                str2 = "I16"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click55():
                btn_55.configure(bg="grey")
                str2 = "I17"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click56():
                btn_56.configure(bg="grey")
                str2 = "I18"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click57():
                btn_57.configure(bg="grey")
                str2 = "H1"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click58():
                btn_58.configure(bg="grey")
                str2 = "H2"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click59():
                btn_59.configure(bg="grey")
                str2 = "H3"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click60():
                btn_60.configure(bg="grey")
                str2 = "H4"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click61():
                btn_61.configure(bg="grey")
                str2 = "H5"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click62():
                btn_62.configure(bg="grey")
                str2 = "H6"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click63():
                btn_63.configure(bg="grey")
                str2 = "H7"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click64():
                btn_64.configure(bg="grey")
                str2 = "H8"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click65():
                btn_65.configure(bg="grey")
                str2 = "H9"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click66():
                btn_66.configure(bg="grey")
                str2 = "H10"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click67():
                btn_67.configure(bg="grey")
                str2 = "H11"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click68():
                btn_68.configure(bg="grey")
                str2 = "H12"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click69():
                btn_69.configure(bg="grey")
                str2 = "H13"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click70():
                btn_70.configure(bg="grey")
                str2 = "H14"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click71():
                btn_71.configure(bg="grey")
                str2 = "H15"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click72():
                btn_72.configure(bg="grey")
                str2 = "H16"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click73():
                btn_73.configure(bg="grey")
                str2 = "H17"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click74():
                btn_74.configure(bg="grey")
                str2 = "H18"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click75():
                btn_75.configure(bg="grey")
                str2 = "G1"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click76():
                btn_76.configure(bg="grey")
                str2 = "G2"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click77():
                btn_77.configure(bg="grey")
                str2 = "G3"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click78():
                btn_78.configure(bg="grey")
                str2 = "G4"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click79():
                btn_79.configure(bg="grey")
                str2 = "G5"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click80():
                btn_80.configure(bg="grey")
                str2 = "G6"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click81():
                btn_81.configure(bg="grey")
                str2 = "G7"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click82():
                btn_82.configure(bg="grey")
                str2 = "G8"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click83():
                btn_83.configure(bg="grey")
                str2 = "G9"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click84():
                btn_84.configure(bg="grey")
                str2 = "G10"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click85():
                btn_85.configure(bg="grey")
                str2 = "G11"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click86():
                btn_86.configure(bg="grey")
                str2 = "G12"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click87():
                btn_87.configure(bg="grey")
                str2 = "G13"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click88():
                btn_88.configure(bg="grey")
                str2 = "G14"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click89():
                btn_89.configure(bg="grey")
                str2 = "G15"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click90():
                btn_90.configure(bg="grey")
                str2 = "G16"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click91():
                btn_91.configure(bg="grey")
                str2 = "G17"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click92():
                btn_92.configure(bg="grey")
                str2 = "G18"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click93():
                btn_93.configure(bg="grey")
                str2 = "F1"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click94():
                btn_94.configure(bg="grey")
                str2 = "F2"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click95():
                btn_95.configure(bg="grey")
                str2 = "F3"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click96():
                btn_96.configure(bg="grey")
                str2 = "F4"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click97():
                btn_97.configure(bg="grey")
                str2 = "F5"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click98():
                btn_98.configure(bg="grey")
                str2 = "F6"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click99():
                btn_99.configure(bg="grey")
                str2 = "F7"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click100():
                btn_100.configure(bg="grey")
                str2 = "F8"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click101():
                btn_101.configure(bg="grey")
                str2 = "F9"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click102():
                btn_102.configure(bg="grey")
                str2 = "F10"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click103():
                btn_103.configure(bg="grey")
                str2 = "F11"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click104():
                btn_104.configure(bg="grey")
                str2 = "F12"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click105():
                btn_105.configure(bg="grey")
                str2 = "F13"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click106():
                btn_106.configure(bg="grey")
                str2 = "F14"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click107():
                btn_107.configure(bg="grey")
                str2 = "F15"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click108():
                btn_108.configure(bg="grey")
                str2 = "F16"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click109():
                btn_109.configure(bg="grey")
                str2 = "F17"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click110():
                btn_110.configure(bg="grey")
                str2 = "F18"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click111():
                btn_111.configure(bg="grey")
                str2 = "E1"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click112():
                btn_112.configure(bg="grey")
                str2 = "E2"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click113():
                btn_113.configure(bg="grey")
                str2 = "E3"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click114():
                btn_114.configure(bg="grey")
                str2 = "E4"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click115():
                btn_115.configure(bg="grey")
                str2 = "E5"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click116():
                btn_116.configure(bg="grey")
                str2 = "E6"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click117():
                btn_117.configure(bg="grey")
                str2 = "E7"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click118():
                btn_118.configure(bg="grey")
                str2 = "E8"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click119():
                btn_119.configure(bg="grey")
                str2 = "E9"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click120():
                btn_120.configure(bg="grey")
                str2 = "E10"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click121():
                btn_121.configure(bg="grey")
                str2 = "E11"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click122():
                btn_122.configure(bg="grey")
                str2 = "E12"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click123():
                btn_123.configure(bg="grey")
                str2 = "E13"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click124():
                btn_124.configure(bg="grey")
                str2 = "E14"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click125():
                btn_125.configure(bg="grey")
                str2 = "E15"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click126():
                btn_126.configure(bg="grey")
                str2 = "E16"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click127():
                btn_127.configure(bg="grey")
                str2 = "E17"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click128():
                btn_128.configure(bg="grey")
                str2 = "E18"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click129():
                btn_129.configure(bg="grey")
                str2 = "D1"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click130():
                btn_130.configure(bg="grey")
                str2 = "D2"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click131():
                btn_131.configure(bg="grey")
                str2 = "D3"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click132():
                btn_132.configure(bg="grey")
                str2 = "D4"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click133():
                btn_133.configure(bg="grey")
                str2 = "D5"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click134():
                btn_134.configure(bg="grey")
                str2 = "D6"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click135():
                btn_135.configure(bg="grey")
                str2 = "D7"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click136():
                btn_136.configure(bg="grey")
                str2 = "D8"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click137():
                btn_137.configure(bg="grey")
                str2 = "D9"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click138():
                btn_138.configure(bg="grey")
                str2 = "D10"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click139():
                btn_139.configure(bg="grey")
                str2 = "D11"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click140():
                btn_140.configure(bg="grey")
                str2 = "D12"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click141():
                btn_141.configure(bg="grey")
                str2 = "D13"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click142():
                btn_142.configure(bg="grey")
                str2 = "D14"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click143():
                btn_143.configure(bg="grey")
                str2 = "D15"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click144():
                btn_144.configure(bg="grey")
                str2 = "D16"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click145():
                btn_145.configure(bg="grey")
                str2 = "D17"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click146():
                btn_146.configure(bg="grey")
                str2 = "D18"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click147():
                btn_147.configure(bg="grey")
                str2 = "C1"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click148():
                btn_148.configure(bg="grey")
                str2 = "C2"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click149():
                btn_149.configure(bg="grey")
                str2 = "C3"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click150():
                btn_150.configure(bg="grey")
                str2 = "C4"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click151():
                btn_151.configure(bg="grey")
                str2 = "C5"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click152():
                btn_152.configure(bg="grey")
                str2 = "C6"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click153():
                btn_153.configure(bg="grey")
                str2 = "C7"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click154():
                btn_154.configure(bg="grey")
                str2 = "C8"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click155():
                btn_155.configure(bg="grey")
                str2 = "C9"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click156():
                btn_156.configure(bg="grey")
                str2 = "C10"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click157():
                btn_157.configure(bg="grey")
                str2 = "C11"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click158():
                btn_158.configure(bg="grey")
                str2 = "C12"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click159():
                btn_159.configure(bg="grey")
                str2 = "C13"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click160():
                btn_160.configure(bg="grey")
                str2 = "C14"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click161():
                btn_161.configure(bg="grey")
                str2 = "C15"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click162():
                btn_162.configure(bg="grey")
                str2 = "C16"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click163():
                btn_163.configure(bg="grey")
                str2 = "C17"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click164():
                btn_164.configure(bg="grey")
                str2 = "C18"
                val = 190
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click165():
                btn_165.configure(bg="grey")
                str2 = "B1"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click166():
                btn_166.configure(bg="grey")
                str2 = "B2"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click167():
                btn_167.configure(bg="grey")
                str2 = "B3"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click168():
                btn_168.configure(bg="grey")
                str2 = "B4"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click169():
                btn_169.configure(bg="grey")
                str2 = "B5"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click170():
                btn_170.configure(bg="grey")
                str2 = "B6"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click171():
                btn_171.configure(bg="grey")
                str2 = "B7"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click172():
                btn_172.configure(bg="grey")
                str2 = "B8"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click173():
                btn_173.configure(bg="grey")
                str2 = "B9"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click174():
                btn_174.configure(bg="grey")
                str2 = "B10"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click175():
                btn_175.configure(bg="grey")
                str2 = "B11"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click176():
                btn_176.configure(bg="grey")
                str2 = "B12"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click177():
                btn_177.configure(bg="grey")
                str2 = "B13"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click178():
                btn_178.configure(bg="grey")
                str2 = "B14"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click179():
                btn_179.configure(bg="grey")
                str2 = "B15"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click180():
                btn_180.configure(bg="grey")
                str2 = "B16"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click181():
                btn_181.configure(bg="grey")
                str2 = "B17"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click182():
                btn_182.configure(bg="grey")
                str2 = "B18"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click183():
                btn_183.configure(bg="grey")
                str2 = "A1"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click184():
                btn_184.configure(bg="grey")
                str2 = "A2"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click185():
                btn_185.configure(bg="grey")
                str2 = "A3"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click186():
                btn_186.configure(bg="grey")
                str2 = "A4"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click187():
                btn_187.configure(bg="grey")
                str2 = "A5"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click188():
                btn_188.configure(bg="grey")
                str2 = "A6"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click189():
                btn_189.configure(bg="grey")
                str2 = "A7"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click190():
                btn_190.configure(bg="grey")
                str2 = "A8"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click191():
                btn_191.configure(bg="grey")
                str2 = "A9"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click192():
                btn_192.configure(bg="grey")
                str2 = "A10"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click193():
                btn_193.configure(bg="grey")
                str2 = "A11"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click194():
                btn_194.configure(bg="grey")
                str2 = "A12"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click195():
                btn_195.configure(bg="grey")
                str2 = "A13"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click196():
                btn_196.configure(bg="grey")
                str2 = "A14"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click197():
                btn_197.configure(bg="grey")
                str2 = "A15"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click198():
                btn_198.configure(bg="grey")
                str2 = "A16"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click199():
                btn_199.configure(bg="grey")
                str2 = "A17"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            def on_click200():
                btn_200.configure(bg="grey")
                str2 = "A18"
                val = 150
                global var
                global price
                var = var + str2 + " "
                price = price + val

            dis_head = Label(newwin, text="Select seats for " + film_name + "\n" + show_time + "  " + screen,
                             bg="grey", fg="white", height=3, width=70)
            dis_head.pack()

            btn_1 = Button(newwin, text="K1", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click1()])
            btn_1.place(x=10, y=60)

            btn_2 = Button(newwin, text="K2", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click2()])
            btn_2.place(x=50, y=60)

            btn_3 = Button(newwin, text="K3", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click3()])
            btn_3.place(x=90, y=60)

            btn_4 = Button(newwin, text="K4", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click4()])
            btn_4.place(x=130, y=60)

            btn_5 = Button(newwin, text="K5", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click5()])
            btn_5.place(x=170, y=60)

            btn_6 = Button(newwin, text="K6", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click6()])
            btn_6.place(x=210, y=60)

            btn_7 = Button(newwin, text="K7", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click7()])
            btn_7.place(x=250, y=60)

            btn_8 = Button(newwin, text="K8", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click8()])
            btn_8.place(x=290, y=60)

            btn_9 = Button(newwin, text="K9", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click9()])
            btn_9.place(x=330, y=60)

            btn_10 = Button(newwin, text="K10", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click10()])
            btn_10.place(x=370, y=60)

            btn_11 = Button(newwin, text="K11", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click11()])
            btn_11.place(x=410, y=60)

            btn_12 = Button(newwin, text="K12", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click12()])
            btn_12.place(x=450, y=60)

            btn_13 = Button(newwin, text="K13", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click13()])
            btn_13.place(x=490, y=60)

            btn_14 = Button(newwin, text="K14", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click14()])
            btn_14.place(x=530, y=60)

            btn_15 = Button(newwin, text="K15", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click15()])
            btn_15.place(x=570, y=60)

            btn_16 = Button(newwin, text="K16", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click16()])
            btn_16.place(x=610, y=60)

            btn_17 = Button(newwin, text="K17", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click17()])
            btn_17.place(x=650, y=60)

            btn_18 = Button(newwin, text="K18", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click18()])
            btn_18.place(x=690, y=60)

            btn_19 = Button(newwin, text="K19", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click19()])
            btn_19.place(x=730, y=60)

            btn_20 = Button(newwin, text="K20", bg="blue", fg="white", height=1, width=3, command= lambda : [on_click20()])
            btn_20.place(x=770, y=60)

            btn_21 = Button(newwin, text="J1", bg="green", fg="white", height=1, width=3, command= lambda : [on_click21()])
            btn_21.place(x=10, y=90)

            btn_22 = Button(newwin, text="J2", bg="green", fg="white", height=1, width=3, command=lambda: [on_click22()])
            btn_22.place(x=50, y=90)

            btn_23 = Button(newwin, text="J3", bg="green", fg="white", height=1, width=3, command=lambda: [on_click23()])
            btn_23.place(x=90, y=90)

            btn_24 = Button(newwin, text="J4", bg="green", fg="white", height=1, width=3, command=lambda: [on_click24()])
            btn_24.place(x=130, y=90)

            btn_25 = Button(newwin, text="J5", bg="green", fg="white", height=1, width=3, command=lambda: [on_click25()])
            btn_25.place(x=170, y=90)

            btn_26 = Button(newwin, text="J6", bg="green", fg="white", height=1, width=3, command=lambda: [on_click26()])
            btn_26.place(x=210, y=90)

            btn_27 = Button(newwin, text="J7", bg="green", fg="white", height=1, width=3, command=lambda: [on_click27()])
            btn_27.place(x=250, y=90)

            btn_28 = Button(newwin, text="J8", bg="green", fg="white", height=1, width=3, command=lambda: [on_click28()])
            btn_28.place(x=290, y=90)

            btn_29 = Button(newwin, text="J9", bg="green", fg="white", height=1, width=3, command=lambda: [on_click29()])
            btn_29.place(x=330, y=90)

            btn_30 = Button(newwin, text="J10", bg="green", fg="white", height=1, width=3, command=lambda: [on_click30()])
            btn_30.place(x=450, y=90)

            btn_31 = Button(newwin, text="J11", bg="green", fg="white", height=1, width=3, command=lambda: [on_click31()])
            btn_31.place(x=490, y=90)

            btn_32 = Button(newwin, text="J12", bg="green", fg="white", height=1, width=3, command=lambda: [on_click32()])
            btn_32.place(x=530, y=90)

            btn_33 = Button(newwin, text="J13", bg="green", fg="white", height=1, width=3, command=lambda: [on_click33()])
            btn_33.place(x=570, y=90)

            btn_34 = Button(newwin, text="J14", bg="green", fg="white", height=1, width=3, command=lambda: [on_click34()])
            btn_34.place(x=610, y=90)

            btn_35 = Button(newwin, text="J15", bg="green", fg="white", height=1, width=3, command=lambda: [on_click35()])
            btn_35.place(x=650, y=90)

            btn_36 = Button(newwin, text="J16", bg="green", fg="white", height=1, width=3, command=lambda: [on_click36()])
            btn_36.place(x=690, y=90)

            btn_37 = Button(newwin, text="J17", bg="green", fg="white", height=1, width=3, command=lambda: [on_click37()])
            btn_37.place(x=730, y=90)

            btn_38 = Button(newwin, text="J18", bg="green", fg="white", height=1, width=3, command=lambda: [on_click38()])
            btn_38.place(x=770, y=90)

            btn_39 = Button(newwin, text="I1", bg="green", fg="white", height=1, width=3, command=lambda: [on_click39()])
            btn_39.place(x=10, y=120)

            btn_40 = Button(newwin, text="I2", bg="green", fg="white", height=1, width=3, command=lambda: [on_click40()])
            btn_40.place(x=50, y=120)

            btn_41 = Button(newwin, text="I3", bg="green", fg="white", height=1, width=3, command=lambda: [on_click41()])
            btn_41.place(x=90, y=120)

            btn_42 = Button(newwin, text="I4", bg="green", fg="white", height=1, width=3, command=lambda: [on_click42()])
            btn_42.place(x=130, y=120)

            btn_43 = Button(newwin, text="I5", bg="green", fg="white", height=1, width=3, command=lambda: [on_click43()])
            btn_43.place(x=170, y=120)

            btn_44 = Button(newwin, text="I6", bg="green", fg="white", height=1, width=3, command=lambda: [on_click44()])
            btn_44.place(x=210, y=120)

            btn_45 = Button(newwin, text="I7", bg="green", fg="white", height=1, width=3, command=lambda: [on_click45()])
            btn_45.place(x=250, y=120)

            btn_46 = Button(newwin, text="I8", bg="green", fg="white", height=1, width=3, command=lambda: [on_click46()])
            btn_46.place(x=290, y=120)

            btn_47 = Button(newwin, text="I9", bg="green", fg="white", height=1, width=3, command=lambda: [on_click47()])
            btn_47.place(x=330, y=120)

            btn_48 = Button(newwin, text="I10", bg="green", fg="white", height=1, width=3, command=lambda: [on_click48()])
            btn_48.place(x=450, y=120)

            btn_49 = Button(newwin, text="I11", bg="green", fg="white", height=1, width=3, command=lambda: [on_click49()])
            btn_49.place(x=490, y=120)

            btn_50 = Button(newwin, text="I12", bg="green", fg="white", height=1, width=3, command=lambda: [on_click50()])
            btn_50.place(x=530, y=120)

            btn_51 = Button(newwin, text="I13", bg="green", fg="white", height=1, width=3, command=lambda: [on_click51()])
            btn_51.place(x=570, y=120)

            btn_52 = Button(newwin, text="I14", bg="green", fg="white", height=1, width=3, command=lambda: [on_click52()])
            btn_52.place(x=610, y=120)

            btn_53 = Button(newwin, text="I15", bg="green", fg="white", height=1, width=3, command=lambda: [on_click53()])
            btn_53.place(x=650, y=120)

            btn_54 = Button(newwin, text="I16", bg="green", fg="white", height=1, width=3, command=lambda: [on_click54()])
            btn_54.place(x=690, y=120)

            btn_55 = Button(newwin, text="I17", bg="green", fg="white", height=1, width=3, command=lambda: [on_click55()])
            btn_55.place(x=730, y=120)

            btn_56 = Button(newwin, text="I18", bg="green", fg="white", height=1, width=3, command=lambda: [on_click56()])
            btn_56.place(x=770, y=120)

            btn_57 = Button(newwin, text="H1", bg="green", fg="white", height=1, width=3, command=lambda: [on_click57()])
            btn_57.place(x=10, y=150)

            btn_58 = Button(newwin, text="H2", bg="green", fg="white", height=1, width=3, command=lambda: [on_click58()])
            btn_58.place(x=50, y=150)

            btn_59 = Button(newwin, text="H3", bg="green", fg="white", height=1, width=3, command=lambda: [on_click59()])
            btn_59.place(x=90, y=150)

            btn_60 = Button(newwin, text="H4", bg="green", fg="white", height=1, width=3, command=lambda: [on_click60()])
            btn_60.place(x=130, y=150)

            btn_61 = Button(newwin, text="H5", bg="green", fg="white", height=1, width=3, command=lambda: [on_click61()])
            btn_61.place(x=170, y=150)

            btn_62 = Button(newwin, text="H6", bg="green", fg="white", height=1, width=3, command=lambda: [on_click62()])
            btn_62.place(x=210, y=150)

            btn_63 = Button(newwin, text="H7", bg="green", fg="white", height=1, width=3, command=lambda: [on_click63()])
            btn_63.place(x=250, y=150)

            btn_64 = Button(newwin, text="H8", bg="green", fg="white", height=1, width=3, command=lambda: [on_click64()])
            btn_64.place(x=290, y=150)

            btn_65 = Button(newwin, text="H9", bg="green", fg="white", height=1, width=3, command=lambda: [on_click65()])
            btn_65.place(x=330, y=150)

            btn_66 = Button(newwin, text="H10", bg="green", fg="white", height=1, width=3, command=lambda: [on_click66()])
            btn_66.place(x=450, y=150)

            btn_67 = Button(newwin, text="H11", bg="green", fg="white", height=1, width=3, command=lambda: [on_click67()])
            btn_67.place(x=490, y=150)

            btn_68 = Button(newwin, text="H12", bg="green", fg="white", height=1, width=3, command=lambda: [on_click68()])
            btn_68.place(x=530, y=150)

            btn_69 = Button(newwin, text="H13", bg="green", fg="white", height=1, width=3, command=lambda: [on_click69()])
            btn_69.place(x=570, y=150)

            btn_70 = Button(newwin, text="H14", bg="green", fg="white", height=1, width=3, command=lambda: [on_click70()])
            btn_70.place(x=610, y=150)

            btn_71 = Button(newwin, text="H15", bg="green", fg="white", height=1, width=3, command=lambda: [on_click71()])
            btn_71.place(x=650, y=150)

            btn_72 = Button(newwin, text="H16", bg="green", fg="white", height=1, width=3, command=lambda: [on_click72()])
            btn_72.place(x=690, y=150)

            btn_73 = Button(newwin, text="H17", bg="green", fg="white", height=1, width=3, command=lambda: [on_click73()])
            btn_73.place(x=730, y=150)

            btn_74 = Button(newwin, text="H18", bg="green", fg="white", height=1, width=3, command=lambda: [on_click74()])
            btn_74.place(x=770, y=150)

            btn_75 = Button(newwin, text="G1", bg="green", fg="white", height=1, width=3, command=lambda: [on_click75()])
            btn_75.place(x=10, y=180)

            btn_76 = Button(newwin, text="G2", bg="green", fg="white", height=1, width=3, command=lambda: [on_click76()])
            btn_76.place(x=50, y=180)

            btn_77 = Button(newwin, text="G3", bg="green", fg="white", height=1, width=3, command=lambda: [on_click77()])
            btn_77.place(x=90, y=180)

            btn_78 = Button(newwin, text="G4", bg="green", fg="white", height=1, width=3, command=lambda: [on_click78()])
            btn_78.place(x=130, y=180)

            btn_79 = Button(newwin, text="G5", bg="green", fg="white", height=1, width=3, command=lambda: [on_click79()])
            btn_79.place(x=170, y=180)

            btn_80 = Button(newwin, text="G6", bg="green", fg="white", height=1, width=3, command=lambda: [on_click80()])
            btn_80.place(x=210, y=180)

            btn_81 = Button(newwin, text="G7", bg="green", fg="white", height=1, width=3, command=lambda: [on_click81()])
            btn_81.place(x=250, y=180)

            btn_82 = Button(newwin, text="G8", bg="green", fg="white", height=1, width=3, command=lambda: [on_click82()])
            btn_82.place(x=290, y=180)

            btn_83 = Button(newwin, text="G9", bg="green", fg="white", height=1, width=3, command=lambda: [on_click83()])
            btn_83.place(x=330, y=180)

            btn_84 = Button(newwin, text="G10", bg="green", fg="white", height=1, width=3, command=lambda: [on_click84()])
            btn_84.place(x=450, y=180)

            btn_85 = Button(newwin, text="G11", bg="green", fg="white", height=1, width=3, command=lambda: [on_click85()])
            btn_85.place(x=490, y=180)

            btn_86 = Button(newwin, text="G12", bg="green", fg="white", height=1, width=3, command=lambda: [on_click86()])
            btn_86.place(x=530, y=180)

            btn_87 = Button(newwin, text="G13", bg="green", fg="white", height=1, width=3, command=lambda: [on_click87()])
            btn_87.place(x=570, y=180)

            btn_88 = Button(newwin, text="G14", bg="green", fg="white", height=1, width=3, command=lambda: [on_click88()])
            btn_88.place(x=610, y=180)

            btn_89 = Button(newwin, text="G15", bg="green", fg="white", height=1, width=3,  command=lambda: [on_click89()])
            btn_89.place(x=650, y=180)

            btn_90 = Button(newwin, text="G16", bg="green", fg="white", height=1, width=3, command=lambda: [on_click90()])
            btn_90.place(x=690, y=180)

            btn_91 = Button(newwin, text="G17", bg="green", fg="white", height=1, width=3, command=lambda: [on_click91()])
            btn_91.place(x=730, y=180)

            btn_92 = Button(newwin, text="G18", bg="green", fg="white", height=1, width=3, command=lambda: [on_click92()])
            btn_92.place(x=770, y=180)

            btn_93 = Button(newwin, text="F1", bg="green", fg="white", height=1, width=3, command=lambda: [on_click93()])
            btn_93.place(x=10, y=210)

            btn_94 = Button(newwin, text="F2", bg="green", fg="white", height=1, width=3, command=lambda: [on_click94()])
            btn_94.place(x=50, y=210)

            btn_95 = Button(newwin, text="G3", bg="green", fg="white", height=1, width=3, command=lambda: [on_click95()])
            btn_95.place(x=90, y=210)

            btn_96 = Button(newwin, text="F4", bg="green", fg="white", height=1, width=3, command=lambda: [on_click96()])
            btn_96.place(x=130, y=210)

            btn_97 = Button(newwin, text="F5", bg="green", fg="white", height=1, width=3, command=lambda: [on_click97()])
            btn_97.place(x=170, y=210)

            btn_98 = Button(newwin, text="F6", bg="green", fg="white", height=1, width=3, command=lambda: [on_click98()])
            btn_98.place(x=210, y=210)

            btn_99 = Button(newwin, text="F7", bg="green", fg="white", height=1, width=3, command=lambda: [on_click99()])
            btn_99.place(x=250, y=210)

            btn_100 = Button(newwin, text="F8", bg="green", fg="white", height=1, width=3, command=lambda: [on_click100()])
            btn_100.place(x=290, y=210)

            btn_101 = Button(newwin, text="F9", bg="green", fg="white", height=1, width=3, command=lambda: [on_click101()])
            btn_101.place(x=330, y=210)

            btn_102 = Button(newwin, text="F10", bg="green", fg="white", height=1, width=3, command=lambda: [on_click102()])
            btn_102.place(x=450, y=210)

            btn_103 = Button(newwin, text="F11", bg="green", fg="white", height=1, width=3, command=lambda: [on_click103()])
            btn_103.place(x=490, y=210)

            btn_104 = Button(newwin, text="F12", bg="green", fg="white", height=1, width=3, command=lambda: [on_click104()])
            btn_104.place(x=530, y=210)

            btn_105 = Button(newwin, text="F13", bg="green", fg="white", height=1, width=3, command=lambda: [on_click105()])
            btn_105.place(x=570, y=210)

            btn_106 = Button(newwin, text="F14", bg="green", fg="white", height=1, width=3, command=lambda: [on_click106()])
            btn_106.place(x=610, y=210)

            btn_107 = Button(newwin, text="F15", bg="green", fg="white", height=1, width=3, command=lambda: [on_click107()])
            btn_107.place(x=650, y=210)

            btn_108 = Button(newwin, text="F16", bg="green", fg="white", height=1, width=3, command=lambda: [on_click108()])
            btn_108.place(x=690, y=210)

            btn_109 = Button(newwin, text="F17", bg="green", fg="white", height=1, width=3, command=lambda: [on_click109()])
            btn_109.place(x=730, y=210)

            btn_110 = Button(newwin, text="F18", bg="green", fg="white", height=1, width=3, command=lambda: [on_click110()])
            btn_110.place(x=770, y=210)

            btn_111 = Button(newwin, text="E1", bg="green", fg="white", height=1, width=3, command=lambda: [on_click111()])
            btn_111.place(x=10, y=240)

            btn_112 = Button(newwin, text="E2", bg="green", fg="white", height=1, width=3, command=lambda: [on_click112()])
            btn_112.place(x=50, y=240)

            btn_113 = Button(newwin, text="E3", bg="green", fg="white", height=1, width=3, command=lambda: [on_click113()])
            btn_113.place(x=90, y=240)

            btn_114 = Button(newwin, text="E4", bg="green", fg="white", height=1, width=3, command=lambda: [on_click114()])
            btn_114.place(x=130, y=240)

            btn_115 = Button(newwin, text="E5", bg="green", fg="white", height=1, width=3, command=lambda: [on_click115()])
            btn_115.place(x=170, y=240)

            btn_116 = Button(newwin, text="E6", bg="green", fg="white", height=1, width=3, command=lambda: [on_click116()])
            btn_116.place(x=210, y=240)

            btn_117 = Button(newwin, text="E7", bg="green", fg="white", height=1, width=3, command=lambda: [on_click117()])
            btn_117.place(x=250, y=240)

            btn_118 = Button(newwin, text="E8", bg="green", fg="white", height=1, width=3, command=lambda: [on_click118()])
            btn_118.place(x=290, y=240)

            btn_119 = Button(newwin, text="E9", bg="green", fg="white", height=1, width=3, command=lambda: [on_click119()])
            btn_119.place(x=330, y=240)

            btn_120 = Button(newwin, text="E10", bg="green", fg="white", height=1, width=3, command=lambda: [on_click120()])
            btn_120.place(x=450, y=240)

            btn_121 = Button(newwin, text="E11", bg="green", fg="white", height=1, width=3, command=lambda: [on_click121()])
            btn_121.place(x=490, y=240)

            btn_122 = Button(newwin, text="E12", bg="green", fg="white", height=1, width=3, command=lambda: [on_click122()])
            btn_122.place(x=530, y=240)

            btn_123 = Button(newwin, text="E13", bg="green", fg="white", height=1, width=3, command=lambda: [on_click123()])
            btn_123.place(x=570, y=240)

            btn_124 = Button(newwin, text="E14", bg="green", fg="white", height=1, width=3, command=lambda: [on_click124()])
            btn_124.place(x=610, y=240)

            btn_125 = Button(newwin, text="E15", bg="green", fg="white", height=1, width=3, command=lambda: [on_click125()])
            btn_125.place(x=650, y=240)

            btn_126 = Button(newwin, text="E16", bg="green", fg="white", height=1, width=3, command=lambda: [on_click126()])
            btn_126.place(x=690, y=240)

            btn_127 = Button(newwin, text="E17", bg="green", fg="white", height=1, width=3, command=lambda: [on_click127()])
            btn_127.place(x=730, y=240)

            btn_128 = Button(newwin, text="E18", bg="green", fg="white", height=1, width=3, command=lambda: [on_click128()])
            btn_128.place(x=770, y=240)

            btn_129 = Button(newwin, text="D1", bg="green", fg="white", height=1, width=3, command=lambda: [on_click129()])
            btn_129.place(x=10, y=270)

            btn_130 = Button(newwin, text="D2", bg="green", fg="white", height=1, width=3, command=lambda: [on_click130()])
            btn_130.place(x=50, y=270)

            btn_131 = Button(newwin, text="D3", bg="green", fg="white", height=1, width=3, command=lambda: [on_click131()])
            btn_131.place(x=90, y=270)

            btn_132 = Button(newwin, text="D4", bg="green", fg="white", height=1, width=3, command=lambda: [on_click132()])
            btn_132.place(x=130, y=270)

            btn_133 = Button(newwin, text="D5", bg="green", fg="white", height=1, width=3, command=lambda: [on_click133()])
            btn_133.place(x=170, y=270)

            btn_134 = Button(newwin, text="D6", bg="green", fg="white", height=1, width=3, command=lambda: [on_click134()])
            btn_134.place(x=210, y=270)

            btn_135 = Button(newwin, text="D7", bg="green", fg="white", height=1, width=3, command=lambda: [on_click135()])
            btn_135.place(x=250, y=270)

            btn_136 = Button(newwin, text="D8", bg="green", fg="white", height=1, width=3, command=lambda: [on_click136()])
            btn_136.place(x=290, y=270)

            btn_137 = Button(newwin, text="D9", bg="green", fg="white", height=1, width=3, command=lambda: [on_click137()])
            btn_137.place(x=330, y=270)

            btn_138 = Button(newwin, text="D10", bg="green", fg="white", height=1, width=3, command=lambda: [on_click138()])
            btn_138.place(x=450, y=270)

            btn_139 = Button(newwin, text="D11", bg="green", fg="white", height=1, width=3, command=lambda: [on_click139()])
            btn_139.place(x=490, y=270)

            btn_140 = Button(newwin, text="D12", bg="green", fg="white", height=1, width=3, command=lambda: [on_click140()])
            btn_140.place(x=530, y=270)

            btn_141 = Button(newwin, text="D13", bg="green", fg="white", height=1, width=3, command=lambda: [on_click141()])
            btn_141.place(x=570, y=270)

            btn_142 = Button(newwin, text="D14", bg="green", fg="white", height=1, width=3, command=lambda: [on_click142()])
            btn_142.place(x=610, y=270)

            btn_143 = Button(newwin, text="D15", bg="green", fg="white", height=1, width=3, command=lambda: [on_click143()])
            btn_143.place(x=650, y=270)

            btn_144 = Button(newwin, text="D16", bg="green", fg="white", height=1, width=3, command=lambda: [on_click144()])
            btn_144.place(x=690, y=270)

            btn_145 = Button(newwin, text="D17", bg="green", fg="white", height=1, width=3, command=lambda: [on_click145()])
            btn_145.place(x=730, y=270)

            btn_146 = Button(newwin, text="D18", bg="green", fg="white", height=1, width=3, command=lambda: [on_click146()])
            btn_146.place(x=770, y=270)

            btn_147 = Button(newwin, text="C1", bg="green", fg="white", height=1, width=3, command=lambda: [on_click147()])
            btn_147.place(x=10, y=300)

            btn_148 = Button(newwin, text="C2", bg="green", fg="white", height=1, width=3, command=lambda: [on_click148()])
            btn_148.place(x=50, y=300)

            btn_149 = Button(newwin, text="C3", bg="green", fg="white", height=1, width=3, command=lambda: [on_click149()])
            btn_149.place(x=90, y=300)

            btn_150 = Button(newwin, text="C4", bg="green", fg="white", height=1, width=3, command=lambda: [on_click150()])
            btn_150.place(x=130, y=300)

            btn_151 = Button(newwin, text="C5", bg="green", fg="white", height=1, width=3, command=lambda: [on_click151()])
            btn_151.place(x=170, y=300)

            btn_152 = Button(newwin, text="C6", bg="green", fg="white", height=1, width=3, command=lambda: [on_click152()])
            btn_152.place(x=210, y=300)

            btn_153 = Button(newwin, text="C7", bg="green", fg="white", height=1, width=3, command=lambda: [on_click153()])
            btn_153.place(x=250, y=300)

            btn_154 = Button(newwin, text="C8", bg="green", fg="white", height=1, width=3, command=lambda: [on_click154()])
            btn_154.place(x=290, y=300)

            btn_155 = Button(newwin, text="C9", bg="green", fg="white", height=1, width=3, command=lambda: [on_click155()])
            btn_155.place(x=330, y=300)

            btn_156 = Button(newwin, text="C10", bg="green", fg="white", height=1, width=3, command=lambda: [on_click156()])
            btn_156.place(x=450, y=300)

            btn_157 = Button(newwin, text="C11", bg="green", fg="white", height=1, width=3, command=lambda: [on_click157()])
            btn_157.place(x=490, y=300)

            btn_158 = Button(newwin, text="C12", bg="green", fg="white", height=1, width=3, command=lambda: [on_click158()])
            btn_158.place(x=530, y=300)

            btn_159 = Button(newwin, text="C13", bg="green", fg="white", height=1, width=3, command=lambda: [on_click159()])
            btn_159.place(x=570, y=300)

            btn_160 = Button(newwin, text="C14", bg="green", fg="white", height=1, width=3, command=lambda: [on_click160()])
            btn_160.place(x=610, y=300)

            btn_161 = Button(newwin, text="C15", bg="green", fg="white", height=1, width=3, command=lambda: [on_click161()])
            btn_161.place(x=650, y=300)

            btn_162 = Button(newwin, text="C16", bg="green", fg="white", height=1, width=3, command=lambda: [on_click162()])
            btn_162.place(x=690, y=300)

            btn_163 = Button(newwin, text="C17", bg="green", fg="white", height=1, width=3, command=lambda: [on_click163()])
            btn_163.place(x=730, y=300)

            btn_164 = Button(newwin, text="C18", bg="green", fg="white", height=1, width=3, command=lambda: [on_click164()])
            btn_164.place(x=770, y=300)

            btn_165 = Button(newwin, text="B1", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click165()])
            btn_165.place(x=10, y=330)

            btn_166 = Button(newwin, text="B2", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click166()])
            btn_166.place(x=50, y=330)

            btn_167 = Button(newwin, text="B3", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click167()])
            btn_167.place(x=90, y=330)

            btn_168 = Button(newwin, text="B4", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click168()])
            btn_168.place(x=130, y=330)

            btn_169 = Button(newwin, text="B5", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click169()])
            btn_169.place(x=170, y=330)

            btn_170 = Button(newwin, text="B6", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click170()])
            btn_170.place(x=210, y=330)

            btn_171 = Button(newwin, text="B7", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click171()])
            btn_171.place(x=250, y=330)

            btn_172 = Button(newwin, text="B8", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click172()])
            btn_172.place(x=290, y=330)

            btn_173 = Button(newwin, text="B9", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click173()])
            btn_173.place(x=330, y=330)

            btn_174 = Button(newwin, text="B10", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click174()])
            btn_174.place(x=450, y=330)

            btn_175 = Button(newwin, text="B11", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click175()])
            btn_175.place(x=490, y=330)

            btn_176 = Button(newwin, text="B12", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click176()])
            btn_176.place(x=530, y=330)

            btn_177 = Button(newwin, text="B13", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click177()])
            btn_177.place(x=570, y=330)

            btn_178 = Button(newwin, text="B14", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click178()])
            btn_178.place(x=610, y=330)

            btn_179 = Button(newwin, text="B15", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click179()])
            btn_179.place(x=650, y=330)

            btn_180 = Button(newwin, text="B16", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click180()])
            btn_180.place(x=690, y=330)

            btn_181 = Button(newwin, text="B17", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click181()])
            btn_181.place(x=730, y=330)

            btn_182 = Button(newwin, text="B18", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click182()])
            btn_182.place(x=770, y=330)

            btn_183 = Button(newwin, text="A1", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click183()])
            btn_183.place(x=10, y=360)

            btn_184 = Button(newwin, text="A2", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click184()])
            btn_184.place(x=50, y=360)

            btn_185 = Button(newwin, text="A3", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click185()])
            btn_185.place(x=90, y=360)

            btn_186 = Button(newwin, text="A4", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click186()])
            btn_186.place(x=130, y=360)

            btn_187 = Button(newwin, text="A5", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click187()])
            btn_187.place(x=170, y=360)

            btn_188 = Button(newwin, text="A6", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click188()])
            btn_188.place(x=210, y=360)

            btn_189 = Button(newwin, text="A7", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click189()])
            btn_189.place(x=250, y=360)

            btn_190 = Button(newwin, text="A8", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click190()])
            btn_190.place(x=290, y=360)

            btn_191 = Button(newwin, text="A9", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click191()])
            btn_191.place(x=330, y=360)

            btn_192 = Button(newwin, text="A10", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click192()])
            btn_192.place(x=450, y=360)

            btn_193 = Button(newwin, text="A11", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click193()])
            btn_193.place(x=490, y=360)

            btn_194 = Button(newwin, text="A12", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click194()])
            btn_194.place(x=530, y=360)

            btn_195 = Button(newwin, text="A13", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click195()])
            btn_195.place(x=570, y=360)

            btn_196 = Button(newwin, text="A14", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click196()])
            btn_196.place(x=610, y=360)

            btn_197 = Button(newwin, text="A15", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click197()])
            btn_197.place(x=650, y=360)

            btn_198 = Button(newwin, text="A16", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click198()])
            btn_198.place(x=690, y=360)

            btn_199 = Button(newwin, text="A17", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click199()])
            btn_199.place(x=730, y=360)

            btn_200 = Button(newwin, text="A18", bg="yellow", fg="black", height=1, width=3, command=lambda: [on_click200()])
            btn_200.place(x=770, y=360)

            lbl_bottom = Label(newwin, text="Screen this side", bg="grey", fg="white", height=1, width=80)
            lbl_bottom.place(x=110, y=410)

            lb_prices = Label(newwin, text="Blue code seats are Rs.250 each \n Green code seats are Rs.190 each \n"
                                           "Yellow code seats are Rs.150 each", bg="red", fg="white", height=5, width=60)
            lb_prices.place(x=190, y=460)

            btn_next = Button(newwin, text="Confirm and view Booking Details", command=dis)
            btn_next.place(x=300, y=550)

        sel_movie(self)



    def newWindow(self):  # new window definition
        self.query = StringVar()
        self.query1 = StringVar()

        newwin = Toplevel(root)
        newwin.title('Details of User')
        newwin.geometry("400x300")
        newwin.resizable(0, 0)

        display_name = Label(newwin, text="Enter your Name", fg="white", bg="red", width=20, height=3)
        display_name.pack()

        entry_name = Entry(newwin, width=50, textvariable=self.query)
        entry_name.pack()

        display_email = Label(newwin, text="Enter your Email-address", fg="white", bg="red", width=20, height=3)
        display_email.pack()

        entry_email = Entry(newwin, width=50, textvariable=self.query1)
        entry_email.pack()

        display_age = Label(newwin, text="Enter your age", fg="white", bg="red", width=20, height=3)
        display_age.pack()

        entry_age = Entry(newwin, width=50)
        entry_age.pack()

        submit = Button(newwin, text="Continue", command=lambda: [self.movie_details()])
        submit.pack()

        info = Label(newwin, text="By continuing you accept the terms \n and conditions of the corporation",
                     fg="white", bg="grey", width=50, height=5)
        info.pack()

    def mainFrame(self, root):
        root.title('Open New Window!!!')
        root.geometry("400x300")
        root.resizable(0, 0)

        title = Label(root, text="WELCOME TO MOVIE BOOKING SYSTEM", fg="white", bg="red", width=350, height=200)
        title.pack()

        button1 = Button(root, text="Proceed to Booking", command=lambda: [ self.newWindow()])
        button1.place(x=130, y=200, width=150, height=40)


root = Tk()
app = Frames()
app.mainFrame(root)
root.mainloop()

