import csv
import random

#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####


filename = "books-en.csv"  # replace with your file name


###############количество записей и строк####################

def EnteryCounter():
       
     with open (filename , mode = 'r') as csv_file:
        csv_reader =  csv.DictReader(csv_file)
        line_num = 0
        entry_num = 0

        for row in csv_reader:
            if line_num == 0:
                line_num += 1
                entry_num += 7
                print(f'Названия столбцов в CSV-файле: {", ".join(row)}')

            line_num += 1
            entry_num += 7
        print(f'{line_num} строк обнаружено.')
        print(f'{entry_num} записей обнаружено.')

EnteryCounter()

###################################



############количество записей, содержащих строку длиннее 30 символов############

def CharacterReader(num):
  with open(filename, mode='r') as File:
    csvReader = csv.DictReader(File)
    numBooks = 0

    for row in csvReader:
        counter = 0
        for c in row["Book-Title"] :  
            counter+=1  
        if counter > num :
              numBooks +=1
        
    print(f'количество записей, содержащих строку длиннее {num} символов, равно {numBooks} книгам.')

CharacterReader(30)

###################################



################Книги от 150 руб###################

def PriceFrom(n):
         with open (filename , mode = 'r') as csv_file:
            csvReader = csv.DictReader(csv_file)
            booksFrom = 0

            for row in csvReader:
                if row["Price"].isnumeric():
                    Price = row["Price"]
                    if int(Price) > n:
                        booksFrom +=1
            print(f'количество записей более {n} рублей  {booksFrom} книг.')

PriceFrom(150)

###################################




#################Произвольно выбранные записи##################

def Random(n):
    
    with open(filename, "r") as file:
        csvReader = csv.reader(file)
        next(csvReader)
        return(random.choice([line[n] for line in csvReader]) )

def RandomEntries():
    with open('Произвольно выбранные записи.txt', 'w',encoding="utf-8") as f:

        for x in range(0, 20):
            AuthorOfBook = "<автор>: "
            NameOfBook =" - <название>: "
            YearOfPublish = " - <год>: "
            lines = [str(AuthorOfBook),str(Random(1)),str(NameOfBook), str(Random(2)),str(YearOfPublish) , str(Random(3))]
            print(lines)
            f.writelines(lines)
            f.write('\n')

RandomEntries()

###################################



####################Доп Задание#######################


###############Уникальные издатели####################

def UniquePublisher():

    # Открываем файл CSV и создаем список словарей, представляющих данные
    rows = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    # теперь мы находим уникальных издателей
    unique_publishers = set()
    duplicate_publishers = set()
    for row in rows:
        publisher = row["Publisher"]
        if publisher in unique_publishers:
            duplicate_publishers.add(publisher)
        else:
            unique_publishers.add(publisher)

    #отфильтровываем повторяющиеся строки
    unique_rows = [row for row in rows if row["Publisher"] not in duplicate_publishers]

    # записываем уникальные строки в выходной файл
    with open("UniquePublisher.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Downloads", "Price"])
        for row in unique_rows:
            writer.writerow([row["ISBN"], row["Book-Title"], row["Book-Author"], row["Year-Of-Publication"], row["Publisher"], row["Downloads"], row["Price"]])

UniquePublisher()

###################################



################20 самых популярных книг###################

def PopularBook():

    # Открываем файл CSV и создаем список словарей, представляющих данные
    rows = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["Downloads"] = int(row["Downloads"])
                rows.append(row)
            except ValueError:
                pass

   # сортируем строки по загрузкам (в порядке убывания)
    rows.sort(key=lambda x: x["Downloads"], reverse=True)

    # мы печатаем первые 20 строк, а затем сохранить в файл csv
    print("{:<15} {:<50} {:<30} {:<20} {:<40} {:<15} {:<10}".format(
        "ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Downloads", "Price"))
    for row in rows[:20]:
        print(
            row["ISBN"], row["Book-Title"], row["Book-Author"], row["Year-Of-Publication"],
            row["Publisher"], row["Downloads"], row["Price"])
        

     
    top_rows = sorted(rows, key=lambda row: row["Downloads"], reverse=True)[:20]
    
    with open("TOP20.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Downloads", "Price"])
        for row in top_rows:
            writer.writerow([row["ISBN"], row["Book-Title"], row["Book-Author"], row["Year-Of-Publication"], row["Publisher"], row["Downloads"], row["Price"]])

PopularBook()

###################################