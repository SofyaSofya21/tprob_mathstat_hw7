# Выбрать тест и проверить, есть  ли различия между выборками:
import numpy as np
import scipy.stats as stats

# 1)  Даны две  независимые выборки. Не соблюдается условие нормальности
# x1  380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции

x1 = np.array([380,420, 290])
y1 = np.array([140,360,200,900])
# кол-во выборок - 2, независимые --> используем критерий Манна Уитни
print(stats.mannwhitneyu(x1,y1)) 
# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)
# Статистически значимых различий между выборками не найдено

# -----------------------------------

# 2) Исследовалось влияние препарата на уровень давления пациентов. Сначала измерялось 
# давление до приема препарата, потом через 10 минут и через 30 минут. Есть ли статистически 
# значимые различия?
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150,  130, 135
# 3е измерение через 30 минут: 130, 130, 120, 130, 125

before = np.array([150, 160, 165, 145, 155])
after10min = np.array([140, 155, 150,  130, 135])
after30min = np.array([130, 130, 120, 130, 125])
# кол-во выборок - более 2, зависимые --> используем критерий Фридмана
print(stats.friedmanchisquare(before,after10min,after30min)) 
# FriedmanchisquareResult(statistic=9.578947368421062, pvalue=0.00831683351100441)
# Между выборками найдено статистически значимое различие, то есть препарат влияет на уровень давления

# -----------------------------------

# 3) Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.
before = np.array([150, 160, 165, 145, 155])
after10min = np.array([140, 155, 150,  130, 135])
# кол-во выборок - 2, зависимые --> используем критерий Уилкоксона
print(stats.wilcoxon(before,after10min))
# WilcoxonResult(statistic=0.0, pvalue=0.0625)
# Между выборками не найдено различий на уровне статистической значимости 0,05, препарат не влияет 
# на уровень давления в течение первых 10 минут (а влияет позже, с учетом предыдущего вывода)

# -----------------------------------

# 4) Даны 3 группы  учеников плавания. Сравнить результаты для спортсменов.
# В 1 группе время на дистанцию 50 м составляют:
# 56, 60, 62, 55, 71, 67, 59, 58, 64, 67
# Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
# Третья группа: 57,67, 49, 48, 47, 55, 66, 51, 54

gr1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
gr2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
gr3 = np.array([57,67, 49, 48, 47, 55, 66, 51, 54])
# кол-во выборок - более 2, независимые --> используем критерий Крускала-Уоллиса
print(stats.kruskal(gr1,gr2,gr3))
# KruskalResult(statistic=5.465564058257224, pvalue=0.0650380998590494)
# На уровне статистической значимости 0,05 различий между выборками нет




