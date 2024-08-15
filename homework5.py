mutable_list = ["computer", "television", "console"]
print(mutable_list[1])
mutable_list[1] = "telephone"
print(mutable_list)


immutable_var = (1, 2, 3, 4, 5)
print(tuple(immutable_var))
immutable_var[0] = 6
print(immutable_var)
#Нельзя изменить кортеж потому что это неизменяемый вид хранения данных в сравнения со списками
