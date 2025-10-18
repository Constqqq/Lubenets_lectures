from rich import print as rich_print

rich_print (
    "[bold blue] Darova friend frm moscov"
)
rich_print ("today film [bold red]smeshariki[/bold red]")
decision = input("lesgoshkins?[Da/Net]: ")
#print(decision.capitalize())
if decision.lower() == 'da':
    age = int(input('skoka rokiv'))
    if age >= 18:
        rich_print('[bold green] super go')
    elif age <= 0:
        rich_print ('[bold red] Ebanat')
    else:
        rich_print ('[bold cyan]kisi kisi meow meow kisi kisi meow meow meow')
elif decision.lower == 'net':
    print('[bold red]zaebis')
else:
    print ('404')