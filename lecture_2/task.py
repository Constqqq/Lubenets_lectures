from rich import print as rprint

akterli = input('Hochesh` bit` actor???? (Da/Net)' )
if akterli.lower() == 'da':
    role_select = input('Kem budesh (Hulk/Loki)')
    if role_select.lower() == 'loki':
        parent_select = input('kogo lubish bolshe (Mamu/Papu)')
        if parent_select.lower() == 'mamu':
            rprint ('[bold italic blue] go to papa')
        elif parent_select.lower() == 'papu':
            rprint ('[bold italic blue] go home broski')
        else:
            rprint ('[bold red] u need to write MAMU or PAPU debil')
    elif role_select.lower() == 'hulk':   
            biceps = str(input('Skolko biceps sm3?'))
            if biceps.isdigit():
                biceps_int = int(biceps)    
                if biceps_int >=60:
                    rprint('[bold green] Ty prinyat')
                elif biceps_int < 60:
                    print('go home boi')
                else:
                    rprint ('[red] mimo')
            else:
                rprint('[bold red] Nyzhno ciferky')
    else:
        rprint ('[red] mimo')
elif akterli.lower() == 'net':
    rprint ('[bold purple] shapka v dveri')         
else:
    rprint ('[red] mimo')