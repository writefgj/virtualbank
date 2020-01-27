def hello(client_name):
	print('Здравствуйте,',client_name,'. Вас приветствует банк VIRTUAL MONEY')
def howmuch():
	money = int(input('Введите сумму депозита ->>>')) 
	print('Спасибо, Вы указали значение', money)
	money+=1000000
	print('Мы дарим Вам еще 1 000 000, теперь на Вашем счету: ',money,' долларов.')
def pay(earn):
	result=earn/100*30
	return result
def term(summ,permonth):
	result=summ//permonth
	return result
def client_audit(stage,earn):
	if earn>100000 and stage>5:
		print("Вам будет выдан кредит.")
		boo=True
	else:
		print("Маловато будет")
		boo=False
	return boo
client_name=input("Введите свое имя ->>>")
hello(client_name)
print('Капитализация банка $1 000 000')
print('Я могу говорить с человеком сколько угодно!')
print('Банк Ивана Иванова')
howmuch()
summ=int(input('Введите сумму кредита ->>'))
earn=int(input('Введите свой ежемесячный доход ->>'))
stage=int(input("Введите свой стаж ->>>"))
payment=pay(earn)
termcredit=term(summ,payment)
boo=client_audit(stage,earn)
if boo:
	print('Срок кредита составит: ',termcredit,'. Ежемесячный платеж: ',payment)
