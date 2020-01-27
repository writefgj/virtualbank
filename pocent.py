money=int(input('Введите сумму ->>>'))
proc=int(input('Введите процент от суммы ->>>'))
result=money/100*proc
print(proc,'% от числа',money,' составляет:',result)

money=int(input('Введите сумму ->>>'))
srok=int(input('Введите срок кредита в месяцах ->>>'))
print('Ваш ежемесячный платеж составит: ',money/srok)