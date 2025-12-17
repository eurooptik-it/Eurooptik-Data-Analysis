from dataclasses import dataclass
from typing import Dict

@dataclass
class GoogleSheet:
    id: str
    pages: Dict[str, str]

GOOGLE_SHEETS = {
    "Raport_Produse" : GoogleSheet(
        id="1hEP1FkrOu_tt9qZ-nHbT21Rpr_vtPu4zlRj3bfGixZE",
        pages={
            "Accesorii_ochelari" : "2075315958",
            "Cristaline" : "1654924316",
            "Lentile" : "889129287",
            "Lentile_contact" : "1160367677",
            "Medicamente" : "269513616",
            "Ochelari_soare" : "1509980223",
            "Rame": "255546074",
        }
    ),
    "Raport_pacienti" : GoogleSheet(
        id="1Ethh9LJdfWv8DPUNzJ4SYLwV0ZAcUxBN5uQ9VGaLpIY",
        pages={
            "Pacienti" : "1821330140"
        }
    ),
    "Raport_bonuri_consum_2025" : GoogleSheet(
        id="1Il18d0YfNV1jgz2wmJnyQcM6UKKKRO2YC95tMCGCMPY",
        pages={
            "Bonuri_consum" : "1205015473"
        }
    ),
    "Raport_bonuri_comanda_2025" : GoogleSheet(
        id="1i6WoKZfx9oGJQlBQ5HUw5O_DZ4FH_lKRlDcn2KDP4S0",
        pages={
            "Bonuri_comanda" : "903488431"
        }
    ),
    "Borderou_facturi_2025" : GoogleSheet(
        id="1khdZFBRjbmCgyEL6l6CaOwXcdLMvZkglc4ox0akaWsM",
        pages={
            "Facturi" : "773106287"
        }
    ),
    "Raport_incasari" : GoogleSheet(
        id="1Cj6mNa6kaPOwckd-REVZsemOyCWKRPuMMIaVlwISxLc",
        pages={
            "Incasari_Iunie_2025": "1455833454",
            "Incasari_Mai_2025" : "1829298788",
            "Incasari_Aprilie_2025" : "1936663589",
            "Incasari_Martie_2025" : "1026830607",
            "Incasari_Februarie_2025" : "881321237",
            "Incasari_Ianuarie_2025" : "1302372194"
        }
    ),
    "Clienti" : GoogleSheet(
        id="1mY10dR51F4yTfUt5Ss5gcqLWdh6x6fi8bBO0XlEpNxk",  
        pages={
            "Clienti" : "1806100243"
        }
    )
}

KNOWN_BRANDS = ['ANA HICKMANN', 'ARMANI EXCHANGE', 'ARNETTE', 'AVANGLION',
                'BABY-HIPPO', 'BURBERRY','BVLGARI',
                'CALVIN KLEIN', 'CELINE',
                'DIOR', 'DOLCE&GABBANA',
                'EMPORIO ARMANI', 'ENOX', 'ESCHENBACH',
                'FIELMANN', 'FITCHE', 'FURLA',
                'GANT', 'GIORGIO ARMANI', 'GUESS',
                'HARLEY DAVIDSON', 'HELLO KITTY', 'HICKMANN',
                'JIMMY CHOO',
                'MICHAEL KORS', 'MISS SIXTY',
                'OAKLEY',
                'POLICE', 'PRADA', 
                'RALPH LAUREN', 'RAY BAN',
                'SFEROFLEX', 'SILHOUETTE', 'SWAROVSKI',
                'VALENTINO', 'VERSACE', 'VOGUE'
                ]