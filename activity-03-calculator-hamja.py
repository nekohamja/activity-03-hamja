import calculator_script_1_stat as totalhp
import calculator_script_1_stat as totalatk
import calculator_script_1_stat as totaldef
import calculator_script_1_stat as totsatk
import calculator_script_1_stat as totsdef
import calculator_script_1_stat as totalspd
import calculator_script_2_ev as evatk
import calculator_script_2_ev as evdef
import calculator_script_2_ev as evsatk
import calculator_script_2_ev as evsdef
import calculator_script_2_ev as evspd

# Nature Library
nature_list = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish", "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet", "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky"]


print("Choose A Calculator")
print("  ")
print("1. Stat Calculator \n2. EV Calculator \n3.Exit")
choose = int(input("Select Mode: "))
match choose:
        
    case 1:
        print("1. Pokemon's HP \n2. Pokemon's Other Stat")
        statch = input(("Select the Function you will use: "))
        while statch != "1" and statch != "2":
            print("Invalid input, Try again!")
            statch = input(("Select the Function you will use: "))


        if statch == "1":
            level = int(input("\nLevel: "))
            while level > 100:
                print("Maxium value is 100")
                level = input(input("LEVEL: "))
            hp = int(input("HP: "))

            iv = int(input("IV: "))
            while iv > 31:
                print("Given value is only between 0 - 31 only")
                iv = int(input("IV: "))

            ev = int(input("EV: "))
            while ev > 255:
                print("Given value is only between 0 - 255 only")
                ev = int(input("EV: "))

            print("\n")
            print("HP =", totalhp.PokemonSTAT.tothpReturnWithParams(hp,iv,ev,level), end='\n\n')
            print("\nSystem Terminated")


        elif statch == "2":
            poke = input("\nEnter your Pokemon Name: ")
            level = int(input("Enter your Pokemon Level: "))
            # NATURE's code
            nature = input("Nature: ")
            while nature not in nature_list:
                print("\nIncorrect Input of Pokemon Nature, Please Try again!")
                nature = input("Nature: ")
            # ATK's code
            baseatk = int(input("\nATK: "))
            iv_atk = int(input("IV: "))
            while iv_atk > 31:
                print("IV value Only between 0 and 31 only.")
                iv_atk = int(input("IV: "))
            
            ev_atk = int(input("EV: "))
            while ev_atk > 255:
                print("EV value Only between 0 and 255 only.")
                ev_atk = int(input("EV: "))
            # DEF's code
            basedef = int(input("\nDEF: "))
            iv_def = int(input("IV: "))
            while iv_def > 31:
                print("IV value Only between 0 and 31 only.")
                iv_def = int(input("IV: "))
            
            ev_def = int(input("EV: "))
            while ev_def > 255:
                print("EV value Only between 0 and 255 only.")
                ev_def = int(input("EV: "))
            # SP ATK's code
            basesatk = int(input("\nSP. ATK: "))
            iv_satk = int(input("IV: "))
            while iv_satk > 31:
                print("IV value Only between 0 and 31 only.")
                iv_satk = int(input("IV: "))
            
            ev_satk = int(input("EV: "))
            while ev_satk > 255:
                print("EV value Only between 0 and 255 only.")
                ev_satk = int(input("EV: "))
            # SP DEF's code
            basesdef = int(input("\nSP. DEF: "))
            iv_sdef = int(input("IV: "))
            while iv_atk > 31:
                print("IV value Only between 0 and 31 only.")
                iv_sdef = int(input("IV: "))
            
            ev_sdef = int(input("EV: "))
            while ev_sdef > 255:
                print("EV value Only between 0 and 255 only.")
                ev_sdef = int(input("EV: "))
            # SPD's code
            basespd = int(input("\nSPD: "))
            iv_spd = int(input("IV: "))
            while iv_spd > 31:
                print("IV value Only between 0 and 31 only.")
                iv_spd = int(input("IV: "))
            
            ev_spd = int(input("EV: "))
            while ev_spd > 255:
                print("EV value Only between 0 and 255 only.")
                ev_spd = int(input("EV: "))

            
            print("\n")
            print("Pokemon", poke, "a Lvl.", level, "with", nature, "nature, Overall Stats:")
            # Total's code
            print("\nATK =", totalatk.PokemonSTAT.totatkReturnWithParams(level,baseatk,iv_atk,ev_atk,nature), end='\n\n')
            print("DEF =", totaldef.PokemonSTAT.totdefReturnWithParams(level,basedef,iv_def,ev_def,nature), end='\n\n')
            print("SP. ATK =", totsatk.PokemonSTAT.totsatkReturnWithParams(level,basesatk,iv_satk,ev_satk,nature), end='\n\n')
            print("SP. DEF =", totsdef.PokemonSTAT.totsdefReturnWithParams(level,basesdef,iv_sdef,ev_sdef,nature), end='\n\n')
            print("SPD =", totalspd.PokemonSTAT.totspdReturnWithParams(level,basespd,iv_spd,ev_spd,nature), end='\n\n')
            print("\nSystem Terminated")
    #Overall stat 
    case 2:
        print("\n")
        base = int(input("Actual STAT: "))
        stat = int(input("Increase STAT: "))
        level = int(input("Selected LEVEL: "))
        while level > 100:
            print("Maxium value is 100 only")
            level = input(input("Select LEVEL: "))
        nature = input("Nature: ")
        while nature not in nature_list:
            print("\nIncorrect Input of Pokemon Nature, Please Try again!")
            nature = input("Nature: ")
        iv = int(input("IV: "))
        ev = int(input("EV: "))
        
        print("\nEFFORT VALUES NEEDED IN:")
        print("\nATK =", evatk.PokemonEV.evatkReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("DEF =", evdef.PokemonEV.evdefReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("SP ATK =", evsatk.PokemonEV.evsatkReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("SP DEF =", evsdef.PokemonEV.evsdefReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("SPD =", evspd.PokemonEV.evspdReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("\nSystem Terminated")
    case 3:
        exit()    

    case default:
        print("Invalid Input, System Terminated.")