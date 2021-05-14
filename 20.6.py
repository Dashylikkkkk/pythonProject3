def do_bet(num, bet):
    global bets
    if bet == 0 or num in bets or num>10 or num<1:
        print("Что-то пошло не так, попробуйте еще раз")
    else:
        print("Ваша ставка в размере " + str(bet) + " на лошадь " + str(num) + " принята")
        bets.append(num)


bets = []
do_bet(1, 10)
do_bet(1, 100)
do_bet(2, 0)
do_bet(2, 200)
