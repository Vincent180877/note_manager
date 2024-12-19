username=input("Имя пользователя ")
title=input("Заголовок заметки ")
title_1=input("Подзаголовок 1 ")
title_2=input("Подзаголовок 2 ")
title_3=input("Подзаголовок 3 ")
title_=[title_1,title_2,title_3]
content=input("Описание заметки ")
status=input("Статус заметки ")
created_date=input("Дата создания заметки:день-месяц-год ")
issue_date=input("Дата истечения заметки:день-месяц-год ")
note=[username,title,content,status,created_date[:5],issue_date[:5],[title_1,title_2,title_3]]
print(note)