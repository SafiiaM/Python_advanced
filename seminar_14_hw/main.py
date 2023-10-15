from company import Company


if __name__ == '__main__':
    mts = Company('mts')
    print(*mts.employes, sep='\n')
    print()
    employer = mts.log('Майя Шахкабзадовна Абесламидзе', '320200')
    new_employer_1 = mts.get_job(employer, 'Иван Иванович Иванов', "1", '123123')
    print(*mts.employes, sep='\n')
    new_employer_2 = mts.get_job(employer, 'Бронислав Алексеевич Дубровин', 7, '233322')