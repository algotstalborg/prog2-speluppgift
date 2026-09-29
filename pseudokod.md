'''
SPEL
    Starta spelet
        Skapa spelare
        Skapa kortlek
        Visa start meny
            Låt spelaren välja karaktär
            Träffa valen

    Spel loop
        Spelaren väljer nästa plats

        Om distansen till bossen är 0
            Starta boss strid
                slumpa vilken boss
                Om vinst
                    Om alla bossar döda
                        Avsluta spelet
                    Annars 
                        ge boss relic

        Om platsen är en fiende
            starta strid
            Om vinst 
                ge normal loot

        Eller om platsen är en elit fiende
            starta elit strid
            Om vinst
                ge elit loot 
        
        Eller om platsen är en kista
            ge normal loot
            ge en relic

        Eller om platsen är en affär
            Visa varor
                Kort
                Relics
                Ta bort ett kort tjänst
'''