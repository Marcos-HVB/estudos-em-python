totalSegundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))



dias = totalSegundos // 86400

segundosRestantesHoras = totalSegundos % 86400

horas = segundosRestantesHoras // 3600 
segundosRestantesMinutos = segundosRestantesHoras % 3600

minutos =  segundosRestantesMinutos // 60
segundosRestantes = segundosRestantesMinutos % 60


print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundosRestantes,"segundos.")
