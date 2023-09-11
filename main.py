import re
from datetime import datetime
from Timestamp import Timestamp

## Altere AQUI o nome dos arquivos, se nescessário
read_file_name = "input_text.txt"
write_file_name = "output_text.txt"
log_file_name = "change_log.txt"

read_file = open(read_file_name, 'r')
all_lines = read_file.readlines()
read_file.close()

write_file = open(write_file_name, 'w')
change_log = open(log_file_name, 'a')
change_log.write(f"Iniciando incremento de uma hora do arquivo {read_file_name} para o arquivo {write_file_name}\n")


def update_change_log(message):
    now = datetime.now()
    message = now.strftime("%d/%m/%Y\t%H:%M:%S\t") + message + "\n"
    change_log.write(message)
    
i = 1
result = []
for line in all_lines:
    if re.search("^([0-9]{2}:?){2,} - ([0-9]{2}:?){2,}$", line):
        t = Timestamp(line)
        if t == False :
            update_change_log(f"## ERRO \t Falha ao converter {line}. na linha {i}")
        else:
            t.incrementHour()
            line = line.rstrip('\n')
            newTime = t.getString().rstrip('\n')
            update_change_log(f"Transformando \"{line}\" em \"{newTime}\". (Incremento de uma hora no timestamp da linha {i})")
            result.append(newTime)
    else:
        result.append(line) 
    i+=1


write_file.writelines(result)
change_log.write("__________________________\n\n\n")
write_file.close()
change_log.close()
